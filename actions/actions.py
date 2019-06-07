# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests, json
from typing import Dict, Text, Any, List, Union
from rasa_sdk import Tracker, Action
from rasa_sdk.events import SlotSet, UserUtteranceReverted, FollowupAction, Restarted, UserUttered
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher

import modules.constants as const
import modules.nlu_helper as nlu

import modules.datamodel.mind as mind
from modules.datamodel import Stakeholder, Option, Consequence, Deed, Context

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Intro(Action):
    """ 
    Initial Action to be executed
    
    Triggered by:
    * Intent 'greeting'

    Required slots: /

    Returns: /
    """
    def name(self):
        return "action_intro"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_intro_1', tracker)
        dispatcher.utter_template('utter_intro_2', tracker)
        dispatcher.utter_template('utter_ask_stakeholders', tracker)
        

class UpdateContext(Action):
    """
    Context entity holding information about the situation
    No Create-Method, because there is only one context

    Triggered by:
    * Intent 'moralquestion'

    Required slots: /

    Returns: 
    * action_return = True if context was updated
    * action_return = False if no update was made
    """
    def name(self):
        return 'action_update_context'

    def run(self, dispatcher, tracker, domain):
        action_return = False

        if (tracker.latest_message['intent'].get('name') == 'moralquestion'):
            context = mind.get_context_singleton(tracker.sender_id)
            context['moralquestion'] = tracker.latest_message['text']
            context.memorize(tracker.sender_id)
            
            dispatcher.utter_template('utter_got_it', tracker)
            action_return = True

        return [SlotSet('action_return', action_return)]


#########################
#                       #
#      STAKEHOLDER      #
#                       #
#########################
class CreateStakeholder(Action):
    """
    Create a new stakeholder and write it to the datamodel

    Triggered by:
    * Intent 'stakeholder'
    * Intent 'decider'

    Required slots:
    * moralstatus == moral status of the stakeholder (human, machine or animal)

    Returns:
    * action_return = True if stakeholder was created with correct amount
    * action_return = False if stakeholder was created with unspecific amount (-1)
    * amount_stakeholders = amount of stakeholders in the datamodel after inserting the new one
    * moralstatus = None if no moral status was detected, to prevent that a previous status is considered again
    """
    def name(self):
        return "action_create_stakeholder"

    def run(self, dispatcher, tracker, domain):
        events = []

        sh = Stakeholder({  
            'decider': False, 
            'moral_status': const.MS_OTHER, 
            'moral_status_weight': 1,
            'amount': -1.1 # The 0.1 indicate that the amount was not asked for yet
        })

        # Do we know whether it is a single stakeholder or a group of people?
        if (tracker.latest_message['intent'].get('name') == 'stakeholder') or \
            (tracker.latest_message['intent'].get('name') == 'decider'):
            sh['amount'] = 1
        elif (tracker.latest_message['intent'].get('name') == 'stakeholdergroup'):
            sources = list(tracker.get_latest_entity_values('stakeholder'))
            quantity = nlu.get_quantity_from_sources(sources)
            if not quantity == -1:
                sh['amount'] = int(quantity)
        else:
            # Misclassified intent - try to retrieve a quantity, else assume a single person
            sources = list(tracker.get_latest_entity_values('stakeholder'))
            sources.extend(list(tracker.get_latest_entity_values('quantity')))
            quantity = nlu.get_quantity_from_sources(sources)
            if not quantity == -1:
                sh['amount'] = int(quantity)
            else:
                sh['amount'] = 1

        # Is a moral status identified?
        moralstatus = next(tracker.get_latest_entity_values('moralstatus'), None)
        if moralstatus == None:
            events.append(SlotSet('moralstatus', None))
        else:
            sh.set_moral_status(moralstatus)

        # Is the stakeholder recognized as the decider?
        if (tracker.latest_message['intent'].get('name') == 'decider'):
            sh['decider'] = True

        # Remember synonym, maybe the user refuses to call the person by its new name
        synonym = next(tracker.get_latest_entity_values('stakeholder'), None)
        if not synonym == None:
            sh['synonym'] = synonym

        sh.memorize(tracker.sender_id) 

        events.append(SlotSet("amount_stakeholders", mind.get_num_stakeholders(tracker.sender_id)))
        events.append(SlotSet("action_return", sh['amount'] != -1.1))

        return events


class UpdateStakeholder(Action):
    """
    Update an existing stakeholder

    Triggered by:
    * Intent 'quantity'     (user specified the amount of stakeholders OR the moral status weight, hopefully between 1 and 10)
    * Intent 'decider'
    * Intent 'name'
    * Intent 'correct'      (user confirmed name recognized by the bot)
    * Intent 'wrong'        (user rejected name recognized by the bot)
    * Intent 'dontknow'     (user does not know the proposed stakeholders name)
    * Intent 'deny'         (user does not tell the proposed stakeholders name)
    * Intent 'moralstatus'  

    Required slots: /

    Returns:
    * action_return = True if stakeholder was successfully updated
    * action_return = False if no update was made
    * decider = name of the stakeholder if he is the decider
    * name = name of the stakeholder if it was freshly assigned
    """
    def name(self):
        return "action_update_stakeholder"

    def run(self, dispatcher, tracker, domain):
        events = []
        action_return = False

        # In general, the last inserted stakeholder is the one we are talking about
        sh = mind.get_recent_stakeholder(tracker.sender_id)

        try:
            # Intent: decider
            if (tracker.latest_message['intent'].get('name') == 'decider'):
                # In this case, the stakeholder to be updated comes with the button payload
                sh = mind.get_stakeholder_by_name(tracker.sender_id, next(tracker.get_latest_entity_values('name'), None))
                sh['decider'] = True        
                events.append(SlotSet('decider', sh['name']))
                mind.memorize(tracker.sender_id, sh)
                dispatcher.utter_template('utter_got_it', tracker)
                action_return = True

            # Intent: quantity
            elif (tracker.latest_message['intent'].get('name') == 'quantity'):
                # We always ask for the amount of stakeholders before we ask for moral status
                # Therefore: If the amount is still set to -1.1, we did not ask yet
                if sh['amount'] == -1.1:
                    sources = list(tracker.get_latest_entity_values('quantity'))
                    sources.extend(list(tracker.get_latest_entity_values('stakeholder')))
                    sources.append(tracker.latest_message['text'])
                    quantity = nlu.get_quantity_from_sources(sources)

                    sh['amount'] = quantity
                    mind.memorize(tracker.sender_id, sh)
                    
                    if quantity != -1:      
                        action_return = True

                        if quantity > 1:
                            dispatcher.utter_message('I see, {} are involved.'.format(sh['amount']))
                        else:
                            dispatcher.utter_template('utter_reflect_single_person', tracker)
                    else:
                        logger.warning('Could not determine amount of stakeholders in message classified as quantity')
                        action_return = False
                        dispatcher.utter_template('utter_not_sure', tracker)
                    
                # Else we asked for the moral status weight
                else:
                    sources = list(tracker.get_latest_entity_values('quantity'))
                    sources.append(tracker.latest_message['text'])
                    weight = nlu.get_quantity_from_sources(sources)
                    
                    sh.set_moral_status_weight(weight).memorize(tracker.sender_id)
                    dispatcher.utter_message('Okay, I will consider the moral status of {} to be a proportion of {} compared to a human.'.format(sh['name'], sh['moral_status_weight']))
                    action_return = True

            # Intent: name or correct
            elif (tracker.latest_message['intent'].get('name') == 'name') \
                or (tracker.latest_message['intent'].get('name') == 'correct') \
                or (tracker.latest_message['intent'].get('name') == 'stakeholder') \
                or (tracker.latest_message['intent'].get('name') == 'stakeholdergroup'):

                if tracker.latest_message['intent'].get('name') == 'correct':
                    name = tracker.get_slot('name')
                else:
                    name = next(tracker.get_latest_entity_values('name'), None)
                    if name == None:
                        name = next(tracker.get_latest_entity_values('stakeholder'), None)

                    # Assure that the name is not already assigned
                    if not mind.get_stakeholder_by_name(tracker.sender_id, name) == None:
                        name = None

                if not name == None:
                    sh.set_name(s_id=tracker.sender_id, name=name).memorize(tracker.sender_id)
                    dispatcher.utter_message('Alright, from now on I will use the name "{}"!'.format(sh['name']))
                else:
                    sh.set_name(s_id=tracker.sender_id).memorize(tracker.sender_id)
                    dispatcher.utter_message('I am not sure if I understood the name correctly. To avoid misunderstandings I will just use the name "{}"!'.format(sh['name']))

                if (sh['decider'] == True):
                    events.append(SlotSet('decider', sh['name']))
                events.append(SlotSet('name', sh['name']))

                action_return = True

            # Intent: wrong
            elif (tracker.latest_message['intent'].get('name') == 'wrong'):
                sh.set_name(s_id=tracker.sender_id).memorize(tracker.sender_id)
                dispatcher.utter_message('Okay, then I will just use the name "{}" when talking about this person.'.format(sh['name']))

                if (sh['decider'] == True):
                    events.append(SlotSet('decider', sh['name']))
                events.append(SlotSet('name', sh['name']))

                action_return = True

            # Intent: dontknow or deny
            elif (tracker.latest_message['intent'].get('name') == 'dontknow') \
                or (tracker.latest_message['intent'].get('name') == 'deny'):

                if sh['amount'] == -1.1:
                    # Flag amount such that we know the question is through
                    sh['amount'] = -1
                    mind.memorize(tracker.sender_id, sh)
                    action_return = False
                    dispatcher.utter_template('utter_too_bad', tracker)
                else:
                    sh.set_name(s_id=tracker.sender_id).memorize(tracker.sender_id)
                    dispatcher.utter_message('Okay, I will just use the name "{}" from now on!'.format(sh['name']))
                    
                    if (sh['decider'] == True):
                        events.append(SlotSet('decider', sh['name']))
                    events.append(SlotSet('name', sh['name']))

                    action_return = True

            # Intent: moralstatus
            elif (tracker.latest_message['intent'].get('name') == 'moralstatus'):
                sh.set_moral_status(tracker.get_slot('moralstatus')).memorize(tracker.sender_id)
                dispatcher.utter_template('utter_got_it', tracker)
                action_return = True

        except (AttributeError, TypeError) as e:
            logger.warning('Exception updating Stakeholder: ' + str(e))
            events.append(SlotSet('name', None))
            action_return = False

        events.append(SlotSet('action_return', action_return))
        return events


#########################
#                       #
#        OPTION         #
#                       #
#########################
class CreateOption(Action):
    """
    Create an option of possible action

    Triggered by:
    * Intent 'option'

    Required slots: /

    Returns:
    * action_return = True if an option was successfully created
    * action_return = False if no option was created
    * deed = next deed to be commented by the user
    """
    def name(self):
        return 'action_create_option'

    def run(self, dispatcher, tracker, domain):
        deeds = list(tracker.get_latest_entity_values('deed'))

        if len(deeds) > 0:
            label = deeds[0]
        else:
            label = 'Option {}'.format(mind.get_num_options(tracker.sender_id) + 1)

        Option({ "deeds_tmp": deeds, "label": label }).memorize(tracker.sender_id)
        
        try:
            current_deed = deeds[0]
        except IndexError:
            current_deed = None

        return [SlotSet("deed", current_deed), SlotSet("action_return", True)]


class UpdateOption(Action):
    """
    Update an existing Option

    Triggered by:
    * Intent 'correct' after 'utter_ask_option_universalizable'
    * Intent 'wrong' after 'utter_ask_option_universalizable' OR 'utter_ask_identified_deed' (check if relevant or not)
    * Intent 'affirm' after 'utter_ask_option_inherent_evil'
    * Intent 'deny' after 'utter_ask_option_inherent_evil'

    Required slots: 
    * deed == deed the bot is currently talking about

    Returns:
    * action_return = True if option was updated
    * action_return = False if no update was made

    """
    def name(self):
        return 'action_update_option'

    def run(self, dispatcher, tracker, domain):
        action_return = False
        events = []

        try:
            option = mind.get_recent_option(tracker.sender_id)

            # Update universalizability and inherent_evil
            if (tracker.latest_message['intent'].get('name') == 'correct'):
                option['universalizable'] = True
                option['inherent_evil'] = False
                action_return = True
            
            elif (tracker.latest_message['intent'].get('name') == 'wrong'):
                # The 'name' entity is abused in this case
                deed_or_option = next(tracker.get_latest_entity_values('name'), None)

                if deed_or_option == 'deed':
                    option['deeds_tmp'].remove(tracker.get_slot('deed'))
                    
                    if len(option['deeds_tmp']) > 0:
                        current_deed = option['deeds_tmp'][0]
                    else:
                        current_deed = None
                        del option['deeds_tmp']

                    action_return = True
                    events.append(SlotSet("deed", current_deed))
                elif deed_or_option == 'option':
                    option['universalizable'] = False
                    action_return = True

            elif (tracker.latest_message['intent'].get('name') == 'affirm'):
                option['inherent_evil'] = True
                action_return = True
                
            elif (tracker.latest_message['intent'].get('name') == 'deny'):
                # The 'name' entity is abused in this case once again
                reason = next(tracker.get_latest_entity_values('name'), None)
                if reason == 'too_specific':
                    option['no_rule_reason'] = 'a more general formulated rule could apply in this case!'
                elif reason == 'needs_conditions':
                    option['no_rule_reason'] = 'a general rule could be applied under certain conditions!'

                option['inherent_evil'] = False
                action_return = True
            
            if action_return == True:
                option.memorize(tracker.sender_id)
                dispatcher.utter_template('utter_got_it', tracker)
        except (AttributeError, TypeError) as e:
            logger.warning('Exception updating Option: ' + str(e))
            action_return = False
            dispatcher.utter_template('utter_not_sure', tracker)

        events.append(SlotSet("action_return", action_return))
        return events


#########################
#                       #
#         DEED          #
#                       #
#########################
class CreateDeed(Action):
    """
    Create a deed which is associated with an option

    Triggered by:
    * Intent 'correct' after 'utter_ask_deed'
    * Intent 'deed'

    Required slots:
    * deed == the deed the bot is currently talking about

    Returns:
    * action_return = True if deed was created
    * action_return = False if deed was not created
    * deed = The deed the bot is currently talking about
    """
    def name(self):
        return 'action_create_deed'

    def run(self, dispatcher, tracker, domain):
        action_return = False
        events = []

        if (tracker.latest_message['intent'].get('name') == 'deed'):
            label = next(tracker.get_latest_entity_values('deed'), None)
            if label == None:
                label = tracker.latest_message['text']
                events.append(SlotSet('deed', label))

        elif (tracker.latest_message['intent'].get('name') == 'correct'):
            label = tracker.get_slot('deed')

        if not label == None:
            recent_option = mind.get_recent_option(tracker.sender_id)
            Deed({"label": label, "option": recent_option.doc_id}).memorize(tracker.sender_id)
            action_return = True
        else:
            dispatcher.utter_template('utter_not_sure', tracker)

        events.append(SlotSet('action_return', action_return))
        return events


class UpdateDeed(Action):
    """
    Update an existing Deed

    Triggered by:
    * Intent 'correct' after 'utter_ask_deed_universalizable'
    * Intent 'wrong' after 'utter_ask_deed_universalizable'
    * Intent 'affirm' after 'utter_ask_deed_inherent_evil'
    * Intent 'deny' after 'utter_ask_deed_inherent_evil'

    Required slots: /

    Returns:
    * action_return = True if deed was updated
    * action_return = False if no update was made
    * deed = Next deed in the list to be checked
    """
    def name(self):
        return 'action_update_deed'

    def run(self, dispatcher, tracker, domain):
        action_return = False
        events = []

        try:
            deed = mind.get_deed(tracker.sender_id, tracker.get_slot('deed'))
        
            # Update universalizability and inherent_evil
            if (tracker.latest_message['intent'].get('name') == 'correct'):
                deed['universalizable'] = True
                deed['inherent_evil'] = False
                action_return = True
            elif (tracker.latest_message['intent'].get('name') == 'wrong'):
                deed['universalizable'] = False
                action_return = True
            elif (tracker.latest_message['intent'].get('name') == 'affirm'):
                deed['inherent_evil'] = True
                action_return = True
            elif (tracker.latest_message['intent'].get('name') == 'deny'):
                # The 'name' entity is abused in this case
                reason = next(tracker.get_latest_entity_values('name'), None)
                if reason == 'too_specific':
                    deed['no_rule_reason'] = 'a more general formulated rule could apply in this case!'
                elif reason == 'needs_conditions':
                    deed['no_rule_reason'] = 'a general rule could be applied under certain conditions!'

                deed['inherent_evil'] = False
                action_return = True
            
            if action_return == True:
                deed.memorize(tracker.sender_id)
                dispatcher.utter_template('utter_got_it', tracker)

            # Remove current and select next deed from list, if available
            if ('universalizable' in deed and 'inherent_evil' in deed):
                option = mind.get_recent_option(tracker.sender_id)

                if deed['label'] in option['deeds_tmp']:
                    option['deeds_tmp'].remove(deed['label'])
                    option.memorize(tracker.sender_id)

                if len(option['deeds_tmp']) > 0:
                    events.append(SlotSet("deed", option['deeds_tmp'][0]))
                else:
                    events.append(SlotSet("deed", None))
                    del option['deeds_tmp']

        except (AttributeError, TypeError) as e:
            logger.warning('Exception updating deed: ' + str(e))
            action_return = False
            dispatcher.utter_template('utter_not_sure', tracker)

        events.append(SlotSet("action_return", action_return))
        return events

#########################
#                       #
#     CONSEQUENCE       #
#                       #
#########################
class CreateConsequence(Action):
    """
    Create a consequence of an option

    Triggered by:
    * Intent 'consequence'

    Required slots:
    * sentiment == sentiment of the last sentence (pos/neu/neg)

    Returns:
    * action_return = True if consequence was created
    * action_return = False if consequence was not created (propably because affected stakeholder is unknown)
    """
    def name(self):
        return 'action_create_consequence'

    def run(self, dispatcher, tracker, domain):
        events = []
        action_return = False
        option = mind.get_recent_option(tracker.sender_id)

        if tracker.get_slot('sentiment') == 'pos':
            impact = 1
        elif tracker.get_slot('sentiment') == 'neg':
            impact = -1
        else:
            impact = 0

        # Find out, which stakeholder is affected by this consequence
        try:
            names = list(tracker.get_latest_entity_values('name'))
            aff_stkhs = []
            # If we find multiple names, assume that they are all affected
            if len(names) > 1:
                for name in names:
                    sh = mind.get_stakeholder_by_name(tracker.sender_id, name)
                    if not sh == None:
                        aff_stkhs.append(sh['name'])
                if len(aff_stkhs) > 1:
                    events.append(SlotSet('name', 'them'))
            # else take a single name, if it is unknown try a potentially found stakeholder
            else:
                sh = mind.get_stakeholder_by_name(tracker.sender_id, names[0])
                if not sh == None:
                    aff_stkhs.append(sh['name'])
                else:
                    sh = mind.get_stakeholder_by_name(tracker.sender_id, next(tracker.get_latest_entity_values('stakeholder'), None))
                    if not sh == None:
                        aff_stkhs.append(sh['name'])
                        events.append(SlotSet('name', sh['name']))

            if len(aff_stkhs) > 0:
                consequence = Consequence({
                    "option": option.doc_id, 
                    "affected_stakeholders": aff_stkhs, 
                    "impact": impact,
                    "probability": 1
                }).memorize(tracker.sender_id)

                action_return = True
            else:
                # If we do not find a distinct name, let the user choose from possible stakeholders
                events.append(SlotSet('name', None))
                action_return = False
        except (AttributeError, TypeError, KeyError, IndexError) as e:
            logger.warning('Exception creating consequence: ' + str(e))
            events.append(SlotSet('name', None))
            action_return = False
            
        events.append(SlotSet('action_return', action_return))
        return events


class UpdateConsequence(Action):
    """
    Update an existing consequence

    Triggered by:
    * Intent 'positive'
    * Intent 'negative'
    * Intent 'correct'
    * Intent 'wrong'
    * Intent 'quantity' (user specified the impact weight OR the probability)

    Required slots: /

    Returns:
    * action_return = True if consequence was updated
    * action_return = False if no update was made
    """
    def name(self):
        return 'action_update_consequence'

    def run(self, dispatcher, tracker, domain):
        action_return = False
        intent = tracker.latest_message['intent'].get('name')

        try:
            consequence = mind.get_recent_consequence(tracker.sender_id)
            old_impact = consequence['impact']

            # Update impact
            if (intent == 'positive'):
                consequence['impact'] = 1

            elif (intent == 'negative'):
                consequence['impact'] = -1

            elif (intent == 'wrong'):
                consequence['impact'] = consequence['impact'] * -1
                
            elif (intent == 'quantity'):
                sources = list(tracker.get_latest_entity_values('quantity'))
                sources.append(tracker.latest_message['text'])
                quantity = nlu.get_quantity_from_sources(sources)

                if quantity != -1:
                    # If impact is still 1 or -1, we set this value first
                    if (consequence['impact'] == 1 or consequence['impact'] == -1):
                        # Store 1.1 as impact if the user provides 1 so that the update can be recognized
                        if quantity == 1: quantity = 1.1    
                        consequence['impact'] = consequence['impact'] * quantity
                    # Else it is asked for the probability
                    else:
                        consequence['probability'] = float(quantity / 100)
                        # Correct the 1.1 value if necessary because we don't need it as an indicator for the update anymore
                        if consequence['impact'] == 1.1: consequence['impact'] = 1
                        if consequence['impact'] == -1.1: consequence['impact'] = -1
                            

            if (consequence['impact'] != old_impact or consequence['probability'] != 1):
                consequence.memorize(tracker.sender_id)
                dispatcher.utter_template('utter_got_it', tracker)
                action_return = True
        except (AttributeError, TypeError) as e:
            logger.warning('Exception updating consequence: ' + str(e))
            action_return = False
            dispatcher.utter_template('utter_not_sure', tracker)

        return [SlotSet("action_return", action_return)]

#########################
#                       #
#        HELPER         #
#                       #
#########################
class CheckIdentifiedName(Action):
    """
    Check if an identified name is already assigned to a stakeholder
    
    Returns:
    * action_return = True if the identified name is already in use
    * action_return = False if the name is still unassigned
    """
    def name(self):
        return 'action_check_identified_name'
        
    def run(self, dispatcher, tracker, domain):
        action_return = False
        name = tracker.get_slot('name')
        if not name == None:
            if not mind.get_stakeholder_by_name(tracker.sender_id, name) == None:
                action_return = True
        else:
            # If no name was identified, it is better to initiate a question for the actual name
            action_return = True

        return [SlotSet("action_return", action_return)]

class HandleSmalltalk(Action):
    """
    Provide an appropriate reaction to smalltalk independently of the current dialogue context!
    That means:
    1. Use Mapping Policy
    2. Rewind after utterance in order to avoid creating an unknown storyline
    
    Returns:
    * UserUtteranceReverted() - do not disturb the current story!
    """
    def name(self):
        return 'action_handle_smalltalk'
        
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_smalltalk_1", tracker)
        dispatcher.utter_template("utter_smalltalk_2", tracker)
        
        dispatcher.utter_message(tracker.events[-3].get('text'))
        
        return [UserUtteranceReverted()] 

class ActionRestart(Action):
    """
    Restart dialogue on user request
    """
    def name(self):
        return 'action_restart'

    def run(self, dispatcher, tracker, domain):
        mind.amnesia(tracker.sender_id)
        return [Restarted(), UserUttered('/greeting'), FollowupAction("action_intro")]
       

class ActionDefaultAskAffirmation(Action):
    """Asks for an affirmation of the intent if NLU threshold is not met."""

    def name(self) -> Text:
        return "action_default_ask_affirmation"

    def __init__(self) -> None:
        self.ignored_intents = ['deny', 'affirm', 'neutral', 'moralstatus', 'dontknow', 'greeting', 'correct', 'wrong', 
                                'utilitarism', 'deontology', 'moralquestion', 'goodbye', 'thanks', 'smalltalk']

        import csv

        self.intent_mappings = {}
        with open('data/intent_description_mapping.csv',
                  newline='',
                  encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                self.intent_mappings[row[0]] = row[1]

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
            ) -> List['Event']:

        intent_ranking = tracker.latest_message.get('intent_ranking', [])
        first_intent_names = [intent.get('name', '')
                              for intent in intent_ranking
                              if not intent.get('name', '') in self.ignored_intents]

        if len(first_intent_names) > 0:
            message_title = "Sorry, I'm not sure I've understood " \
                            "you correctly. Do you want to..."

            mapped_intents = [(name, self.intent_mappings.get(name, name))
                              for name in first_intent_names]

            entities = tracker.latest_message.get("entities", [])
            entities = {e["entity"]: e["value"] for e in entities}
            entities_json = json.dumps(entities)

            buttons = []
            for intent in mapped_intents:
                buttons.append({'title': intent[1],
                                'payload': '/{}{}'.format(intent[0], entities_json)})

            buttons.append({'title': 'Something else',
                            'payload': '/deny'})

            dispatcher.utter_button_message(message_title, buttons=buttons)
        else:
            return [FollowupAction("action_default_ask_rephrase")]

#########################
#                       #
#        BUTTONS        #
#                       #
#########################
class ChooseDecider(Action):
    """
    Choose stakeholder who makes the moral decision
    """
    def name(self):
        return 'action_choose_decider'
        
    def run(self, dispatcher, tracker, domain):
        message = "Out of these persons, whose moral decision do you want to analyse?"  # On request (Google table entry #5)
        buttons = []

        
        for sh in mind.get_stakeholders(tracker.sender_id):
            try:
                buttons.append({ 'title': sh['name'], 'payload': '/decider{"name": "' + sh['name'] + '"}'})
            except (KeyError, AttributeError):
                logger.warning('Exception creating buttons for stakeholders, it appears that some stakeholder does not have a name')
                dispatcher.utter_template('utter_not_sure', tracker)
        buttons.append({ "title": "Some other person", "payload": '/decider' })
        dispatcher.utter_button_message(message, buttons)

        return []


class ChooseAffectedStakeholder(Action):
    """
    Choose stakeholder who is affected by a consequence
    """
    def name(self):
        return 'action_choose_affected_stakeholder'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_reflect_choose_affected_stakeholder', tracker)

        buttons = []
        message = "On which person would this decision have an impact?"
        
        for sh in mind.get_stakeholders(tracker.sender_id):
            try:
                buttons.append({ 'title': sh['name'], 'payload': '/consequence{"name": "' + sh['name'] + '"}'})
            except (KeyError, AttributeError):
                logger.warning('Exception creating buttons for stakeholders, it appears that some stakeholder does not have a name')
                dispatcher.utter_template('utter_not_sure', tracker)
        dispatcher.utter_button_message(message, buttons)
        return []


#########################
#                       #
#      EVALUATION       #
#                       #
#########################
class EvaluationUtilitarism(Action):
    """
    Evaluate the gathered information using utilitarism ethics principle
    """
    def name(self):
        return 'action_evaluation_utilitarism'

    def run(self, dispatcher, tracker, domain):
        events = []

        data = mind.get_full_model(tracker.sender_id)
        r = requests.post(const.API_UTILITARISM, json=data)

        if r.status_code == 200:
            response = r.json()
            action_return = True
            message = {
                "text": 'I have prepared a decision table that lists the utilitarian scores I calculated from your input:', 
                "attachment": response['url'],
                "image": response['url']
            }
            dispatcher.messages.append(message)
        else:
            dispatcher.utter_template('utter_evaluation_failure', tracker)
            action_return = False

        events.append(SlotSet('action_return', action_return))
        return events


class EvaluationDeontology(Action):
    """
    Evaluate the gathered information using deontology ethics principle
    """
    def name(self):
        return 'action_evaluation_deontology'

    def run(self, dispatcher, tracker, domain):
        events = []

        data = mind.get_full_model(tracker.sender_id)
        r = requests.post(const.API_DEONTOLOGY, json=data)

        if r.status_code == 200:
            response = r.json()
            action_return = True
            message = {
                "text": 'I have derived a decision tree from the various options you have mentioned to me and made a deontological assessment of each action:', 
                "attachment": response['url'],
                "image": response['url']
            }
            dispatcher.messages.append(message)
        else:
            dispatcher.utter_template('utter_evaluation_failure', tracker)
            action_return = False

        events.append(SlotSet('action_return', action_return))
        return events
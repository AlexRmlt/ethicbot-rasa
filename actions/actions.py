# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests, json
from typing import Dict, Text, Any, List, Union
from rasa_core_sdk import Tracker
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.forms import FormAction

import modules.constants as const
import modules.nlu_helper as nlu

import modules.datamodel.mind as mind
from modules.datamodel import Stakeholder, Option, Consequence, Deed, Context

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(message)s', filename='rasa.log', level=logging.DEBUG)


class Intro(Action):
	""" 
	Initial Action to be executed
	
	Triggered by: (TODO: map to greeting)
	* Intent 'greeting'

	Required slots: /

	Returns: /
	"""
	def name(self):
		return "action_intro"

	def run(self, dispatcher, tracker, domain):
		dispatcher.utter_template('utter_intro', tracker)
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
#						#
#	   STAKEHOLDER 		#
#						#
#########################
class CreateStakeholder(Action):
	"""
	Create a new stakeholder and write it to the datamodel

	Triggered by:
	* Intent 'stakeholder'
	* Intent 'decider'

	Required slots:
	* plural == singular or plural of stakeholder to be created
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
			'moral_status_weight': 1
		})

		# Do we know whether it is a single stakeholder or a group of people?
		if (tracker.get_slot('plural') == const.SINGULAR):
			sh['amount'] = 1
		else:
			sources = [ next(tracker.get_latest_entity_values('stakeholder'), None),
						next(tracker.get_latest_entity_values('quantity'), -1) ]
			quantity = nlu.get_quantity_from_sources(sources)
			sh['amount'] = int(quantity)

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

		events.append(SlotSet("amount_stakeholders", mind.get_amount_stakeholders(tracker.sender_id)))
		events.append(SlotSet("action_return", sh['amount'] != -1))

		return events


class UpdateStakeholder(Action):
	"""
	Update an existing stakeholder

	Triggered by:
	* Intent 'quantity'		(user specified the amount of stakeholders OR the moral status weight, hopefully between 1 and 10)
	* Intent 'decider'
	* Intent 'name'
	* Intent 'correct' 		(user confirmed name recognized by the bot)
	* Intent 'wrong' 		(user rejected name recognized by the bot)
	* Intent 'dontknow'		(user does not know the proposed stakeholders name)
	* Intent 'deny'			(user does not tell the proposed stakeholders name)
	* Intent 'moralstatus'	

	Required slots: /

	Returns:
	* action_return = True if stakeholder was successfully updated
	* action_return = False if no update was made
	* decider = name of the stakeholder if he is the decider
	* name = name of the stakeholder if it was freshly assigned
	* plural = specific_plural if amount was detected or None if detection failed
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
				# Plural slot must be set to 'unspecific_plural', else we would not ask
				# If detection of stakeholder amount failed, plural slot is set to None
				# Thus: if the slot is still set to 'unspecific_plural', we are asking for the amount
				if tracker.get_slot('plural') == const.UNSPECIFIC_PLURAL:
					sources = [ next(tracker.get_latest_entity_values('quantity'), -1),
								next(tracker.get_latest_entity_values('stakeholder'), None),
								tracker.latest_message['text'] ]
					quantity = nlu.get_quantity_from_sources(sources)

					if quantity != -1:		
						sh['amount'] = quantity
						mind.memorize(tracker.sender_id, sh)
						action_return = True

						if quantity > 1:
							dispatcher.utter_message('I see, {} are involved.'.format(sh['amount']))
							events.append(SlotSet('plural', const.SPECIFIC_PLURAL))
						else:
							dispatcher.utter_message('Okay, so its only one single person. Got that wrong at first.')
							events.append(SlotSet('plural', const.SINGULAR))
					else:
						logging.warning('Could not determine amount of stakeholders in message classified as quantity')
						action_return = False
						events.append(SlotSet('plural', None))
					
				# Else we asked for the moral status
				else:
					sources = [ next(tracker.get_latest_entity_values('quantity'), -1),
								tracker.latest_message['text'] ]
					weight = nlu.get_quantity_from_sources(sources)
					
					sh.set_moral_status_weight(weight).memorize(tracker.sender_id)
					dispatcher.utter_message('Okay, I will consider the moral status of {} to be a proportion of {} compared to a human.'.format(sh['name'], sh['moral_status_weight']))
					action_return = True

			# Intent: name or correct
			elif (tracker.latest_message['intent'].get('name') == 'name') \
				or (tracker.latest_message['intent'].get('name') == 'correct'):

				if tracker.latest_message['intent'].get('name') == 'correct':
					name = tracker.get_slot('name')
				else:
					name = next(tracker.get_latest_entity_values('name'), None)
					if name == None:
						name = next(tracker.get_latest_entity_values('stakeholder'), None)

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
			logging.warning('Exception updating Stakeholder: ' + str(e))
			events.append(SlotSet('name', None))
			action_return = False

		events.append(SlotSet('action_return', action_return))
		return events


#########################
#						#
#	     OPTION 		#
#						#
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
	* option = ID of the created option
	* deeds = list of possible deeds associated with the option to be commented by the user
	"""
	def name(self):
		return 'action_create_option'

	def run(self, dispatcher, tracker, domain):
		deeds = list(tracker.get_latest_entity_values('deed'))
		opt = Option({"deeds": deeds})
		option_id = opt.memorize(tracker.sender_id).doc_id

		if len(deeds) > 0:
			current_deed = deeds[0]
		else:
			current_deed = None

		return [SlotSet("deed", current_deed), SlotSet("option", option_id), SlotSet("action_return", True)]


class UpdateOption(Action):
	"""
	Update an existing Option

	Triggered by:
	* Intent 'wrong' after 'utter_ask_deed'

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
			option = mind.by_id(tracker.sender_id, int(tracker.get_slot('option')))

			if (tracker.latest_message['intent'].get('name') == 'wrong'):
				option['deeds'].remove(tracker.get_slot('deed'))
				option.memorize(tracker.sender_id)

				if len(option['deeds']) > 0:
					current_deed = option['deeds'][0]
				else:
					current_deed = None
					del option['deeds']

				action_return = True
				events.append(SlotSet("deed", current_deed))
				dispatcher.utter_template('utter_got_it', tracker)
		except (AttributeError, TypeError) as e:
			logging.warning('Exception updating Option: ' + str(e))
			action_return = False
			dispatcher.utter_template('utter_not_sure', tracker)

		events.append(SlotSet("action_return", action_return))
		return events


#########################
#						#
#	  	  DEED 			#
#						#
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
			deed = Deed({"label": label, "option": tracker.get_slot('option')}).memorize(tracker.sender_id)
			action_return = True
		else:
			dispatcher.utter_template('utter_not_sure', tracker)

		events.append(SlotSet('action_return', action_return))
		return events


class UpdateDeed(Action):
	"""
	Update an existing Deed

	Triggered by:
	* Intent 'correct' after 'utter_ask_universalizable'
	* Intent 'wrong' after 'utter_ask_universalizable'
	* Intent 'affirm' after 'utter_ask_inherent_evil'
	* Intent 'deny' after 'utter_ask_inherent_evil'

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
				deed['inherent_evil'] = False
				action_return = True
			
			if action_return == True:
				deed.memorize(tracker.sender_id)
				dispatcher.utter_template('utter_got_it', tracker)

			# Remove current and select next deed from list, if available
			if ('universalizable' in deed and 'inherent_evil' in deed):
				option = mind.by_id(tracker.sender_id, int(tracker.get_slot('option')))

				if deed['label'] in option['deeds']:
					option['deeds'].remove(deed['label'])
					option.memorize(tracker.sender_id)

				if len(option['deeds']) > 0:
					events.append(SlotSet("deed", option['deeds'][0]))
				else:
					events.append(SlotSet("deed", None))
					del option['deeds']

		except (AttributeError, TypeError) as e:
			logging.warning('Exception updating deed: ' + str(e))
			action_return = False
			dispatcher.utter_template('utter_not_sure', tracker)

		events.append(SlotSet("action_return", action_return))
		return events

#########################
#						#
#	  CONSEQUENCE		#
#						#
#########################
class CreateConsequence(Action):
	"""
	Create a consequence of an option

	Triggered by:
	* Intent 'consequence'

	Required slots:
	* option == the ID of the option the user is currently talking about
	* sentiment == sentiment of the last sentence (pos/neu/neg)

	Returns:
	* action_return = True if consequence was created with correct impact
	* action_return = False if consequence was created with unknown impact (0)
	"""
	def name(self):
		return 'action_create_consequence'

	def run(self, dispatcher, tracker, domain):
		events = []
		action_return = False
		option = int(tracker.get_slot('option'))

		if tracker.get_slot('sentiment') == 'pos':
			impact = 1
		elif tracker.get_slot('sentiment') == 'neg':
			impact = -1
		else:
			impact = 0

		# Find out, which stakeholder is affected by this consequence
		sh = mind.get_stakeholder_by_name(tracker.sender_id, next(tracker.get_latest_entity_values('name'), None))
		if sh == None:
			sh = mind.get_stakeholder_by_name(tracker.sender_id, next(tracker.get_latest_entity_values('stakeholder'), None))

		try:
			consequence = Consequence({
				"option": option, 
				"affected_stakeholder": sh['name'], 
				"impact": impact,
				"probability": 1
			}).memorize(tracker.sender_id)
			
			action_return = True
		except (AttributeError, TypeError) as e:
			logging.warning('Exception creating consequence: ' + str(e))
			# If we do not find a distinct name, let the user choose from possible stakeholders
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
			consequence = mind.get_consequence(tracker.sender_id, tracker.get_slot('name'), tracker.get_slot('option'))
			old_impact = consequence['impact']

			# Update impact
			if (intent == 'positive'):
				consequence['impact'] = 1

			elif (intent == 'negative'):
				consequence['impact'] = -1

			elif (intent == 'wrong'):
				consequence['impact'] = consequence['impact'] * -1
				
			elif (intent == 'quantity'):
				sources = [ next(tracker.get_latest_entity_values('quantity'), -1),
							tracker.latest_message['text'] ]
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
			logging.warning('Exception updating consequence: ' + str(e))
			action_return = False
			dispatcher.utter_template('utter_not_sure', tracker)

		return [SlotSet("action_return", action_return)]


#########################
#						#
#	  	 BUTTONS		#
#						#
#########################
class ChooseDecider(Action):
	"""
	Choose stakeholder who makes the moral decision
	"""
	def name(self):
		return 'action_choose_decider'
		
	def run(self, dispatcher, tracker, domain):
		message = "Out of this persons, who is the one to make the moral decision?"
		buttons = []

		for sh in mind.get_stakeholders(tracker.sender_id):
			buttons.append({ 'title': sh['name'], 'payload': '/decider{"name": "' + sh['name'] + '"}'})

		buttons.append({ "title": "Some other person", "payload": '/decider{"plural": "' + const.SINGULAR + '"}' })
		buttons.append({ "title": "Some other group of people", "payload": '/decider{"plural": "' + const.UNSPECIFIC_PLURAL + '"}' })
		dispatcher.utter_button_message(message, buttons)

		return []


class ChooseAffectedStakeholder(Action):
	"""
	Choose stakeholder who is affected by a consequence
	"""
	def name(self):
		return 'action_choose_affected_stakeholder'

	def run(self, dispatcher, tracker, domain):
		buttons = []
		message = "On which person would this decision have an impact?"

		for sh in mind.get_stakeholders(tracker.sender_id):
			buttons.append({ 'title': sh['name'], 'payload': '/consequence{"name": "' + sh['name'] + '"}'})
		dispatcher.utter_button_message(message, buttons)
		return []


#########################
#						#
#	   EVALUATION 		#
#						#
#########################
class EvaluationUtilitarism(Action):
	"""
	Evaluate the gathered information using utilitarism ethics principle
	(TODO: map to intent 'utilitarism')
	"""
	def name(self):
		return 'action_evaluation_utilitarism'

	def run(self, dispatcher, tracker, domain):
		data = mind.get_full_model(tracker.sender_id)
		r = requests.post(const.API_UTILITARISM, json=data)

		if r.status_code == 200:
			dispatcher.utter_message(r.text)
		else:
			dispatcher.utter_template('utter_evaluation_failure', tracker)


class EvaluationDeontology(Action):
	"""
	Evaluate the gathered information using deontology ethics principle
	(TODO: map to intent 'deontology')
	"""
	def name(self):
		return 'action_evaluation_deontology'

	def run(self, dispatcher, tracker, domain):
		data = mind.get_full_model(tracker.sender_id)
		r = requests.post(const.API_DEONTOLOGY, json=data)

		if r.status_code == 200:
			dispatcher.utter_message(r.text)
		else:
			dispatcher.utter_template('utter_evaluation_failure', tracker)


###############################################################################
##################### --- DO NOT CALL FROM RASA --- ###########################
###############################################################################
class GetDataModel(Action):
	"""
	Retrieve datamodel for a distinct sender
	"""
	def name(self):
		return 'getdatamodel'

	def run(self, dispatcher, tracker, domain):
		data = mind.get_full_model(tracker.sender_id)
		return data

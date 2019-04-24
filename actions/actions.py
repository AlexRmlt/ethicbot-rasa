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
		mind.amnesia()
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
			context = mind.get_context_singleton()
			context['moralquestion'] = tracker.latest_message['text']
			context.memorize()
			
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
	* stakeholder == synonym the user used to introduce the stakeholder

	Returns:
	* action_return = True if stakeholder was created with correct amount
	* action_return = False if stakeholder was created with unspecific amount (-1)
	* amount_stakeholders = amount of stakeholders in the datamodel after inserting the new one
	* name = the inserted stakeholders name
	* decider = name of the inserted stakeholder, if he is the decider
	"""
	def name(self):
		return "action_create_stakeholder"

	def run(self, dispatcher, tracker, domain):
		events = []

		# Do we know whether it is a single stakeholder or a group of people?
		if (tracker.get_slot('plural') == const.SINGULAR):
			sh = Stakeholder({"decider": False, "amount": 1})
		else:
			sources = [ next(tracker.get_latest_entity_values('stakeholder'), None),
						next(tracker.get_latest_entity_values('quantity'), -1) ]
			quantity = nlu.get_quantity_from_sources(sources)
			sh = Stakeholder({"decider": False, "amount": int(quantity)})

		# Is the stakeholder recognized as the decider?
		if (tracker.latest_message['intent'].get('name') == 'decider'):
			events.append(SlotSet("decider", sh['name']))
			sh['decider'] = True

		# Remember synonym, maybe the user refuses to call the person by its new name
		sh['synonym'] = next(tracker.get_latest_entity_values('stakeholder'), None)

		sh.memorize() 

		events.append(SlotSet("name", sh['name']))
		events.append(SlotSet("amount_stakeholders", mind.get_amount_stakeholders()))
		events.append(SlotSet("action_return", sh['amount'] != -1))

		dispatcher.utter_message('Alright, from now on I will use the name "{}"!'.format(sh['name']))
		return events


class UpdateStakeholder(Action):
	"""
	Update an existing stakeholder

	Triggered by:
	* Intent 'quantity'
	* Intent 'decider'

	Required slots:
	* name == stakeholder to be updated

	Returns:
	* action_return = True if stakeholder was successfully updated
	* action_return = False if no update was made
	* decider = name of the stakeholder if he is the decider
	"""
	def name(self):
		return "action_update_stakeholder"

	def run(self, dispatcher, tracker, domain):
		events = []
		sh = mind.get_stakeholder_by_name(tracker.get_slot('name'))
		action_return = False

		try:
			if (tracker.latest_message['intent'].get('name') == 'decider'):
				sh['decider'] = True		
				events.append(SlotSet('decider', sh['name']))
				action_return = True
				mind.memorize(sh)
				dispatcher.utter_template('utter_got_it', tracker)
			elif (tracker.latest_message['intent'].get('name') == 'quantity'):
				sources = [ next(tracker.get_latest_entity_values('quantity'), -1),
							next(tracker.get_latest_entity_values('stakeholder'), None),
							tracker.latest_message['text'] ]
				quantity = nlu.get_quantity_from_sources(sources)

				if quantity != -1:
					sh['amount'] = quantity
					action_return = True
					mind.memorize(sh)
					dispatcher.utter_template('utter_got_it', tracker)
				else:
					action_return = False
		except (AttributeError, TypeError):
			events.append(SlotSet('name', None))
			action_return = False

		events.append(SlotSet("action_return", action_return))
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
		option_id = opt.memorize().doc_id

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
			option = mind.by_id(int(tracker.get_slot('option')))

			if (tracker.latest_message['intent'].get('name') == 'wrong'):
				option['deeds'].remove(tracker.get_slot('deed'))
				option.memorize()

				if len(option['deeds']) > 0:
					current_deed = option['deeds'][0]
				else:
					current_deed = None
					del option['deeds']

				action_return = True
				events.append(SlotSet("deed", current_deed))
				dispatcher.utter_template('utter_got_it', tracker)
		except (AttributeError, TypeError):
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
			deed = Deed({"label": label, "option": tracker.get_slot('option')}).memorize()
			action_return = True
		else:
			dispatcher.utter_template('utter_not_sure', tracker)

		events.append(SlotSet('action_return', action_return))
		return events


class UpdateDeed(Action):
	"""
	Update an existing Deed

	Triggered by:
	* 

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
			deed = mind.get_deed(tracker.get_slot('deed'))

			# Update universalizability
			if (tracker.latest_message['intent'].get('name') == 'correct'):
				deed['universalizable'] = True
			elif (tracker.latest_message['intent'].get('name') == 'wrong'):
				deed['universalizable'] = False

			if ('universalizable' in deed):
				deed.memorize()
				action_return = True
				dispatcher.utter_template('utter_got_it', tracker)

			# Remove current and select next deed from list, if available
			option = mind.by_id(int(tracker.get_slot('option')))

			if deed['label'] in option['deeds']:
				option['deeds'].remove(deed['label'])
				option.memorize()

			if len(option['deeds']) > 0:
				events.append(SlotSet("deed", option['deeds'][0]))
			else:
				events.append(SlotSet("deed", None))
				del option['deeds']

		except (AttributeError, TypeError):
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
		sh = mind.get_stakeholder_by_name(tracker.get_slot('name'))

		try:
			consequence = Consequence({"option": option, "affected_stakeholder": sh['name'], "impact": impact}).memorize()
			if impact != 0:
				action_return = True
		except (AttributeError, TypeError):
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
	* Intent 'quantity'

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
			consequence = mind.get_consequence(tracker.get_slot('name'), tracker.get_slot('option'))
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
					consequence['impact'] = consequence['impact'] * quantity

			if consequence['impact'] != old_impact:
				consequence.memorize()
				dispatcher.utter_template('utter_got_it', tracker)
				action_return = True
		except (AttributeError, TypeError):
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

		for sh in mind.get_stakeholders():
			buttons.append({ 'title': sh['name'], 'payload': '/decider{"name": "' + sh['name'] + '"}'})

		buttons.append({ "title": "Somebody else", "payload": '/decider{"plural": "' + const.SINGULAR + '"}' })
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

		for sh in mind.get_stakeholders():
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
	"""
	def name(self):
		return 'action_evaluation_utilitarism'

	def run(self, dispatcher, tracker, domain):
		data = mind.get_full_model()
		r = requests.post(const.API_UTILITARISM, json=data)

		if r.status_code == 200:
			dispatcher.utter_message(r.text)
		else:
			dispatcher.utter_template('utter_evaluation_failure', tracker)


class EvaluationDeontology(Action):
	"""
	Evaluate the gathered information using deontology ethics principle
	"""
	def name(self):
		return 'action_evaluation_deontology'

	def run(self, dispatcher, tracker, domain):
		data = mind.get_full_model()
		r = requests.post(const.API_DEONTOLOGY, json=data)

		if r.status_code == 200:
			dispatcher.utter_message(r.text)
		else:
			dispatcher.utter_template('utter_evaluation_failure', tracker)
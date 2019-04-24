from . import *

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
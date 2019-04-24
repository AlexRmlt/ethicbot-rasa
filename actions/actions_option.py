from . import *

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
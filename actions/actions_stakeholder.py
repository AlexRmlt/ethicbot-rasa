from . import *

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
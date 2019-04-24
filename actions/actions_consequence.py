from . import *

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
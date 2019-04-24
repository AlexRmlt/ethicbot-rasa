from . import *

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
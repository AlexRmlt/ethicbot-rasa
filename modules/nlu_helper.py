import spacy
import modules.constants as const
import inflect
from word2number import w2n

inf = inflect.engine()
nlp = spacy.load('en_core_web_md')

def get_quantity_from_sources(sources):
	"""
	Return the quantity that is found first in the list of sources
	The list has to be passed with prioritized elements
	"""
	for s in sources:
		q = get_quantity(s)
		if q != -1:
			return q
	return -1

def get_quantity(entity):
	doc = nlp(str(entity))
	for token in doc:
		try:
			return w2n.word_to_num(token.text)
		except ValueError:
			pass
	return -1

def get_associated_verbs(message):
	"""
	- DEPRECATED -
	Identify verbs in the message which could be associated with actions
	"""
	verbs = []
	doc = nlp(message)

	for token in doc:
   		if token.pos_ == 'VERB' and not token.is_stop:
   			verbs.append(token.lemma_)
	return verbs
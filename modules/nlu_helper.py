import spacy
import modules.constants as const
import inflect
from word2number import w2n
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Init NLP libraries
inf = inflect.engine()
nlp = spacy.load('en_core_web_md')
sid = SentimentIntensityAnalyzer()

def get_sentiment(msg):
	res = sid.polarity_scores(msg)
	return max(res.items(), key=lambda x: x[1])

def get_plural(text, ent=None):
	# Are there words in the message indicating plural?
	assumed_plural = False
	with open('modules/wordlists/plural.txt') as file:
		plw = file.read().split(' ')
		if any(w in text.lower() for w in plw):
			assumed_plural = True

	# Is there a quantity indicating plural?
	quantity = get_quantity(ent)

	if not assumed_plural and not quantity > 1:
		return const.SINGULAR
	else:
		if quantity > 1:
			return const.SPECIFIC_PLURAL
		else:
			return const.UNSPECIFIC_PLURAL

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
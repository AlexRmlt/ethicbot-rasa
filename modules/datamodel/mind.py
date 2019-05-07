from tinydb import TinyDB, Query
import importlib
import re
from operator import attrgetter


db = TinyDB('db.json')
q = Query()

def memorize(obj):
	obj['type'] = obj.__class__.__name__

	try:
		return db.update(obj, doc_ids=[obj.doc_id])[0] if obj.doc_id != -1 else db.insert(obj)
	except AttributeError:
		return db.insert(obj)

def amnesia():
	db.purge()

def get_full_model():
	data = db.all()
	for ent in data:
		ent['id'] = ent.doc_id

	return data

def get_context_singleton():
	from . import Context
	context = db.get(q.type == 'Context')
	if context == None:
		context = Context({}).memorize()

	return context

def by_id(i):
	doc = db.get(doc_id=i)
	try:
		module = importlib.import_module('modules.datamodel')
		class_ = getattr(module, doc['type'])
	except KeyError:
		raise
	return class_(doc)

def get_stakeholders():
	from . import Stakeholder
	stakeholders = []
	for sh in db.search(q.type == 'Stakeholder'):
		stakeholders.append(Stakeholder(sh))
	return stakeholders

def get_amount_stakeholders():
	return db.count(q.type == 'Stakeholder')

def stakeholder_exists(name):
	return db.contains(q.name == name)

def get_stakeholder_by_name(name):
	from . import Stakeholder
	sh = db.get(q.name.matches(name, flags=re.IGNORECASE))
	return Stakeholder(sh) if sh != None else None

def get_recent_stakeholder():
	from . import Stakeholder
	try:
		sh = db.search(q.type == 'Stakeholder')[-1]
	except IndexError:
		return None
	return Stakeholder(sh) if sh != None else None

def get_stakeholders_by_synonym(synonym):
	from . import Stakeholder
	stakeholders = []
	for sh in db.search(q.synonym.matches(synonym, flags=re.IGNORECASE)):
		stakeholders.append(Stakeholder(sh))
	return stakeholders

def get_deed(label):
	from . import Deed
	d = db.get(q.label.matches(label, flags=re.IGNORECASE))
	return Deed(d) if d != None else None

def get_consequence(stakeholder, option):
	from . import Consequence
	cons = db.get((q.affected_stakeholder.matches(stakeholder, flags=re.IGNORECASE)) \
		& (q.option == option))
	return Consequence(cons) if cons != None else None

def get_decider():
	from . import Stakeholder
	decider = db.get(q.decider == True)
	return Stakeholder(decider) if decider != None else None
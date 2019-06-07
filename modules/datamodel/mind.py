from tinydb import TinyDB, Query
import importlib
import re
from operator import attrgetter


db = TinyDB('db.json')
q = Query()


def memorize(s_id, obj):
	obj['type'] = obj.__class__.__name__

	try:
		return current(s_id).update(obj, doc_ids=[obj.doc_id])[0] if obj.doc_id != -1 else current(s_id).insert(obj)
	except AttributeError:
		return current(s_id).insert(obj)

def current(s_id):
	return db.table(s_id)

def amnesia(s_id):
	db.purge_table(s_id)

def get_full_model(s_id):
	data = current(s_id).all()
	for ent in data:
		ent['id'] = ent.doc_id

	return data

def get_context_singleton(s_id):
	from . import Context
	context = current(s_id).get(q.type == 'Context')
	if context == None:
		context = Context({}).memorize()

	return context

def by_id(s_id, i):
	doc = current(s_id).get(doc_id=i)
	try:
		module = importlib.import_module('modules.datamodel')
		class_ = getattr(module, doc['type'])
	except KeyError:
		raise
	return class_(doc)

def get_stakeholders(s_id):
	from . import Stakeholder
	stakeholders = []
	for sh in current(s_id).search(q.type == 'Stakeholder'):
		stakeholders.append(Stakeholder(sh))
	return stakeholders

def get_num_stakeholders(s_id):
	return current(s_id).count(q.type == 'Stakeholder')

def get_num_options(s_id):
	return current(s_id).count(q.type == 'Option')

def stakeholder_exists(s_id, name):
	return current(s_id).contains(q.name == name)

def get_stakeholder_by_name(s_id, name):
	from . import Stakeholder
	try:
		sh = current(s_id).get(q.name.matches(name, flags=re.IGNORECASE))

		if sh == None and name.lower().startswith('the'):
			sh = current(s_id).get(q.name.matches(name.split(' ')[1], flags=re.IGNORECASE))
	except (TypeError, AttributeError):
		return None
	return Stakeholder(sh) if sh != None else None

def get_recent_stakeholder(s_id):
	from . import Stakeholder
	try:
		sh = current(s_id).search(q.type == 'Stakeholder')[-1]
	except IndexError:
		return None
	return Stakeholder(sh) if sh != None else None

def get_recent_consequence(s_id):
	from . import Consequence
	try:
		cons = current(s_id).search(q.type == 'Consequence')[-1]
	except IndexError:
		return None
	return Consequence(cons) if cons != None else None

def get_recent_option(s_id):
	from . import Option
	try:
		opt = current(s_id).search(q.type == 'Option')[-1]
	except IndexError:
		return None
	return Option(opt) if opt != None else None

def get_recent_deed(s_id):
	from . import Deed
	try:
		deed = current(s_id).search(q.type == 'Deed')[-1]
	except IndexError:
		return None
	return Deed(deed) if deed != None else None

def get_stakeholders_by_synonym(s_id, synonym):
	from . import Stakeholder
	stakeholders = []
	for sh in current(s_id).search(q.synonym.matches(synonym, flags=re.IGNORECASE)):
		stakeholders.append(Stakeholder(sh))
	return stakeholders

def get_deed(s_id, label):
	from . import Deed
	d = current(s_id).get((q.label.matches(label, flags=re.IGNORECASE)) \
		& (q.type == 'Deed'))
	return Deed(d) if d != None else None

def get_consequence(s_id, stakeholder, option):
	from . import Consequence
	cons = current(s_id).get((q.affected_stakeholder.matches(stakeholder, flags=re.IGNORECASE)) \
		& (q.option == option))
	return Consequence(cons) if cons != None else None

def get_decider(s_id):
	from . import Stakeholder
	decider = current(s_id).get(q.decider == True)
	return Stakeholder(decider) if decider != None else None
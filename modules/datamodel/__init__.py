from . import mind
import random

aliases = ['Amelie', 'Benjamin', 'Carla', 'Daniel', 'Esther', 'Frank', 'Greta', 'Harald', 'Inga', 'Jörg',
			'Katharina', 'Lars', 'Michelle', 'Nathan', 'Olga', 'Patrick', 'Roswitha', 'Samuel', 'Tanja', 'Uwe', 'Viola', 'Werner', 'Zoe']

collective = ['the Saxons', 'the Rhinelanders', 'the Palatines', 'the Bavarians', 'the Swabians', 'the Hessians']

class Stakeholder(dict):
	def __init__(self,*arg,**kw):
		super(Stakeholder, self).__init__(*arg, **kw)

		try:
			self.doc_id = arg[0].doc_id
		except AttributeError:
			self.doc_id = -1
		try:
			if not 'name' in self:
				if self['amount'] == 1:
					name = random.choice(aliases) 
					while (mind.stakeholder_exists(name)):
						name = random.choice(aliases)
				else:
					name = random.choice(collective) 
					while (mind.stakeholder_exists(name)):
						name = random.choice(collective)
				self['name'] = name
		except KeyError:
			self['amount'] = -1
			name = random.choice(collective) 
			while (mind.stakeholder_exists(name)):
				name = random.choice(collective)
	
	def memorize(self):
		self.doc_id = mind.memorize(self)
		return self

class Option(dict):
	def __init__(self,*arg,**kw):
		super(Option, self).__init__(*arg, **kw)

		try:
			self.doc_id = arg[0].doc_id
		except AttributeError:
			self.doc_id = -1

	def memorize(self):
		self.doc_id = mind.memorize(self)
		return self

	def add_consequence(self, consequence):
		try:
			self['consequences'].append(consequence.doc_id)
		except KeyError:
			self['consequences'] = [consequence.doc_id]
		return self

class Consequence(dict):
	def __init__(self,*arg,**kw):
		super(Consequence, self).__init__(*arg, **kw)

		try:
			self.doc_id = arg[0].doc_id
		except AttributeError:
			self.doc_id = -1

	def memorize(self):
		self.doc_id = mind.memorize(self)
		return self
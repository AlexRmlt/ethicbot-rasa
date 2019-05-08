from . import mind
import random
import modules.constants as const

aliases = ['Amelie', 'Benjamin', 'Carla', 'Daniel', 'Esther', 'Frank', 'Greta', 'Harald', 'Inga', 'Jörg',
			'Katharina', 'Lars', 'Michelle', 'Nathan', 'Olga', 'Patrick', 'Roswitha', 'Samuel', 'Tanja', 'Uwe', 'Viola', 'Werner', 'Zoe']

collective = ['the Saxons', 'the Rhinelanders', 'the Palatines', 'the Bavarians', 'the Swabians', 'the Hessians']

class Entity(dict):
	def __init__(self,*arg,**kw):
		super(Entity, self).__init__(*arg, **kw)

		try:
			self.doc_id = arg[0].doc_id
		except AttributeError:
			self.doc_id = -1

	def memorize(self, s_id):
		self.doc_id = mind.memorize(s_id, self)
		return self


class Stakeholder(Entity):
	def __init__(self,*arg,**kw):
		super(Stakeholder, self).__init__(*arg, **kw)

		try:
			self.doc_id = arg[0].doc_id
		except AttributeError:
			self.doc_id = -1
	
	def set_name(self, s_id, name=None):
		if not 'name' in self:
			if name == None: # No name provided -> set random name
				try:
					if self['amount'] == 1:
						name = random.choice(aliases) 
						while (mind.stakeholder_exists(s_id, name)):
							name = random.choice(aliases)
					else:
						name = random.choice(collective) 
						while (mind.stakeholder_exists(s_id, name)):
							name = random.choice(collective)
				except KeyError:
					self['amount'] = -1
					name = random.choice(collective) 
					while (mind.stakeholder_exists(s_id, name)):
						name = random.choice(collective)
			self['name'] = name
		return self

	def set_moral_status(self, ms):
		self['moral_status'] = ms
		if ms == const.MS_HUMAN:
			self['moral_status_weight'] = 1
		elif ms == const.MS_MACHINE:
			self['moral_status_weight'] = 0
		else:
			self['moral_status_weight'] = -1
		return self

	def set_moral_status_weight(self, w):
		weight = w / 10
		self['moral_status_weight'] = weight
		return self

class Option(Entity):
	def __init__(self,*arg,**kw):
		super(Option, self).__init__(*arg, **kw)


class Consequence(Entity):
	def __init__(self,*arg,**kw):
		super(Consequence, self).__init__(*arg, **kw)


class Deed(Entity):
	def __init__(self,*arg,**kw):
		super(Deed, self).__init__(*arg, **kw)


class Context(Entity):
	def __init__(self,*arg,**kw):
		super(Context, self).__init__(*arg, **kw)
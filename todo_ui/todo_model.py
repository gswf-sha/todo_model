# -*- coding:utf-8 -*-
from openerp import models, fields, api

class Tag(models.Model):
	_name = 'todo.task.tag'
	_parent_store = True
	# _parent_name = 'parent_id'
	name = fields.Char('Name')
	parent_id = fields.Many2one('todo.task.tag','Parent Tag', ondelete='restrict')
	parent_left = fields.Integer('Parent Left', index=True)
	parent_right =  fields.Integer('Parent Right', index=True)
	child_ids = fields.One2many(
		'todo.task.tag','parent_id','Child Tags')
	task_ids = fields.Many2many('todo.task',string='Tasks')

class Stage(models.Model):
	_name = 'todo.task.stage'
	_order = 'sequence.name'
	# _rec_name= 'name' #the default
	# _table = 'todo_task_stage'

	# String fields:
	name = fields.Char('Name', 40)
	desc = fields.Text('Description')
	state = fields.Selection(
		[('draft','New'),('open','Started'),('done','Closed')],
		'State')
	docs = fields.Html('Documentation')
	# Numeric fields:
	sequence=fields.Integer('Sequence')
	perc_complete = fields.Float('% Complete',(3,2))
	# Date fields:
	date_effective = fields.Date('Effective Date')
	date_changed = fields.Datetime('Last Changed')
	# Other fields:
	fold = fields.Boolean('Folded?')
	image = fields.Binary('Image')

	task = fields.One2many(
		'todo.task', # related model
		'stage_id',  # field for this on related model
		'Tasks in this stage'
		)

class TodoTask(models.Model):
	_inherit = 'todo.task'
	stage_id =fields.Many2one('todo.task.stage','Stage')
	tag_ids = fields.Many2many('todo.task.tag',string='Tags')
	stage_fold = fields.Boolean(
		'Stage Folded?',
		compute='_compute_stage_fold')

	@api.one
	@api.depends('stage_id.fold')
	def _compute_stage_fold(self):
		self.stage_fold = self.stage_id.fold
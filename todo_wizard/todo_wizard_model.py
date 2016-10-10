# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp import exceptions 

import logging
_logger = logging.getLogger(__name__)

class TodoWizard(models.TransientModel):
	_name = 'todo.wizard'
	task_ids=fields.Many2many('todo.task',string='Tasks')
	new_deadline=fields.Data('Deadline to Set')
	new_user_id = fields.Many2one(
		'res.users',string='Responsible to Set')

	_logger.debug('A DEBUG message')
	_logger.info('An INFO message')
	_logger.warning('A WARNING message')
	_logger.error('An ERROR message')

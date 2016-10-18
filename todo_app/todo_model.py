# -*- coding: utf-8 -*-
from openerp import models, fields, api
class TodoTask(models.Model):
	"""docstring for TodoTask"""
	_name = 'todo.task'
	name = fields.Char('Description', required = True)
	is_done = fields.Boolean('Done?')
	active = fields.Boolean('Active', default = True)

	@api.one 
	def do_toggle_done(self):
		self.is_done = not self.is_done
		return True #XMLRPC Methods from client requires return sth
	@api.multi
	def do_clear_done(self):
		done_recs = self.search([('is_done','=',True)])
		done_recs.write({'active':False})
		return True

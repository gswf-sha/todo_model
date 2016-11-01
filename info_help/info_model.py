from openerp.addons.base.res.res_partner import format_address
from openerp.osv import fields, osv, orm
from openerp import models, fields, api
from openerp import exceptions 

import logging
_logger = logging.getLogger(__name__)

class InfoHelp(models.Model):
	"""the help page"""
	_name = 'info.help'
	base_intro = fields.Html('Introduction')
	func_easy = fields.Html('Basic functions')
	active = fields.Boolean('Active', default = True)

class SimplyLead(format_address, osv.osv):
	"""
	docstring for SimplyLead
	This is to inherit the CRM module of Odoo and do all the adjustments
	"""
	_name = 'crm.lead'
	_inherit = 'crm.lead'
	SourceUrl =fields.Char('Source Url')

class DateFormatAdjust(osv.osv):
	"""to adjust field format to accormadate for Chinese"""
	_name = 'crm.phonecall'
	_inherit = 'crm.phonecall'
	date = fields.Date('Date')
	
		
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
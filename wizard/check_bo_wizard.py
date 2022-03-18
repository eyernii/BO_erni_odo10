from difflib import restore
from email import message
from odoo import fields, models


class CheckBOWizard(models.TransientModel):
    _name = 'check.bo.wizard'
    _description = 'Message chek booking order'

    message = fields.Text(string='Message', stored=False) 

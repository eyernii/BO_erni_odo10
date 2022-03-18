from odoo import api, fields, models


class Serviceteam(models.Model):
    _name = 'sale.serviceteam'
    _description = 'New Description'

    name_id = fields.Char(string='Team Name')
    team_leader_id = fields.Many2one(comodel_name='res.users', string='Team Leader', required=True)
    team_member_ids = fields.Many2many(comodel_name='res.users', string='Team Member')
        

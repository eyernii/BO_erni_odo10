from email import message
from odoo import fields, models


class cancellation_work_order(models.TransientModel):
    _name = 'cancellation.work.order'
    _description = 'Message Cancellation work '

    notes= fields.Text(string='Reason')

    def action_cancel(self):
        self.env['sale.work.order'].browse(self.env.context['active_id']).update({'notes':self.notes, 'state':'cancelled'})

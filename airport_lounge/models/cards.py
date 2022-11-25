from odoo import models, fields


class CardDetails(models.Model):
    _name = 'card.details'
    _description = 'Card Details'
    _rec_name = 'code'
    code = fields.Char(string="Code", readonly=True,
                       help="code of card")
    description = fields.Char(string="Description", help="card name")
    unit_prize = fields.Float(string="Unit Prize",
                              help="unit prize of the stay")
    currency_id = fields.Many2one('res.currency', string="currency")
    agreement_status = fields.Selection([('active', 'activated'),
                                         ('deactivate', 'Deactivated')],
                                        help="if the card has an agreement")
    status = fields.Selection([('active', 'activated'),
                               ('deactivate', 'Deactivated')])







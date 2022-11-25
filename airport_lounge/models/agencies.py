from odoo import models, fields


class AgenciesDetails(models.Model):
    _name = 'agencies.details'
    _description = 'Agencies Details'
    _rec_name = 'code'
    code = fields.Char(string="Code")
    description = fields.Char(string="Description")
    ruc = fields.Integer(string="RUC")
    phone = fields.Integer(string="TelePhone")
    unit_price = fields.Float(string="Unit Price")
    currency_id = fields.Many2one('res.currency')
    state = fields.Selection([('draft', 'new'),
                              ('active', 'activated'),
                              ('deactive', 'deactivated'),
                              ('cancel', 'cancelled')], default="draft")
    address = fields.Char(strig="Address")
    country_id = fields.Many2one('res.country')
    state_id = fields.Many2one('res.country.state', string="State")
    city = fields.Char(string="City")

    def activate_airline(self):
        pass

    def deactivate_airline(self):
        pass

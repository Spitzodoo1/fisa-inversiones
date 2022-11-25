from odoo import models, fields


class AirlineClass(models.Model):
    _name = 'airline.class'
    code = fields.Char(string="Code")
    airline_id = fields.Many2one('airline.airline', string="Airline")
    state = fields.Selection([('draft', 'new'),
                              ('active', 'activated'),
                              ('deactive', 'deactivated'),
                              ('cancel', 'cancelled')], default="draft")
    airline_class = fields.Selection([('economy', 'Economy'),
                                      ('premium_economy', 'Premium Economy'),
                                      ('business', 'Business'),
                                      ('first_class', 'First Class')],
                                     string='Class'
                                     , help="Select the ticket class")
    parameter = fields.Char(string="Parameter")

    def activate_airline(self):
        pass

    def deactivate_airline(self):
        pass

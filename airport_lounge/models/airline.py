from odoo import models, fields


class Airline(models.Model):
    _name = 'airline.airline'
    _description = "Airline Details"
    _rec_name = 'name'

    code = fields.Char(string="Code")
    name = fields.Char(string="Airline")
    description = fields.Char(string="Description", help="Description"
                                                         "of the airline")

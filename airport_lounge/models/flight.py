from odoo import models, fields


class FlightDetails(models.Model):
    _name = 'flight.details'
    _rec_name = 'name'
    name = fields.Char(string="AirLine", help="Name of Airoplane")


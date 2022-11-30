from odoo import models, fields


class FrequentFireClass(models.Model):
    _inherit = 'passenger.registration'
    connection_code = fields.Char(string="Code")
    passenger_barcode = fields.Char(string="Passenger Code")



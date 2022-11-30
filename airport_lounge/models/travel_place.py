from odoo import models, fields


class TravelPlace(models.Model):
    _name = 'travel.place'
    code = fields.Char(string="Code")
    name = fields.Char(string="Name")

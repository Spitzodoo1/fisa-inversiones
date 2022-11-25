from odoo import models, fields


class CabinClass(models.Model):
    _name = 'cabin.class'
    code = fields.Char(string="Code")
    name = fields.Char(string="Name")

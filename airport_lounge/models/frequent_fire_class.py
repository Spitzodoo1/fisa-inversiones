from odoo import models, fields


class FrequentFireClass(models.Model):
    _name = 'frequent.fire.class'
    _rec_name = 'name'
    name = fields.Char(string="Frequent Fire Class", help="Name of Airoplane")


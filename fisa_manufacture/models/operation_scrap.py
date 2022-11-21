from odoo import models, fields, api


class ScrapInherited(models.Model):
    """adding fields weight And unit of measure"""
    _inherit = 'stock.scrap'
    weight = fields.Float(string="Weight")
    uom_id = fields.Many2one('uom.uom', string="Unit Of Measure")


from odoo import models, fields, api


class PackageInherited(models.Model):
    """add new weight unit of measure and barcode for pack"""
    _inherit = 'stock.quant.package'

    weight = fields.Float(string="Weight")
    uom_id = fields.Many2one('uom.uom', string="Unit of Measure")
    exp_date = fields.Date(string="Expiration Date")

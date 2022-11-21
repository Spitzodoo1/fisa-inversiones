from odoo import models, fields


class ProductTray(models.Model):
    _name = 'tray.tray'
    _rec_name = 'tray'
    tray = fields.Char(string="Tray")
    type = fields.Many2one('stock.package.type', string="Type")
    barcode = fields.Char(string="Barcode")

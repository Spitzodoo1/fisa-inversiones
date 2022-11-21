from odoo import models, fields


class BuffetDetails(models.Model):
    _name = 'buffet.details'
    _description = 'Buffet Details'
    _rec_name = 'buffet_id'
    buffet_id = fields.Many2one('stock.location', string="Buffet")
    origin = fields.Char(string="Order")
    tray_ids = fields.One2many('product.tray', 'buffet_details_id',
                               string="Tray line", )



from odoo import models, fields


class ProductTray(models.Model):
    _name = 'product.tray'
    _rec_name = 'tray_id'
    tray_id = fields.Many2one('tray.tray', string='Tray')
    quantity = fields.Float(string="Quantity")
    exp_hour = fields.Float(string="Expiration Hour")
    write_date = fields.Datetime(string="Write Date")
    picking_id = fields.Many2one('stock.picking', string='Origin')
    product_id = fields.Many2one('product.product', string='Product')
    location_id = fields.Many2one('stock.location', string="Buffet")
    buffet_details_id = fields.Many2one('buffet.details')

    def remove_tray(self):
        """remove only the quantity is zero"""
        self.unlink()

    def return_order(self):

        return {
            'type': 'ir.actions.act_window',
            'name': 'Return Order',
            'view_mode': 'form',
            'res_model': 'stock.picking',
            'res_id': self.picking_id.id,

            'target': 'new'

        }

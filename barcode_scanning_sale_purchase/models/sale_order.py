from odoo import api, models, fields


class SaleOrderLines(models.Model):
    _inherit = 'sale.order.line'

    barcode_scan = fields.Char(
        string='Product Barcode',
        help="Here you can provide the barcode for the product")

    @api.onchange('barcode_scan')
    def _onchange_barcode_scan(self):
        if self.barcode_scan:
            self.product_id = self.env['product.product'].search(
                [('barcode', '=', self.barcode_scan)]).id

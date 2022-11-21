from odoo import models, fields


class PackProduct(models.Model):
    """ for identify package include in manufacturing """
    _inherit = 'product.packaging'
    manufacture = fields.Boolean(string="Manufacture")


class FinalQuality(models.Model):
    """ after checking final quality test put in  pack """
    _inherit = 'mrp.production'
    has_packages = fields.Boolean(string="Pack")
    pack_id = fields.Many2one('stock.quant.package')

    def action_put_in_pack(self):
        """create new packing for manufactured product"""

        self.has_packages = True

        pack = self.env['stock.quant.package'].create(
            {})
        self.write({'pack_id': pack.id})
        picking_move_lines = self.env['stock.move.line'].search(
            [('origin', '=', self.name),
             ('product_id', '=', self.product_id.id)])
        picking_move_lines.write({'result_package_id': pack.id,

                                  })
        scrap = self.env['stock.scrap'].search(
            [('production_id', '=', self.id)])
        """for reducing quantity of product in  pack"""
        for rec in scrap:
            picking_move_line_scrap = self.env['stock.move.line'].search(
                [('reference', '=', self.name),
                 ('origin', '=', rec.name),
                 ('product_id', '=', self.product_id.id)])
            picking_move_line_scrap.write({'package_id': self.pack_id.id,
                                           })

    def action_see_packages(self):
        """smart button view of package"""
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id(
            "stock.action_package_view")
        action['domain'] = [('id', '=', self.pack_id.id)]
        return action


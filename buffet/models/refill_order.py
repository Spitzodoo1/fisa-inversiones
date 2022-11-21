from odoo import models, fields, api
from odoo.exceptions import UserError


class RefillOrder(models.Model):
    """refiling the item in buffet line"""
    _name = 'refill.order'

    @api.onchange('product_id')
    def change_product_id(self):
        return {'domain': {'product_id': [('id', 'in',
                                           self.origin_id.buffet_line_ids.mapped
                                           ('product_id').ids)]}}

    product_id = fields.Many2one('product.product', string="Product",
                                 help="refilling item")
    quantity = fields.Float(string="Quantity")
    origin_id = fields.Many2one('buffet.buffet')

    def button_conform(self):
        """creating internal transfer in stock picking"""
        self.ensure_one()

        values = []

        qty = self.env['stock.quant'].search(
            [('product_id', "=", self.product_id.id)
             ])
        fil = qty.filtered(lambda p: p.location_id.usage == 'internal')
        print(fil, "fillilii")

        for qt in fil:
            if self.quantity < qt.quantity:
                print(qt.location_id, "lotoloduk")
            source = qt.location_id.id

        loc = self.origin_id.buffet_id.location_id.id
        sloc = self.env['mrp.production'].search([('origin', '=',
                                                   self.origin_id.name
                                                   )], limit=1)
        print(sloc)
        if sloc:
            op_type = self.env['stock.picking.type'].search(
                [('code', '=', 'internal'),
                 ('warehouse_id', '=', sloc.picking_type_id.warehouse_id.id),
                 ('sequence_code', '=', 'INT')])
            print(op_type.warehouse_id.name, "poersstuikjk")

            for rec in self.origin_id:
                m = rec.env['stock.picking'].create({'origin': rec.name,
                                                     'location_id': op_type
                                                    .default_location_dest_id.id,
                                                     'location_dest_id': loc,
                                                     'picking_type_id': op_type.id,
                                                     'move_type': 'one',
                                                     'buffet': True,
                                                     })
                m.move_ids_without_package = [(5, 0, 0)]

                for l in self:
                    vals = {
                        'product_id': l.product_id,
                        'product_uom_qty': l.quantity,
                        'name': "uik",
                        'product_uom': l.product_id.uom_id,
                        'location_id': source,
                        'location_dest_id': loc,
                        'reserved_availability': l.quantity}

                    m.move_ids_without_package = [(0, 0, vals)]
                    values.append(vals)
                self.origin_id.write({'state': 'requested'})
        else:
            raise UserError("Please create a  manufacturing order for this "
                            "buffet,  "
                            )

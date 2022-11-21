from odoo import models, fields, api


class TrayInManufacture(models.Model):
    _inherit = 'mrp.production'
    tray = fields.Boolean(string="Do you need Tray", )
    buffet_id = fields.Many2one('buffet.buffet')
    product_tray = fields.Many2one('product.tray')
    tray_id = fields.Many2one('tray.tray')
    exp_hour = fields.Float(string="Expiration Hour")
    transfer_id = fields.Many2one('stock.picking')
    tray_quantity = fields.Float(string="Quantity for tray",
                                 help="quantity of item needs for tray")
    has_tray = fields.Boolean()

    @api.onchange('tray')
    def onchange_tray(self):

        data = self.env['tray.tray'].search([])
        list = []
        for rec in data:
            list.append(rec.id)

        product = self.env['product.tray'].search([('tray_id', 'in', list)])
        print("lilililili", product.mapped('tray_id').ids)
        return {'domain': {'tray_id':
                               [('id', 'not in',
                                 product.mapped(
                                     'tray_id').ids)]}}

    def action_put_in_tray(self):
        values = []
        op_type = self.env['stock.picking.type'].search(
            [('code', '=', 'internal'),
             ('warehouse_id', '=', self.picking_type_id.warehouse_id.id),
             ('sequence_code', '=', 'INT')])
        print(op_type, "picking")
        if self.buffet_id:
            for rec in self:

                m = rec.env['stock.picking'].create({'origin': rec.name,
                                                     'location_id':
                                                         rec.location_dest_id.id,
                                                     'location_dest_id':
                                                         rec.buffet_id.buffet_id.
                                                    location_id.id,
                                                     'picking_type_id':
                                                         op_type.id,
                                                     'move_type': 'one',
                                                     'buffet': True,
                                                     'tray': True
                                                     })
                print("location", rec.buffet_id.buffet_id.location_id.id)
                m.move_ids_without_package = [(5, 0, 0)]
                self.write({'transfer_id': m.id,
                            'has_tray': True})

                for l in self:
                    print(l.tray_quantity)
                    vals = {
                        'product_id': l.product_id,
                        'product_uom_qty': l.tray_quantity,
                        'name': "uik",
                        'product_uom': l.product_id.uom_id,
                        'tray_id': l.tray_id.id,
                        'exp_hour': l.exp_hour,
                        'location_id': l.location_dest_id.id,
                        'location_dest_id': rec.buffet_id.buffet_id.location_id.id,
                        'quantity_done': l.tray_quantity,
                        'reserved_availability': l.tray_quantity}

                    m.move_ids_without_package = [(0, 0, vals)]
                    values.append(vals)
                    print("exp_hour", l.product_id.id)
                    tray = l.env['product.tray'].search(
                        [('tray_id', '=', l.tray_id.id)])
                    if tray:
                        print("POPOP")
                        tray.write({'exp_hour': l.exp_hour,
                                    'product_id': l.product_id.id,
                                    })
                    else:
                        l.env['product.tray'].create(
                            {'tray_id' : l.tray_id.id,
                             'exp_hour': l.exp_hour,
                             'product_id': l.product_id.id,
                             })

        else:
            m = self.env['stock.picking'].create({'origin': self.name,
                                                  'location_id':
                                                      self.location_dest_id.id,
                                                  'location_dest_id':
                                                      self.location_dest_id.id,
                                                  'picking_type_id': op_type.id,
                                                  'move_type': 'one',
                                                  'buffet': True,
                                                  'tray': True
                                                  })
            m.move_ids_without_package = [(5, 0, 0)]
            self.write({'transfer_id': m.id,
                        'has_tray': True})

            for l in self:
                print(l.tray_quantity)
                vals = {
                    'product_id': l.product_id,
                    'product_uom_qty': l.tray_quantity,
                    'name': "uik",
                    'product_uom': l.product_id.uom_id,
                    'tray_id': l.tray_id.id,
                    'exp_hour': l.exp_hour,
                    'location_id': l.location_dest_id.id,
                    'location_dest_id': self.location_dest_id.id,
                    'quantity_done': l.tray_quantity,
                    'reserved_availability': l.tray_quantity}

                m.move_ids_without_package = [(0, 0, vals)]
                values.append(vals)
                print(values)
                tray = l.env['product.tray'].search(
                    [('tray_id', '=', l.tray_id.id)])
                print(l.product_id.id, "manutray")
                if tray:
                    tray.write({'exp_hour': l.exp_hour,
                                'product_id': l.product_id.id,
                                })
                    print("item,", l.product_id.id)

    def action_see_tray_transfer(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Refill Order',
            'view_mode': 'form',
            'res_model': 'stock.picking',
            'res_id': self.transfer_id.id,
            'target': 'current'

        }

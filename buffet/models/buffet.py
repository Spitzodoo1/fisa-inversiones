from odoo import models, fields, api
from datetime import datetime, date


class BuffetLocation(models.Model):
    _name = 'buffet.location'
    _rec_name = 'location_id'
    location_id = fields.Many2one('stock.location', string="Buffet Location",
                                  help="location of buffet")


class BuffetLine(models.Model):
    """for buffet management"""
    _name = 'buffet.buffet'
    _rec_name = 'buffet_id'
    buffet_id = fields.Many2one('buffet.location', string="Buffet",
                                help="location of buffet")
    buffet_line_ids = fields.One2many('buffet.line', 'buffet_id')
    date = fields.Date(string='Date', default=datetime.today(),
                       help="create date of buffet order")
    buffet_check = fields.Boolean()
    menu_type_id = fields.Many2one('buffet.menu.item', string="Menu",
                                   help="type of menu")

    state = fields.Selection(
        [('draft', 'new'),
         ('requested', 'Requested'),
         ('approved', 'Approved'),
         ('delivered', 'Delivered'),
         ('refill', '  Refill Request'),
         ('refilled', ' Refilled'),
         ('cancel', 'cancelled')
         ])
    name = fields.Char(readonly=True, required=True,
                       copy=False, default='New', string='Name')

    @api.onchange('menu_type_id')
    def onchange_product(self):
        """fill the available quantity of product if the menu type is changed"""

        for rec in self:
            rec.buffet_line_ids = [(5, 0, 0)]
            for line in self.menu_type_id.product_ids:
                vals = {
                    'product_id': line.id,
                    'available': line.qty_available
                }
                print(vals, "products")
                print(line.id, "lolo")

                rec.buffet_line_ids = [(0, 0, vals)]
                # print("kolo",rec.buffet_line_ids.product_id.id)
                # m = self.env['product.product'].search([('id', '=', line.id)])z
                # print("mmmmmmm", m)

    @api.model
    def create(self, vals):
        """sequence number"""
        self.write({'state': 'draft'})

        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'buffet.buffet') or 'New'
        result = super(BuffetLine, self).create(vals)

        return result

    def button_conform(self):
        print("vvvv")
        """button conform create manufacture order"""
        self.ensure_one()
        self.write({'state': 'requested',
                    'buffet_check': True})

        for rec in self.buffet_line_ids:
            bom = rec.env['mrp.bom'].search(
                [('product_tmpl_id', '=', rec.product_id.id)])
            print(" rec.product_id.id", rec.product_id.id)

            self.env['mrp.production'].create(
                {'product_id': rec.product_id.id,
                 'product_qty': rec.quantity,
                 'origin': rec.buffet_id.name,
                 'product_uom_id': rec.product_id.uom_id.id,
                 'buffet_id': self.id
                 })
            print(self.date)
            print(date.today())

    def re_send(self):
        """refilling request of the product"""

        vals = []
        for rec in self.menu_type_id.product_ids:
            vals.append(rec.id)
            print("vlds",vals)

        return {
            'type': 'ir.actions.act_window',
            'name': 'Refill Order',
            'view_mode': 'form',
            'res_model': 'refill.order',
            'context': {'default_origin_id': self.id},
            # 'domain': [('product_id', 'in', vals)],
            'target': 'new'

        }

    def refill_order(self):
        """refilling buffet line at kanban view"""
        return {
            'name': 'Order',
            'res_model': 'refill.order',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_type': 'form',
            # 'view_id': self.env.ref("buffet.buffet_views_form").id,
            'context': {'default_origin_id': self.id},

            'target': 'new',
        }

    def buffet_order(self):
        """form view of apply order for buffet-line at kanban view"""
        return {
            'name': 'Order',
            'res_model': 'buffet.buffet',
            'type': 'ir.actions.act_window',
            'res_id': self.id,
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': self.env.ref("buffet.buffet_views_form").id,
            'target': 'new'
        }


class ProductInheritedBuffet(models.Model):
    """buffet line"""
    _name = 'buffet.line'
    buffet_id = fields.Many2one('buffet.buffet', string="Buffet",
                                help="buffet location")
    product_id = fields.Many2one('product.product', string="Item",
                                 help="item of buffet")
    quantity = fields.Float(string="Quantity", required=True,
                            help="quantity need at the buffet")
    available = fields.Float(string="Available Quantity")


class StockPickingInherited(models.Model):
    """adding the details about tray and buffet in stock picking and
       product tray"""
    _inherit = 'stock.picking'

    buffet = fields.Boolean()
    remove = fields.Boolean(help="for identify the tray is removed ")
    tray = fields.Boolean(string="Tray")

    def button_validate(self):
        for rec in self.move_ids_without_package:
            line = rec.env['stock.move.line'].search(
                [('reference', '=', self.name)])
            line.write({'tray_id': rec.tray_id.id})
            tray = rec.env['product.tray'].search(
                [('tray_id', '=', rec.tray_id.id)])
            if tray.id:
                tray.write({'exp_hour': rec.exp_hour,
                            'picking_id': self.id,
                            'quantity': rec.quantity_done,
                            'product_id': rec.product_id.id,
                            'location_id': self.location_dest_id.id})
            else:
                if tray:
                    tray.create({'tray_id': rec.tray_id.id,
                                 'exp_hour': rec.exp_hour,
                                 'picking_id': self.id,
                                 'quantity': rec.quantity_done,
                                 'product_id': rec.product_id.id,
                                 'location_id': self.location_dest_id.id})
            buffet_location = self.env['buffet.details'].search(
                [('buffet_id', '=',
                  self.location_dest_id.id)])
            if buffet_location.buffet_id:
                tray_details = rec.env['product.tray'].search(
                    [('location_id', '=', self.location_dest_id.id)])
                vals = []
                for tr in tray_details:
                    vals.append(tr.id)

                buffet_location.write({'origin': self.origin,
                                       'tray_ids': vals
                                       })
            else:
                vals = []
                loc = self.env['buffet.location'].search(
                    [('location_id', '=', self.location_dest_id.id)])
                for l in loc:
                    vals.append(l.location_id.id)
                if self.location_dest_id.id in vals:
                    buffet_location.create(
                        {'buffet_id': self.location_dest_id.id,
                         'origin': self.origin,
                         'tray_ids': rec.tray_id.ids})
                else:
                    pass

        return super(StockPickingInherited, self).button_validate()

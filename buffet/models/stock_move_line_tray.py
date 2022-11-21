from odoo import models, fields, api


class MoveLineTray(models.Model):
    _inherit = 'stock.move.line'
    tray_id = fields.Many2one('tray.tray')


class MoveTray(models.Model):
    _inherit = 'stock.move'

    @api.onchange('tray_id')
    def onchange_tray(self):
        print(self, "pivlllllllllll")
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

    tray_id = fields.Many2one('tray.tray')
    exp_hour = fields.Float(string="Expiration Hour")

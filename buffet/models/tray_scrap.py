from odoo import models, fields


class ScrapTray(models.Model):
    _inherit = 'stock.scrap'
    product_tray_id = fields.Many2one('product.tray')

    def action_validate(self):
        srap = self.env['removing.tray'].search(
            [('tray_id', '=', self.product_tray_id.tray_id.id)])
        print('srap', srap)
        mm = srap.write({'remove': True,
                         'state': 'remove'})
        print(mm)

        tray = self.env['product.tray'].search(
            [('id', '=', self.product_tray_id.id),
             ('product_id', '=', self.product_id.id)])
        print(tray, "erdftyghuj")
        tray.unlink()

        return super(ScrapTray, self).action_validate()

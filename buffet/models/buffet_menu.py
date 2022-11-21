from odoo import models, fields


class BuffetMenu(models.Model):
    _name = 'buffet.menu'
    _description = 'Buffet Menu'
    _rec_name = 'type'
    type = fields.Char(string="MenuType",help="menu type like breakfast,"
                                              " lunch etc ")


class BuffetMenuItems(models.Model):
    _name = 'buffet.menu.item'
    _rec_name = 'menu_type_id'
    product_ids = fields.Many2many('product.product', string="Item",
                                   help="menu items in buffet line")
    menu_type_id = fields.Many2one('buffet.menu', string="Menu Type",
                                   help="type of menu")
    buffet_location_id = fields.Many2one('buffet.location', string="Buffet "
                                                                   "Location")
    User_id = fields.Many2one('res.users', string="Responsible Person",
                              help="responsible person of buffet")

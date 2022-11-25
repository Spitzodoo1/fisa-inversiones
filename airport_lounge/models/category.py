from odoo import models, fields


class CategoryDetails(models.Model):
    _name = "category.details"
    _description = 'Airline Category'
    _rec_name = 'category'
    category = fields.Char(string='category'
                           , help="Select the category")
    state = fields.Selection([('active', 'activate'),
                              ('deactive', 'Deactivate')], string='State')

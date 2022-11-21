from odoo import models, fields


class VendorDetailsInherited(models.Model):
    _inherit = 'res.partner'

    type_of_client_long_id = fields.Many2one(
        'vendor.details', string="Type of Client Long")
    type_of_client_short = fields.Selection(
        string="Type of Client Short",
        selection=[('b2b', 'B2B'), ('b2c', 'B2C')])
    place_of_invoicing_id = fields.Many2one(
        'vendor.invoice', string="Place of invoicing")
    contract_expiration_date = fields.Date(string="Contract Expiration Date")
    suspend = fields.Boolean(default=True, string="Active")

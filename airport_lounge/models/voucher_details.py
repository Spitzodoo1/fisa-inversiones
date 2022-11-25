from odoo import models, fields


class VoucherDetails(models.Model):
    _name = 'voucher.details'
    voucher_name = fields.Char(string="Voucher")

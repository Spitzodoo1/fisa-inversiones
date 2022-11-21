from odoo import models, fields


class VendorDetails(models.Model):
    """for the type of client"""

    _name = 'vendor.details'
    _description = "Vendor Details"

    _rec_name = "type_of_client_long"
    type_of_client_long = fields.Char(string="Type of Client Long",
                                      translate=True)


class VendorInvoice(models.Model):
    """ for plac of invoicing if vendor is addressed or not addressed"""
    _name = 'vendor.invoice'
    _description = "Vendor Invoice"

    _rec_name = 'place_of_invoicing'
    place_of_invoicing = fields.Char(string="Place of Invoicing",
                                     translate=True)

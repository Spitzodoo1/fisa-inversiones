from odoo import models, fields


class Branch(models.Model):
    _name = 'fisa.branch'
    _description = 'fisa branches'
    _rec_name = 'name'
    name = fields.Char(string="Name")
    address = fields.Char(strig="Address")
    country_id = fields.Many2one('res.country')
    state_id = fields.Many2one('res.country.state', string="State")
    city = fields.Char(string="City")
    mail = fields.Char(string="Mail")
    phone = fields.Integer(string="Phone")
    contact = fields.Integer(string="Contact")
    website = fields.Char(string="website")

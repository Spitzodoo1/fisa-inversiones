from odoo import models, fields


class TypeClient(models.Model):
    _name = 'type.client'
    name = fields.Char(string=" Client")
    branch_id = fields.Many2one('fisa.branch', string="Saloon")
    tariff = fields.Float(string="Tariff")
    extra_time = fields.Boolean(string="Extra Time Allowed By Contract")
    tolerance_in_min = fields.Integer(string="Tolerance In Min")
    hours_allowed_in = fields.Integer(string="Allowed Hour")
    num_of_new_entrance = fields.Integer(string="Number of New Entrance")
    drinks_number = fields.Integer(string="Drinks Number")
    access = fields.Boolean(string=" Have Access By MemberShip Card?")

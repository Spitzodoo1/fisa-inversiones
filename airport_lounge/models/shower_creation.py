from odoo import models, fields, api


class ShowerCreation(models.Model):
    _name = 'shower.creation'
    state = fields.Selection(
        [('available', 'available '),
         ('maintenance', 'maintenance'),
         ('cleaning', 'cleaning'),
         ('booked', 'booked'),
         ], required=True, default='available')
    name = fields.Char(string="Shower")
    branch_id = fields.Many2one('fisa.branch', string="Branch")
    maintenance = fields.Boolean(string="maintenance")
    cleaning = fields.Boolean(string="Cleaning")

    def conform_shower(self):
        rec = self.env['shower.service'].search([('shower_id', '=', self.id)])

        if self.maintenance:
            self.write({'state': 'maintenance'})
            if rec:
                rec.write({'maintenance': True})

        if self.cleaning:
            self.write({'state': 'cleaning'})
            if rec:
                rec.write({'cleaning': True})

        if rec:
            rec.write({'state': self.state})

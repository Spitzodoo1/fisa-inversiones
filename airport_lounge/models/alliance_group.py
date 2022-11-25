from odoo import models, fields, api


class AllianceGroup(models.Model):
    _name = 'alliance.group'
    _description = 'Alliance Group'
    _rec_name = 'code'
    code = fields.Char(string="Code", readonly=True)
    description = fields.Char(string="Description")
    state = fields.Selection([('draft', 'new'),
                              ('active', 'activated'),
                              ('deactive', 'deactivated'),
                              ('cancel', 'cancelled')], default="draft")

    @api.model
    def create(self, vals):
        vals['code'] = self.env['ir.sequence'].next_by_code(
            'alliance.group')

        result = super(AllianceGroup, self).create(vals)
        return result

    def activate_group(self):
        self.write({'state': 'active'})

    def deactivate_group(self):
        self.write({'state': 'deactive'})

    def cancel_group(self):
        self.write({'state': 'cancel'})

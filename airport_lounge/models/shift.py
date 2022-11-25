from odoo import models, fields


class EmployeeShift(models.Model):
    _inherit = 'hr.employee'
    emp_shift_id = fields.Many2one('planning.slot.template', string="Shift")

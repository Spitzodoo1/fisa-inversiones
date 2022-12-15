from odoo import models, fields, api


class ShowerService(models.Model):
    _name = 'shower.service'
    _rec_name = 'shower_id'
    state = fields.Selection(
        [('available', 'available '),
         ('maintenance', 'maintenance'),
         ('cleaning', 'cleaning'),
         ('booked', 'booked'),
         ], required=True, default='available')
    shower_id = fields.Many2one('shower.creation', string="Shower",
                                domain="[('state','=','available')]")
    shower_max = fields.Integer(string="Allowed Shower")
    branch_id = fields.Many2one('fisa.branch', string="Branch")
    cleaning_time = fields.Integer(string="Cleaning Time", default=15,
                                   readonly=True)
    usage_time = fields.Integer(string="Usage Time", default=45, readonly=True)
    passenger_id = fields.Many2one('passenger.registration',
                                   string="Passenger Name")
    maintenance = fields.Boolean(string="Maintenance")
    cleaning = fields.Boolean(string="Cleaning")
    color = fields.Integer()
    time_schedule_start = fields.Float(string="Time Schedule Start")
    time_schedule_end = fields.Float(string="Time Schedule End")

    def action_conform(self):
        self.write({'state':'booked'})
        self.shower_id.write({'state':'booked'})
        print("pppppppppp")

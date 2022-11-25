from odoo import models, fields, api


class FlightDetails(models.Model):
    _name = 'user.registration'

    name = fields.Char(string="User Name", help="Name of User")
    identification = fields.Char(string="Identification Number",
                                 readonly=True)
    _sql_constraints = [('identification',
                         'unique(identification)',
                         'identification'
                         ' must be unique!')]

    type_of_client_id = fields.Many2one('type.client', string="Type of client",
                                        help="Type of client")
    airline_id = fields.Many2one('flight.details', string='Airline')
    phone = fields.Integer(string="Phone")
    email = fields.Char(string="Email")
    age = fields.Integer(string="Age")
    country_of_destiny_id = fields.Many2one('res.country',
                                            string='Country of Destiny')
    city_of_destiny = fields.Char(string='City of Destiny')
    commercial_name = fields.Char(string="Commercial Name")
    legal_name = fields.Char(string='Legal Name')
    vat_number = fields.Integer(string="VAT Number")
    ticket_class = fields.Selection([('economy', 'Economy'),
                                     ('premium_economy', 'Premium Economy'),
                                     ('business', 'Business'),
                                     ('first_class', 'First Class')],
                                    string='Class'
                                    , help="Select the ticket class")
    date_entrance = fields.Datetime(string="Date Of Entrance")
    hour = fields.Float(string="Hour of Entrance")
    date_of_exit = fields.Datetime(string="Date of exit")
    hour_of_exit = fields.Float(string="Hour of exit")
    # registered_by = fields.Many2one('res.users', string='Registered By',
    #                                 default=lambda self: self.env.user)
    tariff = fields.Float(string="Tariff")
    ticket_number = fields.Char(string="Ticket Number")
    date_of_flight = fields.Datetime(string="Date of Flight")
    hour_of_flight = fields.Float(string="Hour of flight")
    pass_port_no = fields.Char(string="Passport Number")

    @api.model
    def create(self, vals):
        vals['identification'] = self.env['ir.sequence'].next_by_code(
            'user.registration')

        result = super(FlightDetails, self).create(vals)
        return result

    def register(self):
        self.write({'state': 'register'})

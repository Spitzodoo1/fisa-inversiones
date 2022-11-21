from datetime import datetime

from odoo import models, fields, api


class PettyCashManagement(models.Model):
    """for adding petty cash details"""
    _name = 'petty.cash'
    _rec_name = 'user_id'
    date = fields.Datetime(string="Date", default=datetime.today())
    user_id = fields.Many2one('res.users', string="Responsible",
                              default=lambda self: self.env.user)
    line_ids = fields.One2many('petty.cash.line', 'petty_id')
    petty_limit = fields.Float(" Cash Limit",
                               compute='_compute_petty_cash_limit',
                               readonly=True)
    limit = fields.Boolean(string="exceed limit")
    petty = fields.Boolean()
    state = fields.Selection(
        [('draft', 'new'),
         ('requested', 'Requested'),
         ('send', 'Send To Manager'),
         ('approved', 'Approved'),
         ('rejected', 'Rejected'),
         ('approve', 'Manager Approved'),
         ('transmitted', 'Transmitted'),
         ('cancel', 'cancelled')
         ], default='draft')

    @api.depends('date')
    def _compute_petty_cash_limit(self):
        """compute petty cash limit"""

        self.petty_limit = self.env['ir.config_parameter'].sudo().get_param(
            "petty_cash_management.petty")

    # def button_internal_transfer(self):
    #     # """internal transfer of payment"""
    #     amount = []
    #     # print("ooooo")
    #     for recs in self:
    #         for rec in recs.line_ids:
    #             amount.append(rec.amount)
    #             print(amount, "a,oiu")
    #     payment = self.env['account.payment'].create({
    #         'amount': sum(amount),
    #         'is_internal_transfer': True, })
        # print(payment, "payment")
        # """for reconcile the particular  petty-cash """
        # values = []
        # for rec in self:
        #     p = rec.env['account.bank.statement'].create({
        #         'journal_id': 10,
        #     })
        #     print(p,"p")
        # p.line_ids = [(5, 0, 0)]
        # for l in self.line_ids:
        #     vals = {
        #         'partner_id': l.partner_id.id,
        #         'date': l.date,
        #         'amount': l.amount,
        #         'payment_ref': "Petty Cash"
        #     }
        #
        #     p.line_ids = [(0, 0, vals)]
        #     values.append(vals)
        # self.write({'state': 'transmitted',
        #             'petty': False})

        # return {
        #     'type': 'ir.actions.act_window',
        #     'context': {},
        #     'res_id': payment.id,
        #     'view_mode': 'form',
        #     'view_type': 'form',
        #     'res_model': 'account.payment',
        #     'target': 'current'
        #
        # }

    def button_conform(self):
        """conform the petty cash request"""

        amount = []
        for recs in self:
            for rec in recs.line_ids:
                amount.append(rec.amount)
        if sum(amount) > self.petty_limit:
            self.limit = True

        self.write({'state': 'requested', }
                   )

    def button_approve(self):
        """approve the petty cash"""

        self.write({'state': 'approved',
                    'petty': True})

    def button_reject(self):
        """reject the petty cash request"""
        self.write({'state': 'cancel'})

    def send_manager(self):
        """ request send to the manager if the limit exceed"""
        self.write({'state': 'send'})

    def approve_manager(self):
        """approve the manager if limit is smaller-than the requested limit"""
        self.write(({'state': 'approve',
                     'limit': False}))

    def reject_manager(self):
        """reject the manager if limit is smaller-than the requested limit"""

        self.write(({'state': 'reject'}))


class InheritBankStatementLine(models.Model):
    """details of petty cash """
    _name = 'petty.cash.line'
    petty_id = fields.Many2one('petty.cash', string="petty cash")
    date = fields.Date(string="Date", requerd=True)
    partner_id = fields.Many2one('res.partner', string="Partner", requred=True)
    amount = fields.Float(string="Amount", requared=True)


class PettyCash(models.TransientModel):
    """set the petty cash limit in settings """
    _inherit = "res.config.settings"

    petty = fields.Float(string="Petty Cash Limit")

    @api.model
    def get_values(self):
        res = super(PettyCash, self).get_values()
        res['petty'] = self.env['ir.config_parameter'].sudo().get_param(
            "petty_cash_management.petty", default="")
        return res

    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].set_param("petty_cash_management.petty",
                                                  self.petty or '')
        super(PettyCash, self).set_values()

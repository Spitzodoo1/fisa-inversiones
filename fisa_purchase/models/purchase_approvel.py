from odoo import models, fields
from odoo.exceptions import UserError


class PurchaseApprove(models.Model):
    _inherit = 'purchase.order'

    state = fields.Selection(selection_add=
                             [('checked', 'checked budget '),
                              ('waiting_approval', 'waiting for approval'),
                              ('approved', 'approved order'),
                              ('sent_to_approve', 'sent to manager'),
                              ('manager_approved', 'manager approved budget'),
                              ('sent',)],
                             ondelete={'checked': 'cascade',
                                       'waiting_approval': 'cascade',
                                       'approved': 'cascade'})
    check_amount = fields.Boolean(default=False)

    def check_budget(self):
        """check budget if budget is greater than the monthly budget send to
        budget approver """

        if self.amount_total > self.company_id.po_double_validation_amount:
            self.write({'check_amount': 'True', 'state': 'checked'})
        else:
            self.write({'state': 'waiting_approval'})

    def approve_budget(self):
        """for approve budget by the manager """
        self.write({'state': 'manager_approved'})

    def approve_order(self):
        """ approve purchase order """
        self.write({'state': 'approved'})

    def button_approve_manager(self):
        """for approving  the rfq is the total amount greater than send to it
        to the manager """

        if self.amount_total < self.company_id.po_double_validation_amount:
            raise UserError("Please click the Check Button,  "
                            "This Order has Not an extraordinary expense")

        self.write({'state': 'sent_to_approve', 'check_amount': False})

    def button_disapprove_budget(self):
        """disapprove the budget"""
        self.write({'state': 'cancel'})

    def button_confirm(self):
        """ overwrite  button conform """

        for order in self:
            if order.state not in ['draft', 'sent', 'approved']:
                continue
            order._add_supplier_to_product()
            if order._approval_allowed():
                order.button_approve()
            else:
                order.write({'state': 'to approve'})
            if order.partner_id not in order.message_partner_ids:
                order.message_subscribe([order.partner_id.id])
        if not self.partner_id.suspend:
            raise UserError(" Sorry !!!! This Vendor is not active. "
                            " Purchase Order is Suspended .")
        return True

    def button_disapprove(self):
        self.write({'state': 'cancel'})


class MailComposer(models.TransientModel):
    _inherit = 'mail.compose.message'

    def action_send_mail(self):
        po = self.env['purchase.order'].search([('id', '=', self.res_id)])
        po.write({'state': 'sent'})
        return super(MailComposer, self).action_send_mail()

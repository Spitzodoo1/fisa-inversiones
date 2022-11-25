from odoo import models, fields


class BranchAccess(models.Model):
    _name = "branch.access"
    _description = 'Branch Access'
    branch_id = fields.Many2one('fisa.branch')

    def get_branch_access(self):
        print("ins")
        res = []

        branches = self.env['fisa.branch'].search([])
        for rec in branches:
            res.append({'id':rec.id,
                        'name':rec.name})
        print(res)

        return res

    def get_mo(self):
        print("fdxghj")

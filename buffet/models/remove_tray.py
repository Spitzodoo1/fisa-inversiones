import datetime
import pytz

from odoo.exceptions import UserError
import odoo
import math

from odoo import models, fields


class RemoveTray(models.Model):
    _name = 'removing.tray'
    _rec_name = 'tray_id'
    tray_id = fields.Many2one('tray.tray')
    exp_hour = fields.Float()
    product_id = fields.Many2one('product.product')
    state = fields.Selection([('draft', 'draft '),
                              ('remove', 'removed'),
                              ], required=True, default='draft')
    remove = fields.Boolean(string="remove")
    location_id = fields.Many2one('stock.location')
    picking_id = fields.Many2one('stock.picking')

    def cron_remove_tray(self):
        print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
        # user_tz = self.env.user.tz or pytz.utc
        # local = pytz.timezone(user_tz)

        picking = self.env['stock.picking.type'].search([('code', '=',
                                                          'internal')])

        tray = self.env['product.tray'].search(
            [])
        print("tray", tray)
        for r in tray:
            print(r.picking_id.id)

        for rec in tray:
            dates = rec.env['stock.picking'].search(
                [('id', '=', rec.picking_id.id)])
            print(dates, "...............................")

            user_tz = self.env.user.tz
            print("utime", self.env.user.tz)

            if not user_tz:
                raise odoo.exceptions.Warning(
                    (" Please set time zone in your prefereces"))

            to_usertz = pytz.timezone(user_tz) or pytz.utc

            localutc = pytz.timezone('UTC')

            check_in = localutc.localize(dates.date_done).astimezone(to_usertz)
            print("datetime", check_in)
            today = datetime.datetime.now()
            print(today, "ennnnnnnnnnnnnnnnnnnnnnn")
            day = localutc.localize(today).astimezone(to_usertz)
            thour = float(day.strftime("%H"))
            print("ennmanikkoor", thour)
            tmin = float(day.strftime("%M"))
            print("tmin", tmin)
            # trayhour=float(str(dates.move_ids_without_package.exp_hour).strftime("%H"))
            # print(trayhour)
            if dates.date_done:
                mins_string = str(dates.move_ids_without_package.exp_hour)
                tsplit_mints = mins_string.split(".", 1)
                tray_mints = int(tsplit_mints[1])
                tray_hour = int(tsplit_mints[0])
                print("54", tray_mints)
                hour = float(check_in.strftime("%H"))
                min = float(check_in.strftime("%M"))
                sec = float(check_in.strftime("%S"))
                print('sec', sec)
                print('min', min)
                print("createhour", hour)
                exceed = thour - hour
                exceed_sec = sec - 0
                exceed_min = (tmin - min)
                print(exceed, "exceed hour")
                print('exceed_min', exceed_min)
                # print("trayhour", dates.move_ids_without_package.exp_hour)
                print(tray_mints)
                if abs(exceed) >= tray_hour:
                    print(math.floor(dates.move_ids_without_package.exp_hour),
                          'mmmmmmmmmmmmmmmmmmmmm')
                    if exceed_min >= tray_mints:
                        print("dfghjk")

                        tr = self.env['removing.tray'].search([('tray_id',
                                                                '=',
                                                                dates.move_ids_without_package.tray_id.id),
                                                               (
                                                                   'picking_id',
                                                                   '=',
                                                                   dates.id)])
                        print("ggggggggggggggggggg", tr)
                        if not tr:
                            m = self.create(
                                {
                                    'product_id': dates.move_ids_without_package.product_id.id,
                                    'tray_id': dates.move_ids_without_package.tray_id.id,
                                    'exp_hour': dates.move_ids_without_package.exp_hour,
                                    'location_id': dates.location_dest_id.id,
                                    'picking_id': dates.id, })
                            print("h",
                                  m)
                        template = self.env.ref(
                            'buffet.exp_notification_email_template',
                            raise_if_not_found=False)
                        print(template)
                        user_email = self.env.user.login
                        user = self.env.user.name
                        to_email = self.env.user.login
                        print(user_email, "user")

                        ctx = {
                            'tray_id': dates.move_ids_without_package.tray_id.tray,
                            'user': user,
                            'buffet': dates.location_dest_id.name,
                            'from_email': user_email,
                            'to_email': to_email
                        }
                        print(ctx, "ctx")
                        mol = template.sudo().with_context(ctx).send_mail(
                            self.env.user.id,
                            force_send=True)
                        print(mol, "memail")

                        template = self.env.ref(
                            'buffet.exp_notification_email_template',
                            raise_if_not_found=False)
                        print(template)
                        user_email = self.env.user.login
                        user = self.env.user.name
                        print(user_email, "user")

                        ctx = {
                            'tray_id': dates.move_ids_without_package.tray_id.tray,
                            'user': user,
                            'buffet': dates.location_dest_id.name,
                            'from_email': user_email,
                            'to_email': to_email

                        }
                        print(ctx, "ctx")
                        mol = template.sudo().with_context(
                            ctx).send_mail(
                            self.env.user.id,
                            force_send=True)
                        print(mol, "memail")
                else:
                    print("dfghjkl")
                    pass

    def remove_tray(self):
        """remove tray if the quantity of product is zero"""

        tray = self.env['product.tray'].search(
            [('tray_id', '=', self.tray_id.id),
             ('product_id', '=', self.product_id.id)])
        print("lkakakak", tray)
        self.write({'remove': True,
                    'state': 'remove'})
        tray.unlink()

    def return_tray(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Return Order',
            'view_mode': 'form',
            'res_model': 'stock.picking',
            'res_id': self.picking_id.id,
            # 'res_id': self.picking_id.id,
            # 'domain': [('id', '=', self.picking_id)],
            'target': 'new'

        }

    def scrap_tray(self):
        tray = self.env['product.tray'].search(
            [('tray_id', '=', self.tray_id.id)])
        return {
            'type': 'ir.actions.act_window',
            'name': 'Return Order',
            'view_mode': 'form',
            'res_model': 'stock.scrap',
            # 'res_id': self.picking_id.id,
            # 'res_id': self.picking_id.id,
            # 'domain': [('id', '=', self.picking_id)],
            'context': {'default_product_id': self.product_id.id,
                        'default_location_id': self.location_id.id,
                        'default_product_tray_id': tray.id},
            'view_id': self.env.ref('stock.stock_scrap_form_view2').id,
            'target': 'new'

        }

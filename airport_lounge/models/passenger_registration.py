from odoo import models, fields, api
import re

from datetime import datetime


class PassengerRegistration(models.Model):
    _name = 'passenger.registration'
    _description = 'Passenger Registration Details'
    _rec_name = 'name'
    passenger_data_by = fields.Selection(
        [('agreement cards', 'Agreement cards'),
         ('airlines', 'Airlines'),
         ('sales', 'Sales'),
         ('agencies', 'Agencies')],
        string='Passenger Data By'
        , help="able to visualize and enter"
               " passenger data by")
    passenger = fields.Char(string="Passenger")
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    date_passenger = fields.Date(string="Date")
    name = fields.Char(string='code')
    state = fields.Selection(
        [('draft', 'draft '),
         ('register', 'registerd'),
         ], required=True, default='draft')

    date_attention = fields.Datetime(string="Date Attention")
    client_id = fields.Many2one('type.client', string="Client")
    airline_id = fields.Many2one('airline.airline', string="Airline")
    date = fields.Datetime(string="Date", default=datetime.today())
    time_alert = fields.Float()
    origin = fields.Char(string="Origin",
                         help="he place from which the passenger is departing "
                              "is indicated")
    destination = fields.Char(string="Destination",
                              help="where the passenger is going.")
    category_id = fields.Many2one('category.details', string="Category")
    no_of_people = fields.Integer(string="Number Of People",
                                  help="is represented by the number"
                                       " 1 but if it is a guest,"
                                       " it is represented by 0")
    flight_number = fields.Char(string="Flight Number"
                                , help="type the first two digits of "
                                       "the airline and the flight number")
    seat_number = fields.Char(string="Seat Number")

    cabin_class_id = fields.Many2one('cabin.class', string="Cabin class")
    voucher_id = fields.Many2one('voucher.details', string="Voucher",
                                 help="represents and indicates the guest to "
                                      "the airline, agency, cards among "
                                      "others")
    voucher_qty = fields.Integer(dstring="Voucher Quantity")
    account_number = fields.Integer(string="Account Number")
    reservation = fields.Char(string="Reservation Code")
    frequent_passenger_number = fields.Char(
        string="Frequent Passenger Number")
    authorised_by = fields.Char(string="Authorised By")
    invoiced_group = fields.Char(string="Invoice Group")
    invitation = fields.Binary(string="Attach Invitation",
                               )
    observation = fields.Char(string="Observation")

    identification = fields.Char(string="Identification Number",
                                 readonly=True)
    _sql_constraints = [('identification',
                         'unique(identification)',
                         'identification'
                         ' must be unique!')]

    type_of_client_id = fields.Many2one('type.client', string="Type of client",
                                        help="Type of client")
    phone = fields.Integer(string="Phone")
    email = fields.Char(string="Email")
    age = fields.Integer(string="Age")
    country_of_destiny_id = fields.Many2one('res.country',
                                            string='Country of Destiny')
    city_of_destiny = fields.Char(string='City of Destiny')
    commercial_name = fields.Char(string="Commercial Name")
    legal_name = fields.Char(string='Legal Name')
    vat_number = fields.Integer(string="VAT Number")
    # ticket_class = fields.Selection([('economy', 'Economy'),
    #                                  ('premium_economy', 'Premium Economy'),
    #                                  ('business', 'Business'),
    #                                  ('first_class', 'First Class')],
    #                                 string='Class'
    #                                 , help="Select the ticket class")
    date_entrance = fields.Datetime(string="Date Of Entrance")
    date_of_exit = fields.Datetime(string="Date of exit")

    tariff = fields.Float(string="Tariff")
    ticket_number = fields.Char(string="Ticket Number")
    date_of_flight = fields.Datetime(string="Date of Flight Departurel")
    hour_of_flight = fields.Float(string="Hour of flight")
    pass_port_no = fields.Char(string="Passport Number")
    no_of_guest = fields.Integer(string="No.Of.Guest", default=5)
    no_of_guest_pay = fields.Integer("No.Of.Guest To Pay", defualt=5)
    no_of_guest_entry = fields.Integer("No.Of.Entry Guest")
    bar_courtesy = fields.Integer(string="Bar Courtesy", default=1)
    entry_time_allowed = fields.Float(string="Entry Time Allowed")
    hour_of_exit = fields.Float(string=" Exit time")
    hour_entry = fields.Float(string="Exact Entry Time")
    camera_capture = fields.Binary()

    @api.model
    def create(self, vals):
        self.state = 'draft'
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'passenger.registration') or 'New'
        result = super(PassengerRegistration, self).create(vals)
        print("result", result)
        return result

    def passenger_alert(self):
        pass

    def action_invitation(self):
        pass

    def guest_registration(self):
        pass

    def shower_registration(self):
        pass

    @api.onchange('passenger')
    def onchangeObservation(self):
        s = str(self.passenger)
        sp = ' '
        first_na = s.split(sp)
        si = str(first_na[0])
        so = si.split('/')
        first_name = [i for i in first_na if i]
        print(first_name)
        print(len(first_name))
        print(first_na)

        '''for removing space'''
        for i in range(len(first_name)):
            print(first_name[i])

            length = len(list(first_name[i]))
            reservation = []

            if '/' in first_name[i]:
                name = first_name[i].split('/')
                print("names", name)
                m = list(first_name[0])
                print(m)
                for i in range(2):
                    print("sdfghjkl")
                    m.pop(0)
                    print("kalapani", m)
                exa_name = "".join([str(i) for i in m])
                rs_code = exa_name
                if 'E' in name[1]:
                    findex = name[1]
                    in1 = findex.index('E')
                    in2 = len(name[1])
                    in_last = in2 - 6
                    in_last1 = in2 - 7
                    print("1", in2)
                    print("2", in1)
                    print("5", in_last1)
                    print(in_last, "kolo")
                    e = list(name[1])
                    if len(name[1]) > 6:

                        print("object", e)
                        reverse = findex[::-1]

                        print('reversess', reverse)
                        rev = list(findex)
                        inrev = rev.index('E')
                        print(len(rev))
                        last_length = len(rev) - inrev
                        range_e = e[-6]
                        r = e.index(range_e)
                        print("rrrrrrr", (e[-7]))

                        for i in range(r, len(e)):
                            print("jiiii")
                            reservation.append(rev[i])
                        print("omale", reservation)
                        reservation_code = "".join(
                            [str(i) for i in reservation])
                        print('reservation_codes', reservation_code)
                        if e[-7] == 'E':
                            if reservation != name[1]:
                                if len(reservation_code) == 6:
                                    if not self.reservation:
                                        self.write(
                                            {'reservation': reservation_code})
                                        print(reservation, "poi")
                    else:
                        if len(list(first_name[1])) == 6:
                            print("joo")
                            if not self.reservation:
                                self.write(
                                    {'reservation': first_name[
                                        1]})

                if '/' in exa_name:
                    exact_na = exa_name.split('/')
                    exact_name = exact_na[0]
                    print("extna", exact_name)
                    self.write({'last_name': exact_name,
                                'first_name': exact_na[1]})
                    print("popi", exact_na[1])
                    print("lastaaaaaaaa", exact_na[1])
                    if first_name[1]:
                        if 'E' not in list(first_name[1]):
                            print("common")
                            if self.last_name:
                                if len(first_name[1]) != 6:
                                    self.write(
                                        {'first_name': exact_na[1] + " " +
                                                       first_name[
                                                           1]})
                        else:
                            findex = first_name[1]
                            code = list(findex)
                            print(len(code), "length")
                            print(code, "tippp")
                            reverse = code[::-1]

                            range_s = reverse[-6]
                            print("strtng", range_s)
                            reser_code = []
                            starting_index = reverse.index(range_s)
                            print("kutiiii", starting_index)
                            for i in range(starting_index, len(code)):
                                reser_code.append(code[i])
                                print(reservation, "1669")
                            reservation_code = "".join(
                                [str(i) for i in reser_code])
                            if not self.reservation:
                                print("webiii")
                                self.write({'reservation': reservation_code})
                                print("*******888", self.reservation)

                            print("!!!!!!!!!!!!!!!!!!!!!!")
                            if len(code) > 6:
                                last = []
                                for i in range(0, starting_index - 1):
                                    last.append(code[i])
                                    print(reservation, "1669")
                                last_n = "".join(
                                    [str(i) for i in last])
                                if self.last_name:
                                    self.write(
                                        {'first_name': self.first_name + " " +
                                                       last_n})

                    if 'E' in list(exact_na[1]):
                        print("hasa", list(exact_na[1]))
                        last_name = []
                        findex = list(exact_na[1])
                        in1 = findex.index('E')
                        ln2 = len(list(exact_na[1]))
                        diff = ln2 - in1
                        print("diff", diff)
                        reverse = findex[::-1]
                        print("shabeer", reverse)

                        if len(reverse) > 6:
                            s_range = findex[-6]
                            print("kumari", s_range)
                            range_start = reverse.index(s_range)
                            print("rangestart", range_start)
                            print("helloooo", findex.index(findex[-6]))
                            r = findex.index(findex[-6])
                            print(r, "kana")
                            if diff > 6:

                                e = list(exact_na[1])
                                print("index", in1)
                                for i in range(0, r + 1):
                                    last = "".join(
                                        [str(i) for i in e[i]])
                                    last_name.append(last)
                                    last_p = "".join(
                                        [str(i) for i in last_name])

                                    self.write({'first_name': last_p})
                                    print(last, "atlastiiii")
                                """WINGO"""
                                reser = []

                                for i in range(0, range_start + 1):
                                    reser.append(reverse[i])
                                    print(reservation, "1997")
                                reservation_code = "".join(
                                    [str(i) for i in reser])
                                print("sundari", reservation_code)
                                if not self.reservation:

                                    if len(list(reservation_code)) == 6:
                                        print(reservation_code, "etttt")
                                        self.write(
                                            {
                                                'reservation': reservation_code[
                                                               ::-1]})
                                    print("hiiiiiiiiiiiiiiii")

                    if not self.first_name:
                        if 'E' not in first_name[i]:
                            if first_name[i] != exact_na[1]:
                                print("fffffffffffffffffffff")
                                last = exact_na[1] + " " + first_name[i]
                                self.write({'first_name': last})

                if not self.reservation:
                    print("lololo")
                    if 'E' in first_name[i]:
                        print("Ewwwww")
                        if first_name[i] != first_name[0]:
                            print("firstname", first_name[0])
                            if length >= 6:
                                print("ana")
                                if first_name[i] != first_name[0]:
                                    findex = first_name[i]
                                    in1 = findex.index('E')
                                    in2 = len(first_name)
                                    in_last = in2 - 6
                                    in_last1 = in2 - 7
                                    print("1", in2)
                                    print("2", in1)
                                    print("5", in_last1)
                                    print(in_last,
                                          "lllllllllpppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp")
                                    reverse = findex[::-1]

                                    print('reverse', reverse)
                                    rev = list(reverse)
                                    inrev = rev.index('E')
                                    print("copico", self.last_name)

                                    if in1 == 0:
                                        if len(first_name[i]) == 6:
                                            if not self.reservation:
                                                self.write(
                                                    {'reservation': first_name[
                                                        i]})
                                        else:
                                            e = list(first_name[i])
                                            print(e, "eeeeee")
                                            res = []

                                            for i in range(in1 + 1, len(e)):
                                                print("jiiii")
                                                res.append(e[i])
                                                reservation_code = "".join(
                                                    [str(i) for i in res])
                                                print('reservation_code',
                                                      reservation_code)
                                                if len(reservation_code) == 6:
                                                    print("qqqqqqqq")
                                                    if not self.reservation:
                                                        self.write(
                                                            {
                                                                'reservation': reservation_code})
                                                    print(reservation, "poi")
                                                else:
                                                    if len(list(
                                                            first_name[
                                                                1])) == 6:
                                                        print("joo")
                                                        if not self.reservation:
                                                            self.write(
                                                                {'reservation':
                                                                     first_name[
                                                                         1]})

                                    else:
                                        reverse = findex[::-1]

                                        print('reverse', reverse)
                                        rev = list(reverse)
                                        inrev = rev.index('E')
                                        print(len(rev))
                                        last_length = len(rev) - inrev

                                        if 'E' in rev:
                                            for i in range(0, inrev):
                                                reservation.append(rev[i])
                                                reservation_code = "".join(
                                                    [str(i) for i in
                                                     reservation])
                                                if len(reservation_code) == 6:
                                                    if not self.reservation:
                                                        self.write(
                                                            {
                                                                'reservation': reservation_code[
                                                                               ::-1]})
                    else:
                        for i in range(len(first_name)):
                            if len(first_name[i]) == 6:
                                self.write({'reservation': first_name[i]})

                            print(reservation, "polo")
                            if len(first_name[i]) >= 6:
                                if 'E' in first_name[i]:
                                    if first_name[i] != first_name[0]:
                                        rev = list(first_name[i])
                                        strt = rev[-6]
                                        start_range = rev.index(strt)
                                        print(strt, "popo")
                                        print("koko", first_name[i])
                                        for i in range(start_range, len(rev)):
                                            reservation.append(rev[i])
                                            reservation_code = "".join(
                                                [str(i) for i in
                                                 reservation])
                                            if len(reservation) == 6:
                                                self.write({
                                                    'reservation': reservation_code})

            list_dest = []
            list_origin = []
            airline = []
            new = []

            for d in range(len(first_name)):
                """flight number"""
                if not self.flight_number:
                    if len(list(first_name[d])) == 4:
                        if (first_name[d].isdigit()):
                            self.write({'flight_number': first_name[d]})
                des = list(first_name[d])

                print("listofreservation", first_name)
                print("ddesss", des)
                if not self.origin:
                    print("llolll", d)
                    if len(list(first_name[d])) == 8:
                        print("456")
                        for i in list(first_name[d]):
                            print('i: ', i)
                            if '/' not in list(first_name[d]):
                                if first_name[d + 1] == self.flight_number:
                                    if len(list_dest) < 3:
                                        print("lobb", list(first_name[d]))
                                        list_dest.append(i)
                                        print("lisstdest", list_dest)
                                        x = "".join([str(i) for i in list_dest])
                                        print(x, "destina")
                                        self.write({
                                            'origin': x})
                                    elif len(list_dest) < 5:
                                        if len(list_origin) < 3:
                                            list_origin.append(i)
                                        y = "".join(
                                            [str(i) for i in list_origin])
                                        print(y, "orgin")
                                        self.write({
                                            # 'origin': x,
                                            'destination': y
                                        })

                                    air_code = list(first_name[d])
                                    print(air_code, "kasav")
                                    airline.append(air_code[-2])
                                    airline.append(air_code[-1])
                                    if len(airline) == 2:
                                        print("rand")
                                        air = "".join([str(i) for i in airline])
                                        airline_nmae = self.env[
                                            'airline.airline'].search(
                                            [('code', 'like', air)])
                                        print("moon,airline_nmae", air)
                                        self.write(
                                            {'airline_id': airline_nmae.id})
                                        print("moon,airline_nmae", airline_nmae)



                    else:
                        print("hoki", len(first_name))
                        if len(first_name) == 5:
                            list_dest.clear()
                            list_origin.clear()
                            h = first_name[1].split('\u200b')
                            print("hhh", h)

                            for_origin = first_name[1].split('\u200b')
                            print('for_origin', for_origin)
                            for i in list(for_origin[-1]):
                                if '/' not in list(for_origin):
                                    if len(list_dest) < 3:
                                        print(list_dest, "ponnazhak")
                                        list_dest.append(i)
                                        x = "".join([str(i) for i in list_dest])
                                        print(x, "xxxxxxxxxxxxxx")
                                    if not self.origin:
                                        if len(list_dest) == 3:
                                            self.write({
                                                'origin': x})
                                    elif len(list_dest) < 5:
                                        if len(list_origin) < 3:
                                            list_origin.append(i)
                                        y = "".join(
                                            [str(i) for i in list_origin])
                                        print(y, "orgin")
                                        if not self.destination:
                                            if len(list_origin) == 3:
                                                self.write({
                                                    # 'origin': x,
                                                    'destination': y
                                                })
                                    air_code = list(for_origin[-1])
                                    print(air_code, "kasav")
                                    airline.append(air_code[-2])
                                    airline.append(air_code[-1])
                                    if len(airline) == 2:
                                        print("onne")
                                        air = "".join([str(i) for i in airline])
                                        airline_nmae = self.env[
                                            'airline.airline'].search(
                                            [('code', '=', air)])
                                        self.write(
                                            {'airline_id': airline_nmae.id})

                """seat number"""
                list_seat = []
                list_date = []
                list_class = []
                # detail = ['R', 'J', 'Y', 'C', 'B', 'A', 'F']
                detail = ['Y', 'R', 'J', 'A', 'C', 'B', 'F']
                for seat in range(len(first_name)):

                    if len(list(first_name[seat])) == 12:
                        if (first_name[seat] != first_name[0]) and first_name[
                            seat] != first_name[1]:
                            ticket = first_name[seat]
                            print(ticket, "lpo")
                            tickt_cls = list(first_name[seat])

                            for t in range(len(ticket)):
                                for i in range(len(detail)):
                                    if not self.cabin_class_id.code:
                                        if ticket[t] == detail[i]:
                                            print("143", ticket[t])

                                            print("resultres", detail[i])

                                            cabin=self.env['cabin.class'].search(
                                                [('code', 'like', detail[i])],limit=1)
                                            self.write(
                                                {'cabin_class_id': cabin.id})
                                            print("143", ticket[t])
                            # list_date=first_name[seat].split(self.ticket)
                            # print("listdate",list_date)
                            # date=datetime.strptime(list_date[0], '%y%j').date()
                            # print("date",date)
                            # self.write({'date_passenger':date})

                            if not self.seat_number:
                                sp = self.cabin_class_id.code
                                seat = ticket.split(sp)
                                print("part1", seat)
                                seat1 = list(seat[1])
                                print(seat1, "77")
                                for sl in range(len(seat1)):

                                    if len(list_seat) < 4:
                                        list_seat.append(seat1[sl])

                                        seat = "".join(
                                            [str(sl) for sl in list_seat])
                                        print('date', seat)
                                        print(list_seat, "llllllllllllllllllll")

                                        listToStr = ' '.join(
                                            map(str, list_seat))

                                        print(listToStr)

                                        self.write({'seat_number': listToStr,
                                                    })
                                if len(seat1) == 3:
                                    self.write({
                                        'seat_number': self.seat_number + " " + self.cabin_class_id.code,
                                    })
                                seat_num_list = list(self.seat_number)
                                if seat_num_list[-1].isdigit():
                                    self.write({'seat_number': ''})

                if '/' not in first_name[0]:
                    last_name_final = []
                    reservation = []
                    print("#############", first_name)
                    for i in range(len(first_name)):
                        if '/' in first_name[i]:
                            print("b", first_name[i])
                            second = first_name[i].split('/')
                            print("second", second)
                            if len(second) == 2:
                                print(",,,,,,,,,,")
                                m = list(first_name[0])
                                for i in range(2):
                                    m.pop(0)
                                    print("kalapani", m)
                                exact_name = "".join([str(i) for i in m])

                                final_name = exact_name + ' ' + second[0]
                                print("lolololol", final_name)
                                self.write({'last_name': final_name})

                            if 'E' in second[1]:
                                print("goo")
                                findex = second[1]
                                last_n = list(findex)
                                reverse = findex[::-1]

                                print('reverse', reverse)
                                rev = list(reverse)
                                inrev = rev.index('E')
                                print(len(rev))

                                for i in range(0, len(rev)):
                                    if len(reservation) <= 5:
                                        reservation.append(rev[i])
                                        print("bololo", reservation)
                                        rv_code = "".join(
                                            [str(i) for i in reservation[::-1]])

                                        self.write(
                                            {
                                                'reservation': rv_code})
                                last_length = len(rev) - 6
                                s_range = findex[-6]
                                print("kumari", s_range)
                                range_start = reverse.index(s_range)
                                print("rangestarting", range_start)
                                print("helloooo0123", findex.index(findex[-6]))
                                r = findex.index(findex[-6])

                                for i in range(0, r - 1):
                                    last_name_final.append(last_n[i])
                                    print("kokokoko", last_name_final)
                                    last = "".join(
                                        [str(i) for i in last_name_final])
                                    print("qooooooooooooo", last)
                                    self.write({'first_name': last})
                            else:
                                self.write({'first_name': second[1]})
                        if 'E' in first_name[i]:
                            if first_name[i] != first_name[0]:
                                print("goo")
                                findex = first_name[i]
                                print(findex, "pito")
                                last_n = list(findex)
                                print("lastn", last_n)
                                if len(last_n) >= 6:
                                    value = last_n[-6]
                                    print(value, "chinna")
                                    strt_range = findex.index(value)
                                    print("indexxxx", strt_range)
                                    reverse = findex[::-1]

                                    print('reverse', reverse)
                                    rev = list(reverse)
                                    inrev = rev.index('E')
                                    print(inrev)
                                    last_length = len(findex) - 6
                                    l = []

                                    for i in range(0, strt_range - 1):
                                        print("kk", last_n[i])

                                        la_name = l.append(last_n[i])
                                        print("kk", la_name)
                                    last = "".join(
                                        [str(i) for i in l])
                                    if last != exact_name:
                                        self.write(
                                            {'last_name': self.last_name + " " +
                                                          last})
                                    print(last_name_final)
                                    reser_code = []
                                    for i in range(strt_range, len(last_n)):
                                        reser_codes = reser_code.append(
                                            last_n[i])
                                    if last_n[-7] == 'E':
                                        if len(reser_code) == 6:
                                            reser = "".join(
                                                str(i) for i in reser_code)
                                            self.write({'reservation': reser})
                word = str(self.airline_id.code)
                print('word', word)
                # txt = ".*" + word
                new.append(first_name[d] if word in first_name[d] else "")
                print("fbjshfiehjlkfs", new)
                place = list(filter(None, new))
            print(place)
            if len(place) == 2:
                print(place[0])
                origin_list = []
                dest_list = []
                new_origin = list(place[0])
                if self.origin:

                    for i in range(0, 3):
                        if len(origin_list) < 4:
                            origin_list.append(new_origin[i])
                    result = "".join(
                        str(i) for i in origin_list)
                    print(origin_list)
                    print(result)
                    self.write({'origin': result})
                    for i in range(3, 6):
                        if len(dest_list) < 4:
                            dest_list.append(new_origin[i])
                    dst = "".join(
                        str(i) for i in dest_list)
                    print(origin_list)
                    print(dst)
                    self.write({'destination': dst})

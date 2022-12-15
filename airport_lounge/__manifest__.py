{
    'name': "Airport Lounge ",
    'depends': ['base','hr','planning'],
    'data': [
        'security/ir.model.access.csv',
        'views/sequence.xml',
        'views/branch_access.xml',
        # 'views/flight.xml',
        'views/airline.xml',
        # 'views/category.xml',
        # 'views/alliance_group.xml',
        # 'views/card_details.xml',
        # 'views/employee_shift.xml',
        # 'views/agencies.xml',
        'views/passenger_details.xml',
        'views/guest_view.xml',
        'views/type_client.xml',
        'views/cabin_class.xml',
        'views/travel_place.xml',
        'views/shower_creation.xml',
        'views/shower_service.xml',
        # 'views/shower_stages.xml'




    ],
    'assets': {
        'web.assets_backend': [

            'airport_lounge/static/js/branch_access.js',
            'airport_lounge/static/xml/access_branch.xml',

        ],

    },
    'installable': True,
    'application': True,
    'auto_install': False,
}

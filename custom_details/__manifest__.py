{
    'name': "Custom Details",
    'depends': ['base', 'hr', 'stock', 'contacts', 'account_accountant'],
    'data': [
        'security/ir.model.access.csv',
        'views/custom_details.xml',
        'views/vendor_details_in_contact.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

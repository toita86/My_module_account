# -*- coding: utf-8 -*-

{
    'name': 'My module account',
    'version': '1.0',
    '0': 'Sales/My module account',
    'summary': 'The best odoo exstension in the world on accounts',
    'depends': ['My_module','account'],
    'data': [
        'security/ir.model.access.csv',

        'views/account_views.xml'
    ]
}
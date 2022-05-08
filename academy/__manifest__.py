# -*- coding: utf-8 -*-
{
    'name': "academy",

    'summary': """academy""",

    'description': """academy
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '1.5',
    'sequence': 1,
    # any module necessary for this one to work correctly
    'depends': ['website','mail','website_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

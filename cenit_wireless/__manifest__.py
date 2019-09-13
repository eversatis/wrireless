# -*- coding: utf-8 -*-
{
    'name': "Cenit Arion Wireless",

    'summary': """
       Cenit Odoo module for Arion-Wireless company integration""",

    'description': """
        This module will integrate Odoo with Backmarket and Shipstation through Cenit Platform, for Orion-Wireless company.
    """,

    'author': "Cenit IO",
    'website': "https://cenit.io/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'cenit_base', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/config.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True
}
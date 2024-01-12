# -*- coding: utf-8 -*-
{
    'name': "Personal-monthly-budget",

    'summary': """
        Maneja tus finanzas personales con esta sencilla app""",

    'description': """
        Lleva el conteo de tus finanzas temporales y te muestra varios dashboard con tu progreso
    """,

    'author': "AlexSnowReDo",
    'website': "https://www.hmmmmmmmm.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '16.0.0.4.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

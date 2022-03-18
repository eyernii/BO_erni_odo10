# -*- coding: utf-8 -*-
{
    'name': "booking_order_erniy_odoo10",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'sales',
    'version': '0.1',
    'installable': True,
    'aplication':True,

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/service_team.xml',
        'views/booking_order.xml',
        'views/work_order.xml',
        'wizard/check_bo_wizard.xml',
        'wizard/cancel_work_order.xml',
        'report/report.xml',
        'report/report_work_order.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
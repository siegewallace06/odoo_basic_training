# -*- coding: utf-8 -*-
{
    'name': "Farid Academy",

    'summary': "Learning Odoo 18",

    'description': """
Long description of module's purpose
    """,

    'author': "Test Company",
    'website': "https://www.testcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/course_data.xml',
        'views/menu.xml',
        'views/course.xml',
        'views/session.xml',
        'views/partner.xml',
        'views/partner_categories.xml',
        'views/views.xml',
        'views/templates.xml',
        # 'reports/inherit_report_sale.xml',
        'views/template_web.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

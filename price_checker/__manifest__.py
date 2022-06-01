# -*- coding: utf-8 -*-
{
    'name': "price_checker",

    'summary': """
        Price checker""",

    'description': """
        Long description of module's purpose
    """,

    'author': "bagus",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # 'depends': ['base'],
      'depends': ['website', 'sale', 'website_payment', 'website_mail', 'website_form', 'website_rating', 'digest'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

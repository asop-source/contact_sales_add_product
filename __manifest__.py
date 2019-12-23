# -*- coding: utf-8 -*-
{
    'name': "Report CRM",

    'summary': """
       Add Report CRM Product
       Add Report Sample Sumary

       """,

    'description': """
        Long description of module's purpose
    """,

    'author': "asopkarawang@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm'],

    # always loaded
    'data': [
        'views/product.xml',
        'views/templates.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
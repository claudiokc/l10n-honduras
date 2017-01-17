# -*- coding: utf-8 -*-
{
    'name': "l10n-honduras",

    'summary': """
        Accounting Localization for 2016 Honduran new tax policies
            - Adding support for CAI, RTN & range of invoces
            - Getting RTN and contributor name from http://enlacertn.dei.gob.hn/consultartn/
            - Adding official list of banks in Honduras
            - New 15 percentage of ISV
        """,

    'description': """
        Hoduras accounting module
    """,

    'author': "Claudio J. Cáceres",
    'website': "http://www.esmeraldalabs.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Localization',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/l10n_hn_chart_data.xml',
        'data/account_chart_template_data.xml',
        'data/account_chart_template_data.yml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
# -*- coding: utf-8 -*-
{
    'name': "SISFO - Módulo de Usuarios",

    'summary': """
        En el presente módulo se manejará toda la sección de usuarios""",

    'description': """
        Este módulo permite mantener el control del registro de los diversos usuarios que van a interactuar con el sistema
    """,

    'author': "tomasa",
    'website': "http://www.sisfo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'SISFO Modulo de Usuarios',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'muk_web_theme'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/registro_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True
}
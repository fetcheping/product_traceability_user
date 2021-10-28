# -*- coding: utf-8 -*-
{
    'name': "User Product Traceability",
    'summary': "This module allows you to know the user who has do a movement on a product",
    'description': """
        this module allows you to know the user who has do a movement on a product
    """,
    'author': "Cabrel Tchomte",
    'website': "http://www.innovations-groups.com",
    'category': 'Inventory',
    'version': '13.0.1.0',
    "license": "LGPL-3",
    'depends': ['stock'],
    'data': ['views/stock_move_line_inherit.xml'],
    'images': ['static/description/traceability_main_screen.png'],
    "installable": True,
    "application": True,
    "auto_install": False,
}

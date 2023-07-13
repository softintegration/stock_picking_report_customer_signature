# -*- coding: utf-8 -*- 


{
    'name': 'Transfer with customer signature in delivery slip',
    'author': 'Soft-integration',
    'application': True,
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'description': False,
    'images': [],
    'version': '1.0.1.1',
    'category': 'Stock',
    'demo': [],
    'depends': ['stock'],
    'data': [
        'views/stock_picking_views.xml',
        'report/report_deliveryslip.xml',
    ],
    'license': 'LGPL-3',
}

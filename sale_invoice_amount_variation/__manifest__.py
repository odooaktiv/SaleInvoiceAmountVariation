# -*- coding: utf-8 -*-
# Part of AktivSoftware See LICENSE file for full copyright and licensing details.
{
    'name': "Sale Invoice Amount Variation",
    'summary': """
        Prints report which shows unit price changed, sale price, difference and the user who has done changes.
       """,
    'author': "Aktiv Software",
    'website': "http://www.aktivsoftware.com",
    'license': "AGPL-3",
    'category': 'web',
    'version': '10.0.1.0.0',
    'depends': ['sale', 'account', 'stock'],
    'data': [
        'views/account_invoice_line_views.xml',
        'views/account_invoice.xml',
        'views/report_invoice.xml'
    ],
    'images': [
        'static/description/banner.jpg',
    ],
    'auto_install': False,
    'installable': True,
    'application': False
}

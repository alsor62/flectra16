# -*- coding: utf-8 -*-
# Part of Odoo, Flectra. See LICENSE file for full copyright and licensing details.

{
    'name': 'Check Printing Base',
    'author': 'Odoo S.A',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Check printing commons',
    'description': """
This module offers the basic functionalities to make payments by printing checks.
It must be used as a dependency for modules that provide country-specific check templates.
The check settings are located in the accounting journals configuration page.
    """,
    'website': 'https://flectrahq.com/page/accounting',
    'depends': ['account'],
    'data': [
        'data/account_check_printing_data.xml',
        'views/account_journal_views.xml',
        'views/account_payment_views.xml',
        'wizard/print_prenumbered_checks_views.xml'
    ],
    'installable': True,
    'auto_install': False,
}

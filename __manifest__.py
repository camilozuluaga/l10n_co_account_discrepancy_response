# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
	'name': 'l10n_co account discrepancy response',
	'version': '1.0',
	'website': '',
	'category': 'Localizacion',
	'summary': 'l10n_co account discrepancy response',
	'description': """
	

	""",
	'depends': [
		'account'
	],
	'data': [
		'data/account_invoice_discrepancy_response_code_data.xml',
		'views/account_invoice_discrepancy_response_code.xml',
		'views/account_invoice.xml',
		'security/ir.model.access.csv',
		
	],
	'installable': True,
	'auto_install': False,
	'application': True,
}

# -*- coding: utf-8 -*-
# Copyright 2018 Simone Rubino - Agile Business Group
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
from odoo import api, fields, models, _
_logger = logging.getLogger(__name__)


class AccountInvoice(models.Model):
   
	_inherit = "account.invoice"

	# Establece por defecto el medio de pago Efectivo
	discrepancy_response_code_id   = fields.Many2one(
		'account.invoice.discrepancy.response.code',
		string='Discrepacy Response',)
	


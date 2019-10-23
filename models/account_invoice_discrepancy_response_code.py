# -*- coding: utf-8 -*-
# Copyright 2018 Simone Rubino - Agile Business Group
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
from odoo import api, fields, models, _
_logger = logging.getLogger(__name__)



class AccountInvoiceDiscrepancyResponseCode(models.Model):


	_name = 'account.invoice.discrepancy.response.code'


	name = fields.Char(string=u'Method')
	code = fields.Char(string=u'Code')
	type = fields.Selection([('in_refund', 'In Refund'),('out_refund', 'Out Refund')], string = 'Type')
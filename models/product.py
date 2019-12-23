# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Crm(models.Model):
		_name	='crm.lead'
		_inherit='crm.lead'

		order_date =fields.One2many('product.lead.line', 'crm_id', string='Product')

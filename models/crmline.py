from odoo import models, fields, api
import datetime

class productCRM(models.Model):
		_name='product.lead.line'

		product_id	=fields.Many2one('product.product', string='Product',required=True)
		product_qty	=fields.Float(string='Quantity', required=True)
		date_planned =fields.Datetime(string='Enquiry Date',required=True )
		crm_id	=fields.Many2one('crm.lead')
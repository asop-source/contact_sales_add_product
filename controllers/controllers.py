# -*- coding: utf-8 -*-
from odoo import http

# class ReportCrm(http.Controller):
#     @http.route('/report_crm/report_crm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_crm/report_crm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_crm.listing', {
#             'root': '/report_crm/report_crm',
#             'objects': http.request.env['report_crm.report_crm'].search([]),
#         })

#     @http.route('/report_crm/report_crm/objects/<model("report_crm.report_crm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_crm.object', {
#             'object': obj
#         })
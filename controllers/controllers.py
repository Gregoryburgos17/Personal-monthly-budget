# -*- coding: utf-8 -*-
# from odoo import http


# class DeveloperTest(http.Controller):
#     @http.route('/Personal_monthly_budget/Personal_monthly_budget', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/Personal_monthly_budget/Personal_monthly_budget/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('Personal_monthly_budget.listing', {
#             'root': '/Personal_monthly_budget/Personal_monthly_budget',
#             'objects': http.request.env['Personal_monthly_budget.Personal_monthly_budget'].search([]),
#         })

#     @http.route('/Personal_monthly_budget/Personal_monthly_budget/objects/<model("Personal_monthly_budget.Personal_monthly_budget"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('Personal_monthly_budget.object', {
#             'object': obj
#         })

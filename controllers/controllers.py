# -*- coding: utf-8 -*-
from odoo import http

# class Escarcha(http.Controller):
#     @http.route('/escarcha/escarcha/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/escarcha/escarcha/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('escarcha.listing', {
#             'root': '/escarcha/escarcha',
#             'objects': http.request.env['escarcha.escarcha'].search([]),
#         })

#     @http.route('/escarcha/escarcha/objects/<model("escarcha.escarcha"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('escarcha.object', {
#             'object': obj
#         })
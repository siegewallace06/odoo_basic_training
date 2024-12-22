# -*- coding: utf-8 -*-
# from odoo import http


# class Faridacademy(http.Controller):
#     @http.route('/faridacademy/faridacademy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/faridacademy/faridacademy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('faridacademy.listing', {
#             'root': '/faridacademy/faridacademy',
#             'objects': http.request.env['faridacademy.faridacademy'].search([]),
#         })

#     @http.route('/faridacademy/faridacademy/objects/<model("faridacademy.faridacademy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('faridacademy.object', {
#             'object': obj
#         })


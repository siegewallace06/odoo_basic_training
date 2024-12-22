# -*- coding: utf-8 -*-
# from odoo import http


# class Faridperpustakaan(http.Controller):
#     @http.route('/faridperpustakaan/faridperpustakaan', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/faridperpustakaan/faridperpustakaan/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('faridperpustakaan.listing', {
#             'root': '/faridperpustakaan/faridperpustakaan',
#             'objects': http.request.env['faridperpustakaan.faridperpustakaan'].search([]),
#         })

#     @http.route('/faridperpustakaan/faridperpustakaan/objects/<model("faridperpustakaan.faridperpustakaan"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('faridperpustakaan.object', {
#             'object': obj
#         })


# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.http import request
import requests


class generate_book(models.TransientModel):
    _name = 'generate.book'

    def act_generate_book(self):
        # import pdb;pdb.set_trace()
        books = requests.get('https://simple-books-api.glitch.me/books').json()
        for book in books:
            vals = {
                'name': book['name'],
                'description': book['type'],
                'total': 10
            }
            self.env['faridperpustakaan.book'].sudo().create(vals)
        # for book in books:
        #     vals = {
        #         'name': book
        #     }

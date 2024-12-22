# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Faridperpustakaan_book(models.Model):
    _name = 'faridperpustakaan.book'
    _description = 'faridperpustakaan.book'

    name = fields.Char()
    total = fields.Float()
    transaction_ids = fields.One2many(
        'faridperpustakaan.transaction', string='Transaction', inverse_name='book_id')
    description = fields.Text()
    available_book = fields.Float(
        'Available Book', compute='count_transaction', store=True)

    @api.depends('transaction_ids', 'total')
    def count_transaction(self):
        for rec in self:
            # import pdb;pdb.set_trace()
            # record_id = rec.ids[0]
            # rec.available_book = rec.total - len(rec.transaction_ids.sudo().search([('book_id','=',record_id),('state','=','progres')]))
            rec.available_book = rec.total - \
                len([x.id for x in rec.transaction_ids if x.state == 'progres'])

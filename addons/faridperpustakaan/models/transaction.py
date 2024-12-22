from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class khaikalperpustakaan_transaction(models.Model):
    _name = 'faridperpustakaan.transaction'
    _description = 'faridperpustakaan.transaction'

    name = fields.Char('Name', required=True, copy=False,
                       readonly=True, index=True, default=lambda self: _('New'))
    tanggal_pinjam = fields.Date('Tanggal Peminjaman', readonly=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('progres', 'Progress'),
        ('done', 'Done')
    ], string='State', default='draft')
    tanggal_kembali = fields.Date('Tanggal Pengembalian', readonly=True)
    book_id = fields.Many2one('faridperpustakaan.book', string='Buku')
    description = fields.Text('Description')
    partner_id = fields.Many2one('res.partner', 'Customer')

    @api.model
    def create(self, vals):
        seq_date = None
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'faridperpustakaan.transaction') or _('New')
        result = super(khaikalperpustakaan_transaction, self).create(vals)
        return result

    # @api.depends('tanggal_pinjam')
    # def change_name(self):
    #     for rec in self:
    #         tr = self.env['faridperpustakaan.transaction'].sudo().search_count([])
    #         if not rec.name:
    #             rec.name = 'Trx-{}-{}'.format(fields.Date.today().month, tr+1)

    def action_confirm(self):
        if self.book_id.available_book > 0:
            self.state = 'progres'
            self.tanggal_pinjam = fields.Date.today()
            self.book_id.count_transaction()
        else:
            raise ValidationError(
                "Stok Buku {} Sedang Tidak Tersedia".format(self.book_id.name))

    def action_done(self):
        self.state = 'done'
        self.tanggal_kembali = fields.Date.today()
        self.book_id.count_transaction()

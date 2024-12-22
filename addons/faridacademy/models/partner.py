from odoo import models, fields, api


class InheritPartner(models.Model):
    _inherit = 'res.partner'

    is_instructor = fields.Boolean(string='Instructor ?')

    session_ids = fields.Many2many('faridacademy.session', string='Sessions')
    partner_category_id = fields.Many2one(
        'res.partner.category', string='Category')

from odoo import models, fields, api


class PartnerCategories(models.Model):
    _name = 'faridacademy.partner_categories'
    _description = 'Partner Categories'

    name = fields.Char(string='Name', required=True)

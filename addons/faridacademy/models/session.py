from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Session(models.Model):
    _name = 'faridacademy.session'

    name = fields.Char('Name', required=True)
    start_date = fields.Date('Start Date', default=fields.Date.today)
    duration = fields.Float('Duration')
    number_of_seats = fields.Float(string='Number Of Seats')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('running', 'Running'),
        ('closed', 'Closed')
    ], default="draft", string='State')
    description = fields.Text('Description')

    def action_confirm(self):
        self.state = 'running'

    def action_done(self):
        self.state = 'closed'

    def action_draft(self):
        self.state = 'draft'

    partner_id = fields.Many2one('res.partner', string='Instructor',
                                 domain="['|',('is_instructor','=',True),('partner_category_id','!=',False)]")
    course_id = fields.Many2one('faridacademy.course', string='Course')
    partner_ids = fields.Many2many('res.partner', string='Attendees')

    taken_seats = fields.Float(
        compute='_compute_taken_seats', string='Taken Seats')
    active = fields.Boolean('Active', default=True)

    @api.depends('number_of_seats', 'partner_ids')
    def _compute_taken_seats(self):
        for rec in self:
            if rec.number_of_seats:
                rec.taken_seats = len(rec.partner_ids) / \
                    rec.number_of_seats * 100
            else:
                rec.taken_seats = 0

    @api.onchange('number_of_seats', 'partner_ids')
    def _onchange_taken_seats(self):
        if self.number_of_seats < 0:
            return {
                'warning': {
                    'title': "Warning",
                    'message': "Number of seats can't be negative",
                }
            }

        if self.number_of_seats < len(self.partner_ids):
            return {
                'warning': {
                    'title': "Warning",
                    'message': "Number of seats can't be less than attendees",
                }
            }

        if self.number_of_seats:
            self.taken_seats = len(self.partner_ids) / \
                self.number_of_seats * 100
        else:
            self.taken_seats = 0

    @api.constrains('partner_ids', 'partner_id')
    def _check_instructor_not_in_attendees(self):
        for rec in self:
            if rec.partner_id in rec.partner_ids:
                raise ValidationError(
                    "Instructor can't be in attendees: {}".format(rec.partner_id.name))

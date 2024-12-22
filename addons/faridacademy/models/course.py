from odoo import models, fields


class Course(models.Model):
    _name = 'faridacademy.course'
    _description = 'Farid Academy Course'

    _sql_constraints = [
        ("name_description_check", "check(name != description)",
         "Name and description must be different"),
        ("name_unique", "unique(name)", "Name must be unique"),
    ]

    name = fields.Char(string='Title', required=True)
    description = fields.Text()

    user_id = fields.Many2one('res.users', string='Responsible User')

    session_ids = fields.One2many(
        comodel_name='faridacademy.session',
        inverse_name='course_id',
        string='Sessions',
    )

    def copy(self, default=None):
        # import pdb;
        # pdb.set_trace()
        # []
        default = dict(default or {})

        # Training Odoo
        # Cari course name nya like Copy of Training odoo
        # 3
        copied_count = self.search_count(
            [('name', '=like', "Copy of {}%".format(self.name))])

        # Kalau tidak ada
        if not copied_count:
            # Copy of training odoo
            new_name = "Copy of {}".format(self.name)

        # # Kalau ada
        else:
            # Copy of training odoo (jumlah ada berapa)
            new_name = "Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Course, self).copy(default)

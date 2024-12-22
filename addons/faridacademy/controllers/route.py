from odoo import http


class RouteAcademy(http.Controller):

    @http.route('/sample', auth='public')
    def sample(self, **kw):
        print("Hello, world")
        return "Hello, world"

    @http.route('/teacher', auth='public')
    def teacher(self, **kw):
        return http.request.render('faridacademy.teacher', {
            'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
        })

    @http.route('/course', auth='public', website=True)
    def course(self, **kw):
        Courses = http.request.env['faridacademy.course'].sudo().search([])
        return http.request.render('faridacademy.course', {
            'courses': Courses,
        })

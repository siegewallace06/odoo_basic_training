from odoo import http


class RouteAcademy(http.Controller):

    @http.route('/academy/<name>/', auth='public', website=True)
    def academy(self, name):
        return '<h1>{}</h1>'.format(name)

    @http.route('/academy/type/<int:id>/', auth='public', website=True)
    def data_type(self, id):
        return '<h1>{} ({})</h1>'.format(id, type(id).__name__)

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

    @http.route('/course/<model("faridacademy.course"):course>/', auth='public', website=True)
    def course_detail(self, course):
        return http.request.render('faridacademy.course_detail', {
            'course': course
        })

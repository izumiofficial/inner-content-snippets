# from odoo import http


# class InnerContent(http.Controller):
#     @http.route('/inner_content/inner_content', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inner_content/inner_content/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('inner_content.listing', {
#             'root': '/inner_content/inner_content',
#             'objects': http.request.env['inner_content.inner_content'].search([]),
#         })

#     @http.route('/inner_content/inner_content/objects/<model("inner_content.inner_content"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inner_content.object', {
#             'object': obj
#         })


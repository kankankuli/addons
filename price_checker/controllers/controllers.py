# -*- coding: utf-8 -*-
# from odoo import http


# class PriceChecker(http.Controller):
#     @http.route('/price_checker/price_checker/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/price_checker/price_checker/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('price_checker.listing', {
#             'root': '/price_checker/price_checker',
#             'objects': http.request.env['price_checker.price_checker'].search([]),
#         })

#     @http.route('/price_checker/price_checker/objects/<model("price_checker.price_checker"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('price_checker.object', {
#             'object': obj
#         })

# -*- coding: utf-8 -*-
from odoo import http

# class L10n-honduras(http.Controller):
#     @http.route('/l10n-honduras/l10n-honduras/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n-honduras/l10n-honduras/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n-honduras.listing', {
#             'root': '/l10n-honduras/l10n-honduras',
#             'objects': http.request.env['l10n-honduras.l10n-honduras'].search([]),
#         })

#     @http.route('/l10n-honduras/l10n-honduras/objects/<model("l10n-honduras.l10n-honduras"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n-honduras.object', {
#             'object': obj
#         })
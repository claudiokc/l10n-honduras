# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResCompany(models.Model):
    _inherit = 'res.company'

    rtn = fields.Char(
        size=14, index=True, help="Tax Identification Number")
    # value2 = fields.Float(compute="_value_pc", store=True)

    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2 = float(self.value) / 100

class ResPartner(models.Model):
    _inherit = 'res.partner'

    rtn = fields.Char(
        size=14, index=True, help="Tax Identification Number")
    # value2 = fields.Float(compute="_value_pc", store=True)

    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2 = float(self.value) / 100
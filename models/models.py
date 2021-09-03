# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ModuleName(models.Model):
    _inherit = 'res.company'

    logo_propyme = fields.Binary(string='Logo ProPyme')


class ModuleName(models.Model):
    _inherit = 'account.invoice.line'

    precio_sin_impto = fields.Char(compute='_compute_precio_sin_impto', string='Precio S/Impto')
    
    @api.depends('quantity','price_unit')
    def _compute_precio_sin_impto(self):
        self.precio_sin_impto= self.price_unit-(self.price_tax/self.quantity)


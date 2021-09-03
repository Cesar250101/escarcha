# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ModuleName(models.Model):
    _inherit = 'res.company'

    logo_propyme = fields.Binary(string='Logo ProPyme')

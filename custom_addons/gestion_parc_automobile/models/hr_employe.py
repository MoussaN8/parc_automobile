from odoo import models, fields

class HrEmployee(models.Model):
    _inherit='hr.employee'

    is_chauffeur=fields.Boolean(string="Chauffeur")

    est_cadre=fields.Selection([
        ('oui','OUI'),
        ('non','NON')
    ],string="Cadre")
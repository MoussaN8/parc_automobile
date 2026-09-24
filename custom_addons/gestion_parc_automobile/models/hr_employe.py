from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    est_cadre = fields.Selection([
        ('oui', 'OUI'),
        ('non', 'NON')
    ], string="Cadre")

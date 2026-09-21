from odoo import models, fields


class ChauffeurReportWizard(models.TransientModel):
    _name = "chauffeur.report.wizard"
    _description = "Rapport Excel des chauffeurs"

    year = fields.Integer(
        string="Année",
        required=True,
        default=lambda self: fields.Date.today().year,
    )

    month = fields.Selection(
        [
            ('1', "JANVIER"),
            ('2', "FEVRIER"),
            ('3', "MARS"),
            ('4', "AVRIL"),
            ('5', "MAI"),
            ('6', "JUIN"),
            ('7', "JUILLET"),
            ('8', "AOUT"),
            ('9', "SEPTEMBRE"),
            ('10', "OCTOBRE"),
            ('11', "NOVEMBRE"),
            ('12', "DECEMBRE"),
        ],
        string="Mois",
        required=True,
        default=lambda self: str(fields.Date.today().month),
    )

    def action_generate_xlsx(self):
        self.ensure_one()

        return self.env.ref(
            'gestion_parc_automobile.action_chauffeur_report_xlsx'
        ).report_action(
            self,
            data={
                'year': self.year,
                'month': self.month,
            }
        )


   
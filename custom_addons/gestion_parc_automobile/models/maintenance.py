from odoo import models, fields

class Maintenance (models.Model):
    _name="parc.maintenance"
    _description="Module qui permet de voir l'historique des réparations"

    name=fields.Char(string="Titre du service",required=True)
    voiture_id=fields.Many2one('parc.voiture',string="Véhicule concerné", required=True,ondelete="cascade")
    type_service=fields.Selection([
        ("preventif","Préventif"),
        ("correctif","Correctif"),
        ("accident","Accident"),
        ("controle_technique","Controle Technique")

    ],string="Type de service",default="preventif",required=True)

    date_service=fields.Date(string="Date de l'intervention",required=True)
    cout_maintenance=fields.Integer(string="Coût de l'intervention",required=True)
    garage_id=fields.Many2one('res.partner',string="Prestaire / Garage exécutant")
    etat=fields.Selection([
        ("brouillon","Brouillon"),
        ("planifie","Planifie"),
        ("termine","Terminé"),
        ("annule","Annulé")
    ],string="Statut maintenance",default="brouillon",required=True)

    description=fields.Text(string="Détails des travaux effectués")

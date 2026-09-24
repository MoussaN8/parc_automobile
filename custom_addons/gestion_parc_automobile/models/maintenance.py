from odoo import models, fields,api
from odoo.exceptions import ValidationError
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

    # Mettre l'etat en brouillon
    def action_brouillon(self):
        for record in self:
            record.etat="brouillon"
            record._update_voiture_statut()


     # Mettre l'etat en planifie
    def action_planifier(self):
        for record in self:
            record.etat="planifie"
            record._update_voiture_statut()     


    # Mettre l'etat en terminé
    def action_marquer_terminer(self):
        for record in self:
            record.etat="termine"
            record._update_voiture_statut()


    # Mettre l'etat en annulé
    def action_annuler(self):
        for record in self:
            record.etat="annule"
            record._update_voiture_statut()

    # --- Méthode Helper de synchronisation ---
    def _update_voiture_statut(self):
        for record in self:
            if not record.voiture_id:
                continue

            if record.etat == 'planifie':
                record.voiture_id.statut = 'maintenance'
            
            elif record.etat in ('termine','annule','brouillon'):
                record.voiture_id.statut = 'disponible'

    # automatiser le statut de la voiture(disponible ou pas ) en fonction de l'état de la maintenance
    # pour faire cela je surcharge les méthode create et write

    # pour dire à odoo que le user peut créer plusieurs enregistrement d'un coup
    @api.model_create_multi
    def create(self,vals_list):
        records=super().create(vals_list)
        records._update_voiture_statut()
        return records

    
    def write(self,vals):
        res=super().write(vals)
        if 'etat' in vals or 'voiture_id' in vals:
            self._update_voiture_statut()
        
        return res


    @api.constrains('cout_maintenance')
    def _check_cout_maintenance(self):
        for record in self:
            if record.cout_maintenance < 0:
                raise ValidationError("Le coût d'une maintenance ne peut pas être négatif !")
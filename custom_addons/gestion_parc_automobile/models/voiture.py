from odoo import models, fields,api

class Voiture(models.Model):
    _name= "parc.voiture"
    _description="Module pour gérer les voitures du parc automobile"

    name=fields.Char(string="Nom court",required=True)
    plaque=fields.Char(string="Plaque d'immatriculation",required=True)
    marque=fields.Char(string="Marque",required=True)
    modele=fields.Char(string="Modèle",required=True)
    # definition de la relation many to one vers chauffeur
    chauffeur_id=fields.Many2one(
        'res.partner',
        string="Employé / chauffeur",
        ondelete=" set null" # Si l'employé est supprimé, le champ devient vide
        )
    kilometrage=fields.Integer(string="Kilométrage",required=True)
    statut=fields.Selection([
        ('disponible','Disponible'),
        ('en_service','En service'),
        ('maintenance','Maintenance'),
        ('rebut','Rebut'),
    ],string="Statut",default='disponible',required=True)
    # historique des réparations 
    maintenance_id=fields.One2Many(
        'parc.maintenance',
        'voiture_id',
        string="Historique réparation",
        ondelete="set null" # Si une historique est  est supprimé, le champ devient vide
        )

    #Coût total des maintenances enregistrées.
    cout_total=fields.Integer(string="Coût total des maintenances",compute="_compute_cout_total",store=True)

    @api.depends("maintenance_id")
    def _compute_cout_total(self):
        for record in self:
            total=sum(line.cout_maintenance for line in record.maintenance_id)
            record.cout_total=total
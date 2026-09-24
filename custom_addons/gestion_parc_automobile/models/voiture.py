from odoo import models, fields,api
from odoo.exceptions import ValidationError
class Voiture(models.Model):
    _name= "parc.voiture"
    _description="Module pour gérer les voitures du parc automobile"

    name=fields.Char(string="Nom court",required=True)
    plaque=fields.Char(string="Plaque d'immatriculation",required=True)
    marque=fields.Char(string="Marque",required=True)
    modele=fields.Char(string="Modèle",required=True)
    # definition de la relation many to one vers chauffeur
    chauffeur_id=fields.Many2one(
        'hr.employee',
        string="Employé / chauffeur",
        ondelete="set null" # Si l'employé est supprimé, le champ devient vide
        )
    kilometrage=fields.Integer(string="Kilométrage",required=True)
    statut=fields.Selection([
        ('disponible','Disponible'),
        ('en_service','En service'),
        ('maintenance','Maintenance'),
        ('rebut','Rebut'),
    ],string="Statut",default='disponible',required=True)
    # historique des réparations 
    maintenance_ids=fields.One2many(
        'parc.maintenance',
        'voiture_id',
        string="Historique réparation",
        )

    #Coût total des maintenances enregistrées.
    cout_total=fields.Integer(string="Coût total des maintenances",compute="_compute_cout_total",store=True)

    maintenance_count=fields.Integer(string="Nombre maintenances",compute="_compute_nombre_maintenance")

    @api.depends("maintenance_ids.cout_maintenance")
    def _compute_cout_total(self):
        for record in self:
            total=sum(line.cout_maintenance for line in record.maintenance_ids)
            record.cout_total=total


    @api.depends("maintenance_ids")
    def _compute_nombre_maintenance(self):
        for record in self:
            record.maintenance_count=len(record.maintenance_ids)


    def action_afficher_stats(self):
        #sécurité vérifier que self ne contient qu'un seul enregistrement au lieu de faire planter le serveur
        #en mélangeant les données
        self.ensure_one()
        return{
            'type':'ir.actions.act_window', #ouvrir une fenêtre odoo
            'name': "Maintenances", #Nom de cette fenêtre
            'res_model':"parc.maintenance",
            'view_mode':'list,form', #ouvrir d'abord la liste des maintenances (list) puis si on clique sur l'une ouvrir le form
            'domain':[('voiture_id','=',self.id)], #on veut afficher que les maintenances liées au voiture actuelle
            'context':{'default_voiture_id':self.id},
            #Le dictionnaire context est un outil d'Odoo qui permet de passer des paramètres et des données "en arrière-plan" d'une vue à une autre.
            # Le préfixe default_ est un mot-clé dans Odoo: Lorsque vous cliquez sur le bouton, Odoo ouvre la liste des maintenances. 
            # Grâce à cette ligne, si l'utilisateur clique sur le bouton "Nouveau" (Créer) depuis cette liste, Odoo va lire le contexte, 
            # intercepter le default_voiture_id et remplir automatiquement le champ voiture_id avec la voiture d'où vous venez.
            # Le bénéfice : L'utilisateur n'a pas besoin de chercher et de resélectionner la voiture manuellement dans le formulaire de maintenance. 
            # Cela évite les erreurs de saisie et fait gagner du temps.
        }

    @api.constrains("statut","maintenance_ids")
    def _check_statut_disponible(self):
        for record in self:
            # Si l'utilisateur essaie de passer le véhicule en "disponible"
            if record.statut == 'disponible':
                # On cherche si au moins une maintenance est en état 'brouillon' ou 'planifie'
                maintenances_en_cours = record.maintenance_ids.filtered(
                    # je créé une fonction anonyme lambda
                    lambda m: m.etat in ('brouillon','planifie')
                )
                if maintenances_en_cours:
                    raise ValidationError("Impossible de passer le véhicule en 'Disponible :"
                        "une ou plusieurs maintenances sont encore en cours ou planifiées.")
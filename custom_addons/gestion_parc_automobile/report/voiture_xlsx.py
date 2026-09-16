#on importe la bibliothéque qui permet de créer des fichiers excel
import xlsxwriter
from odoo import models

# le modéle odoo qui représente notre générateur de rapport
class RapportVoitureXlsx(models.AbstractModel):
    _name = "report.gestion_parc_automobile.rapport_voiture_xlsx"
    _inherit="report.report_xlsx.abstract"

    #la fonction principale appelée par Odoo au moment où l'utilisateur clique sur le bouton d'impression.
    # workbook : Représente le fichier Excel global en cours de création.
    # data : Un dictionnaire contenant les paramètres ou filtres envoyés depuis un éventuel assistant (wizard)
    #voitures : La liste des enregistrements (ici, vos voitures parc.voiture) que l'utilisateur a sélectionnés à l'écran pour générer le rapport.
    #self : Contient l'environnement technique d'Odoo (l'accès à la base de données via self.env, les droits de l'utilisateur, etc.).
    def generate_xlsx_report(self,workbook,data,voitures):
        #Cette ligne crée un nouvel onglet (une feuille de calcul) à l'intérieur du fichier Excel et le nomme "Fiche véhicule".
        worksheet = workbook.add_worksheet("Fiche véhicule")

        for voiture in voitures:
            #je créé une feuille excel
            sheet = workbook.add_worksheet(f"Voiture {voiture.name}")

            # je définit les formats ou styles

            titre= workbook.add_format({
                "bold":True,
                "font_size":16,
                "align":"center",
                
            })

            entete=workbook.add_format({
                "bold":True,
                "border":1
            })

            cellule=workbook.add_format({
                "border":1
            })

            # je définis le titre
            sheet.merge_range(
                "A1:B1",
                "Fiche de la Voiture",
                titre
            )

            #informations de la voiture
            lignes=[
                ("Nom court",voiture.name),
                ("Plaque d'immatriculation",voiture.plaque),
                ("Marque",voiture.marque),
                ('Modèle',voiture.modele),
                ("Chauffeur",voiture.chauffeur_id.name if voiture.chauffeur_id else ""),
                ("Kilométrage",voiture.kilometrage),
                ("Statut",'voiture.statut'),
                ("Nombre de maintenances",voiture.maintenance_count),
                ("Coût total des maintenances",voiture.cout_total)
            ]

            # je définis la ligne à laquelle je commence à remplir les cellules
            row = 2
            # je décompose le tuple
            for label, valeur in lignes:
                sheet.write(row,0,label,entete)
                sheet.write(row,1,valeur,cellule)
                row+=1
            # je définis la largeur des colonnes
            sheet.set_column("A:A",30),
            sheet.set_column("B:B",40)
        



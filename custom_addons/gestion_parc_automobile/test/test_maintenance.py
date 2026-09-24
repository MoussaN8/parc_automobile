from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestParcMaintenance(TransactionCase):

    def setUp(self):
        super(TestParcMaintenance, self).setUp()
        # Création des données de test
        self.voiture = self.env['parc.voiture'].create({
            'name': 'Peugeot 208 Test',
            'plaque': 'DK-1234-AA',
            'statut': 'disponible'
        })
        
        self.maintenance = self.env['parc.maintenance'].create({
            'name': 'Vidange Vidange',
            'voiture_id': self.voiture.id,
            'type_service': 'preventif',
            'date_service': '2026-09-01',
            'cout_maintenance': 50000,
            'etat': 'brouillon'
        })

    def test_01_synchronisation_statut_voiture(self):
        """ Vérifie que le statut de la voiture passe en 'maintenance' quand la maintenance est planifiée """
        self.maintenance.action_planifier()
        self.assertEqual(self.voiture.statut, 'maintenance', "La voiture devrait être marquée en maintenance.")

        self.maintenance.action_marquer_terminer()
        self.assertEqual(self.voiture.statut, 'disponible', "La voiture devrait repasser en disponible une fois la maintenance terminée.")

    def test_02_contrainte_cout_negatif(self):
        """ Vérifie qu'un coût négatif lève bien une ValidationError """
        with self.assertRaises(ValidationError):
            self.env['parc.maintenance'].create({
                'name': 'Test Erreur Coût',
                'voiture_id': self.voiture.id,
                'date_service': '2026-09-01',
                'cout_maintenance': -10000,
            })
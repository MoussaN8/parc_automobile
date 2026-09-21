# -*- coding: utf-8 -*-
{
    'name': 'Système de Gestion de Parc Automobile',
    'version': '1.0',
    'summary': "Module permettant aux entreprises de superviser, d'organiser et d'optimiser l'utilisation de leurs véhicules.",
    'category': 'Human Resources/Fleet',
    'author': 'Moussa Ndiaye',
    'depends': ['base','contacts','report_xlsx','hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/voiture_views.xml',
        'views/maintenance_views.xml',
        'views/res_partner_views.xml',
        'wizard/chauffeur_report_wizard_views.xml',
        'views/menu_view.xml',
    
        'rapports/parc_layout.xml',
        'rapports/voiture_rapport_template.xml',
        'rapports/voiture_rapport.xml',
        'report/voiture_xlsx.xml',
        'report/chauffeur_xlsx.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
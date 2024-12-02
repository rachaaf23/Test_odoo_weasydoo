{
    'name': 'Contact Travel',
    'version': '1.0',
    'summary': 'Gestion des voyages associés aux contacts',
    'description': 'Un module pour gérer les informations de voyage des contacts.',
    'author': 'Racha',
    'category': 'Custom',
    'depends': ['base', 'contacts'],  # Ajout de dépendance au module "contacts"
    'data': [
            
        'security/ir.model.access.csv',
        'views/voyage_views.xml',
        'actions.xml',  # Les vues pour le modèle "Voyage"
    ],
    'installable': True,
    'application': True,
}

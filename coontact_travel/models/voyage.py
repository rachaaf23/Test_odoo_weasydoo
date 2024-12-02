from odoo import models, fields

class Voyage(models.Model):
    _name = 'voyage'
    _description = 'Modèle pour gérer les informations de voyage'

    name = fields.Char(string='Nom du Voyage', required=True)
    departure_date = fields.Date(string='Date de Départ', required=True)
    destination = fields.Char(string='Destination', required=True)
    contact_id = fields.Many2one('res.partner', string='Contact Associé')

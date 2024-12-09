# Module Odoo : contact_travel

Ce document décrit le module Odoo `contact_travel` créé dans le cadre du test technique pour le poste de développeur junior Odoo. Le module a pour objectif d'ajouter un bouton intelligent aux utilisateurs pour accéder à leurs voyages, ainsi que d'autres fonctionnalités décrites ci-dessous.

## Fonctionnalités Implémentées

### 1. Création du Module Odoo
- Nom du module : **contact_travel**
- Initialisation du module avec la structure standard d'Odoo.

### 2. Modèle "Voyage"
- Création d'un modèle nommé `Voyage` pour gérer les informations sur les voyages :
  - **Champs principaux** :
    - `name` : Nom du voyage (type Char).
    - `departure_date` : Date de départ (type Date).
    - `destination` : Destination (type Char).
  - Relation Many2one avec `res.partner` pour associer un voyage à un utilisateur.

### 3. Bouton Intelligent
- Ajout d'un bouton intelligent dans la vue formulaire des utilisateurs (`res.partner`).
- Le bouton redirige vers une vue liste des voyages associés à l'utilisateur.

### 4. Calcul du Nombre de Voyages
- Le libellé du bouton intelligent affiche le nombre total de voyages associés à l'utilisateur.

### 5. Gestion des Niveaux de Récompense
- Ajout d'un champ `reward_level` au modèle `res.partner` :
  - Type : Sélection.
  - Valeurs possibles : Argent, Or, Platine.
- Implémentation de règles métier pour définir le niveau de récompense en fonction des voyages d'un utilisateur.
- Fonctionnalité de calcul automatique du niveau de récompense mise à jour lors de l'ajout ou de la modification des voyages associés.

### 6. Tests du Module
- Installation et test du module sur une instance Odoo locale.
- Création d'utilisateurs et association de voyages.
- Vérification de l'affichage des voyages et du calcul des niveaux de récompense.

## Fonctionnalités Non Terminées
- **Calcul automatique du niveau de récompense** : Non finalisé.
- **Bouton intelligent** : Configuration incomplète pour rediriger vers la vue des voyages.

## Instructions pour l'Installation
1. Clonez le dépôt :
  
2. Placez le dossier `contact_travel` dans le répertoire `addons` d'Odoo.
3. Redémarrez le serveur Odoo :
  
4. Installez le module à partir de l'interface Odoo.

## Structure du Dépôt
- **models/** : Contient les définitions de modèles (`voyage.py`).
- **views/** : Contient les fichiers XML pour les vues.
- **__init__.py** et **__manifest__.py** : Fichiers d'initialisation et de description du module.


## Limitations
- Le bouton intelligent n'est pas complètement fonctionnel.
- Les règles métier pour les niveaux de récompense nécessitent des ajustements.

## Améliorations Futures
- Finaliser le calcul automatique des niveaux de récompense.
- Compléter la configuration et le test du bouton intelligent.
- Ajouter plus de tests unitaires et fonctionnels.


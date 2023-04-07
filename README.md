# Olist
Piloter la stratégie marketing

# Mise en place du projet

## Env
`python -m virtualenv .env`

## Activier l'environnement
`.\.env\Scripts\activate`

## Install packages
`pip install -r requirements.txt`

## Faire une migration de la bdd
`py manage.py migrate`

## Démarrer le serveur
`python manage.py runserver`

## Import des données
Télécharger les fichiers [CSV sur Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce?select=olist_orders_dataset.csv) et mettre les fichiers extraîts dans script/data (exemple de path : ./script/data/olist_sellers_dataset.csv)

### Méthodes d'import de la bdd
- Méthode 1: Chaque fichier jupiter dans script est numéroté de 1 et 7. Il faut lancer le code des fichiers dans l'ordre afin d'importer les données en bdd.
- Méthode 2 : Lancer le code contenu dans BDD après avoir paramétré l'accès à la base de donnée initialement.

# Data base 

'NAME': 'olist',  
'USER': 'postgres',  
'PASSWORD': '0000',  
'HOST': '127.0.0.1',  
'PORT': '5432',  

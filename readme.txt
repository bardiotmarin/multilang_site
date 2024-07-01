
Ce fichier README fournit des instructions pour télécharger, configurer, et déployer l'application multilingue basée sur Django, ainsi que des explications sur l'utilisation du chatbot et la fonctionnalité RAG intégrés.

 ------ Téléchargement du Projet ------
Pour télécharger le projet à partir de GitHub et l'installer localement, suivez ces étapes :

Cloner le projet depuis GitHub :


git clone https://github.com/bardiotmarin/multilang_site.git


Configuration de l'environnement virtuel :
python -m venv env
source env/bin/activate  # Sous Windows, utilisez env\Scripts\activate


Installation des dépendances :
pip install -r requirements.txt
Configuration des Clés API dans l'Environnement
Pour gérer les clés d'API de manière sécurisée, rennomer le ficher ENV.example en .env et repmplisez avec vos clef api comme ceci :

 ------ clef api ------
# Exemple de clé d'API
SECRET_KEY="votre_secret_key_ici"

pour que le code fonctionne il vous faut une clef api de chez : 


SERPAPI_API
GOOGLE_API
UNSPLASH_ACCESS_KEY
et l'url de votre bdd

Dans votre code Django, accédez à ces variables d'environnement ainsi :

import os

secret_key = os.getenv('SECRET_KEY')


Installation des dépendances : demarage serv

 ------ Mise en Production ------
Pour déployer l'application en production, vous pouvez utiliser des services comme Render.com ou tout autre service d'hébergement Django. Assurez-vous d'avoir configuré vos variables d'environnement sur le serveur de production pour la sécurité.

Bien vérifier que vous etes

Préparation du déploiement :
python manage.py collectstatic

Déployer sur Render.com :
Créez un nouveau site sur Render.com.
Utilisez GitHub pour connecter votre dépôt.
Configurez les variables d'environnement dans les paramètres du projet sur Render.com.
Configuration des variables d'environnement sur Render.com :

Ajoutez les clés d'API et autres configurations spécifiques à votre environnement de production dans les paramètres du projet Render.com.

-------  Fonctionnement du Projet et du Chatbot   ------
Fonctionnalités de Base

Modèles et Vues :
Utilisation de Django pour gérer les articles de blog.
Modèles comme Article avec les champs title, content, et publication_date.

Internationalisation (i18n) :
Configuration pour supporter au moins deux langues (français et anglais).
Traduction des éléments

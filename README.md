# XML-Project

Description

Le projet XML est une initiative visant à développer une solution innovante pour une interface de cinema.

Architecture

Le projet suit une architecture modulaire et évolutive permettant de s'adapter aux besoins futurs. Les principaux composants sont :

Frontend

Technologie : Vuejs

Objectif : Fournir une interface utilisateur intuitive et réactive.

Dépendances clés : voir dependances

Backend

Technologie : python

Objectif : Gérer la logique métier et assurer la communication avec la base de données.

Dépendances clés : voir requirements.txt

Base de données

Type : JSON

Objectif : Stocker et gérer les données de manière efficace.

API

Protocole : REST

Objectif : Offrir un moyen standard d'intéragir avec les données et les services.

Endpoints principaux : /cinemas


Installation

Cloner le dépôt :

git clone [https://github.com/7ntys/XML-Project]

Installer les dépendances :

Frontend :

cd frontend
npm install

Backend :

cd backend
pip install -r requirements.txt

Configurer les variables d'environnement :

Créer un fichier .env à la racine des répertoires frontend et backend.

Ajouter les clés et valeurs nécessaires selon env.example.

Lancer l'application :

Frontend :

npm start

Backend :

python manage.py runserver

Tests

Frontend :

npm test

Backend :

uvicorn backend:app --reload

Contribuer

Forkez le dépôt.

Créez une branche pour votre fonctionnalité :

git checkout -b PRENOM/nouvelle-fonctionnalite

Faites vos modifications et committez-les :

git commit -m "Ajout d'une nouvelle fonctionnalité"

Poussez vos modifications :

git push origin feature/nouvelle-fonctionnalite

Créez une Pull Request.

Licence


Pour toute question ou problème, veuillez contacter [votre adresse email ou un canal de support].
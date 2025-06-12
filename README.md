# Gestion d'évènements

## Mode d'accès

Application Web

## Fonctionnalités

* Créer un évènement (title)
* Un évènement gratuit ou payant
* Un évènement a une limite de participants
* S'inscrire à un évènement


## Architecture

* Serveur d'application pour Python : Flask
* ORM : SQLAlchemy
* Base de données : PostgreSQL
* Micro-Service de paiement
* Communication entre le serveur d'application et le micro-service de paiement utilise gRPC avec le protocole ProtoBuf


## Tests

Tests de navigation :

* Selenium avec déploiement et utilisation de Selenium Grid

Tests de performance :

* k6 par Grafana Labs
* JMeter par la fondation Apache

Intégrer les tests dans un pipeline Jenkins

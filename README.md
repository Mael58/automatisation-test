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

### Selenium navigateurs

[Télécharger Chrome et ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/)

## GRPC

commande pour générer les fichiers Python à partir du fichier proto

se positionner à la racine du projet global

```bash
python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. models/payment.proto
```

### Tests de performance

Exécuter des tests de performance avec K6

```bash
docker run --rm -u $(id -u) -e K6_WEB_DASHBOARD=true -e K6_WEB_DASHBOARD_EXPORT=html-report.html -v $PWD:/app -w /app -p 5665:5665 grafana/k6 run /app/script.js
```

### Coverage 

Lancer le test de couverture du projet 
```bash
coverage run -m pytest
```

Pour avoir un rendu directement dans le terminal

```bash
coverage report
```
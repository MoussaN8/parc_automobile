# 🚗 Odoo 19 Fleet Management (`parc_automobile`)

[![CI/CD Pipeline](https://github.com/votre-username/odoo-automobile/actions/workflows/ci.yml/badge.svg)](https://github.com/votre-username/odoo-automobile/actions)
[![Docker Image](https://img.shields.io/badge/Docker%20Hub-moussan8%2Fodoo--parc--app-blue)](https://hub.docker.com/r/moussan8/odoo-parc-app)
[![Odoo Version](https://img.shields.io/badge/Odoo-19.0-purple.svg)](https://www.odoo.com/)

Module sur mesure pour la gestion et le suivi d'un parc automobile d'entreprise sous **Odoo 19**. Ce projet intègre une architecture complète orientée qualité avec conteneurisation Docker et automatisation CI/CD via GitHub Actions.

---

## 📋 Fonctionnalités du Module

- **Gestion des Véhicules (`parc.voiture`)** : Suivi des détails techniques, immatriculations, modèles et états de la flotte.
- **Suivi des Maintenances (`parc.maintenance`)** : Planification et historique des révisions, vidanges et réparations.
- **Intégration RH (`hr.employee`)** : Affectation des véhicules aux employés de l'entreprise.
- **Vues Personnalisées** : Interface utilisateur enrichie avec vues Kanban stylisées, Formulaires dynamiques et Graphiques d'analyse.
- **Sécurité et Règles d'Accès** : Gestion fine des droits utilisateur via `ir.model.access.csv`.

---

## 🛠️ Stack Technique & Dépendances

- **ERP** : Odoo 19.0
- **Langage** : Python 3.12+ / JavaScript
- **Base de données** : PostgreSQL 16/17
- **Dépendances Python** : `xlsxwriter` (export de rapports)
- **DevOps** : Docker, Docker Compose, GitHub Actions (CI/CD)

---

## 🚀 Installation & Lancement en Local

### Prérequis
- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/) & Docker Compose

### 1. Cloner le dépôt
```bash
git clone https://github.com/MoussaN8/parc_automobile.git

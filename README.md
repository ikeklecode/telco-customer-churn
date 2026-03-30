# 📉 Prédiction d'Attrition Client (Telco Churn End-to-End Project)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=sqlite&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-XGBoost-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![PowerBI](https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=Power%20BI&logoColor=black)

## 📌 Contexte du Projet
Dans le secteur des télécommunications, le coût d'acquisition d'un nouveau client est largement supérieur au coût de rétention. J'ai conçu ce projet analytique de bout en bout pour identifier les "signaux faibles" de résiliation et automatiser la détection des clients à risque via l'Intelligence Artificielle.

**Objectif Business :** Maximiser la détection des clients sur le départ (Recall) pour cibler les offres de rétention, tout en comprenant les facteurs de friction majeurs (prix, services, ancienneté).

## 🏗️ Architecture du Projet
Le projet est divisé en 4 grandes étapes techniques, consultables dans les dossiers associés :

1. **Extraction & Requêtage (SQL) :** Création d'une base de données locale (`SQLite`) et requêtes analytiques sur les profils des fuyards et les types de contrats.
2. **Exploration & Dataviz (Python / EDA) :** Analyse de la distribution et profilage avec `Pandas`, `Matplotlib` et `Seaborn`.
3. **Machine Learning & XAI (XGBoost & SHAP) :** Entraînement de modèles de classification et explicabilité des décisions de l'algorithme.
4. **Dashboard Business (PowerBI) :** *[En cours de construction]* Restitution visuelle et suivi du risque pour les équipes opérationnelles.

## 🚀 Résultats de la Modélisation (Machine Learning)

Le principal défi de ce projet était le **déséquilibre des classes** (environ 73 % de fidèles pour 27 % de départs). 

* **Baseline (XGBoost standard) :** Incapacité à détecter suffisamment de fuyards (Recall = 53%). L'algorithme laissait passer près de la moitié des résiliations.
* **Optimisation Technique (Scale Pos Weight) :** Ajustement des poids de l'algorithme pour pénaliser lourdement les faux négatifs, forçant le modèle à se concentrer sur la détection du churn.
* **Optimisation Métier (Explainable AI) :** Utilisation des valeurs `SHAP` pour ouvrir la "boîte noire" de l'IA et prouver au métier que le type de contrat (mensuel) et l'ancienneté sont les premiers facteurs de départ.

### 📊 Performance Finale
Grâce à l'ajustement de la pondération, le modèle agit désormais comme un radar ultra-sensible :
- **Taux de détection (Recall Churn) :** **80 %** - **Impact Métier :** Le modèle permet d'identifier la grande majorité des clients sur le départ, permettant au service fidélisation de proposer des réductions ciblées avant que la résiliation ne soit effective (ce qui coûte moins cher que de perdre l'abonnement complet).

## 📂 Structure du Repository
- `/data` : Données brutes, prédictions exportées et base de données (ignorées sur Git).
- `/notebooks` : 
  - `01_setup_db.py` : Script d'initialisation de la base SQLite.
  - `02_SQL_Exploration.ipynb` : Requêtage SQL et analyse de cohorte.
  - `03_EDA_Visualisation.ipynb` : Data Cleaning & Analyse Exploratoire visuelle.
  - `04_Machine_Learning.ipynb` : Modélisation XGBoost, analyse SHAP & export.
- `/dashboard` : Livrables PowerBI *[À venir]*.

## 📊 Tableau de Bord Exécutif (Power BI)
*[Section à venir : Intégration du dashboard interactif orienté "Rétention Client"]*

---
*👤 Projet réalisé par **Ilyes H** | Data Analyst Junior | Disponible immédiatement.*
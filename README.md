# NYC Taxi Spark Project

Ce projet montre un pipeline Spark complet pour l’ingestion, le nettoyage, la transformation, l’optimisation et l’analyse de données NYC Taxi.

## Structure du projet

- `src/ingestion.py` : ingestion de jeux de données Parquet depuis le service NYC Taxi.
- `src/cleaning.py` : nettoyage des trajets, suppression des valeurs invalides et calcul de la durée.
- `src/feature_engineering.py` : génération de nouvelles colonnes utiles pour l’analyse et le machine learning.
- `src/optimization.py` : optimisation simple de DataFrame Spark pour le cache et le partitionnement.
- `src/analytics.py` : fonctions d’analyse comme le chiffre d’affaires horaire, les zones de prise en charge et les pourcentages de pourboire.
- `src/ml.py` : préparation des données et entraînement d’un modèle de régression linéaire pour prédire le montant total.
- `src/visualization.py` : génération d’une visualisation métier destinée à un recruteur.

## Comment exécuter

1. Créer un environnement virtuel Python :
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

2. Exécuter le pipeline principal :
   ```powershell
   python src\main.py
   ```

3. Générer la visualisation des résultats :
   ```powershell
   python src\visualization.py
   ```

## Visualisation

La visualisation produira un fichier image `reports/spark_taxi_insights.png` contenant :

- la répartition du chiffre d’affaires total par heure de prise en charge
- le pourcentage moyen de pourboire par heure de prise en charge

Cette visualisation est utile pour présenter un projet à un recruteur, car elle réunit à la fois une métrique business et une métrique d’expérience client.

## Points forts

- Pipeline Spark end-to-end
- Nettoyage des données et contrôle des valeurs aberrantes
- Feature engineering sur les trajets taxi
- Optimisation Spark simple mais efficace
- Visualisation métier orientée business
- Possibilité d’extension vers le machine learning

## Remarques

- Le projet télécharge automatiquement le fichier `yellow_tripdata_2023-01.parquet` dans `data/raw` si nécessaire.
- Le fichier de données volumineux n’est pas inclus dans le dépôt Git.

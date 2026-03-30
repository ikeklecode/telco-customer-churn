import sqlite3
import pandas as pd

# 1. Définir les chemins
csv_file = 'data/telco_churn.csv'
db_file = 'telco_churn.db'

# 2. Lire le CSV avec Pandas
print("Lecture du fichier CSV...")
df = pd.read_csv(csv_file)

# 3. Nettoyage très rapide (les espaces dans le texte posent souvent problème)
# On remplace les espaces vides par des NaN (valeurs nulles) dans la colonne TotalCharges
df['TotalCharges'] = df['TotalCharges'].replace(" ", None)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'])

# 4. Connexion à SQLite et création de la base
print("Création de la base de données SQLite...")
conn = sqlite3.connect(db_file)

# 5. Envoi des données dans la base SQL
df.to_sql('customers', conn, if_exists='replace', index=False)

print(f"Succès ! La base de données '{db_file}' a été créée avec {len(df)} lignes.")

conn.close()
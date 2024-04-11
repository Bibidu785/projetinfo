import mysql.connector
from faker import Faker

# Se connecter à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Utopie39*",
    database="projetinfo"
)
cursor = conn.cursor()

# Supprimer toutes les lignes de la table Professeurs
cursor.execute("DELETE FROM Professeurs")

# Création d'un générateur de données aléatoires
fake = Faker()

# Préparation de la requête SQL pour insérer une nouvelle ligne
requete = "INSERT INTO Professeurs (Nom, Prenom) VALUES (%s, %s)"

# Boucle pour insérer 25 nouvelles lignes dans la table
for i in range(25):
    # Génération de données aléatoires
    nom = fake.last_name()
    prenom = fake.first_name()

    # Données à insérer
    donnees = (nom, prenom)

    # Exécution de la requête SQL avec les données spécifiées
    cursor.execute(requete, donnees)

# Validation de la transaction pour enregistrer les données dans la base de données
conn.commit()

# Exécution d'une requête SQL pour sélectionner toutes les lignes de la table
cursor.execute("SELECT * FROM Professeurs")

# Récupération des résultats de la requête
resultats = cursor.fetchall()

# Affichage des résultats
for row in resultats:
    print(row)

# Fermeture de la connexion à la base de données
cursor.close()
conn.close()
print("Connexion à la base de données fermée.")

import mysql.connector
import random

# Se connecter à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mdp",
    database="projetinfo"
)
cursor = conn.cursor()

# Boucle pour insérer les données dans la table
for i in range(ord('A'), ord('H')):
    # Préparation de la requête SQL pour insérer une nouvelle ligne
    requete = "INSERT INTO Salles (Nom, Capacite) VALUES (%s, %s)"

    # Données à insérer
    nom = f"Amphi {chr(i)}"
    capacite = random.randint(100, 500)

    # Exécution de la requête SQL avec les données spécifiées
    cursor.execute(requete, (nom, capacite))

for j in range(100, 601, 100):
    for i in range(j, j+11):
        # Préparation de la requête SQL pour insérer une nouvelle ligne
        requete = "INSERT INTO Salles (Nom, Capacite) VALUES (%s, %s)"

        # Données à insérer
        nom = f"Salle {i}"
        capacite = random.randint(25, 50)

        # Exécution de la requête SQL avec les données spécifiées
        cursor.execute(requete, (nom, capacite))

# Validation de la transaction pour enregistrer les données dans la base de données
conn.commit()

# Récupération des données de la table
requete = "SELECT * FROM Salles"
cursor.execute(requete)
resultats = cursor.fetchall()

# Affichage des données de la table
print("Contenu de la table Salles :")
for row in resultats:
    print(row)

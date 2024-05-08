import mysql.connector
import random

# Se connecter à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MDP",
    database="projetinfo"
)
cursor = conn.cursor()

# Générer aléatoirement les disponibilités pour chaque salle
def generate_disponibilites_salle():
    jours_semaine = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']
    heures_travail = ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"]

    disponibilites = []

    for jour in jours_semaine:
        for id_salle in range(1, 74):  # Supposons qu'il y ait 73 salles
            # Génération aléatoire des heures de début et de fin
            heure_debut = random.choice(heures_travail)
            heure_fin = random.choice(heures_travail[heures_travail.index(heure_debut):])

            # Ajout de la disponibilité à la liste
            disponibilites.append((id_salle, jour, heure_debut, heure_fin))

    return disponibilites

# Préparation de la requête SQL pour insérer une nouvelle ligne dans la table Disponibilites_salle
requete_disponibilites_salle = "INSERT INTO Disponibilites_salle (ID_Salle, JourSemaine, HeureDebut, HeureFin) VALUES (%s, %s, %s, %s)"

# Générer aléatoirement les disponibilités pour chaque salle et les insérer dans la base de données
disponibilites_salle = generate_disponibilites_salle()
cursor.executemany(requete_disponibilites_salle, disponibilites_salle)

# Validation de la transaction pour enregistrer les données dans la base de données
conn.commit()

# Exécution d'une requête SQL pour récupérer toutes les disponibilités des salles
requete = "SELECT * FROM Disponibilites_salle"
cursor.execute(requete)

# Récupération des résultats de la requête
resultats = cursor.fetchall()

# Affichage de toutes les disponibilités des salles
print("Liste de toutes les disponibilités des salles :")
for disponibilite in resultats:
    print(f"Salle {disponibilite[1]}, Jour: {disponibilite[2]}, Heure de début: {disponibilite[3]}, Heure de fin: {disponibilite[4]}")

# Fermeture de la connexion à la base de données
cursor.close()
conn.close()

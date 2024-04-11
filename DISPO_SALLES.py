import mysql.connector
import random

# Se connecter à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Utopie39*",
    database="projetinfo"
)
cursor = conn.cursor()

# Générer aléatoirement les disponibilités pour chaque salle
def generate_disponibilites_salle():
    jours_semaine = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']
    heures_travail = ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"]

    disponibilites = []

    for jour in jours_semaine:
        # Génération aléatoire des heures de début et de fin
        heure_debut = random.choice(heures_travail)
        heure_fin = random.choice(heures_travail[heures_travail.index(heure_debut):])

        # Génération aléatoire de l'ID de salle (supposons que vous avez 73 salles)
        id_salle = random.randint(1, 73)

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

# Fermeture de la connexion à la base de données
cursor.close()
conn.close()

print("Les disponibilités des salles ont été générées et enregistrées dans la base de données.")

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

# Création d'un générateur de disponibilités aléatoires pour chaque professeur
def generate_disponibilites(id_professeur):
    jours_semaine = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']
    heures_travail = ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"]

    disponibilites = []

    for jour in jours_semaine:
        # Génération aléatoire des heures de début et de fin
        heure_debut = random.choice(heures_travail)
        if heure_debut == heures_travail[-1]:
            heure_fin = heures_travail[-1]
        else:
            heure_fin = random.choice(heures_travail[heures_travail.index(heure_debut) + 1:])

        # Ajout de la disponibilité à la liste
        disponibilites.append((id_professeur, jour, heure_debut, heure_fin))

    return disponibilites

# Préparation de la requête SQL pour insérer une nouvelle ligne dans la table Disponibilites
requete_disponibilites = "INSERT INTO Disponibilites (ID_Prof, JourSemaine, HeureDebut, HeureFin) VALUES (%s, %s, %s, %s)"

# Récupérer le nombre réel de professeurs dans la base de données
cursor.execute("SELECT COUNT(*) FROM Professeurs")
num_profs = cursor.fetchone()[0]

# Boucle pour insérer les disponibilités pour chaque professeur
for id_prof in range(1, num_profs + 1):  # Utiliser le nombre réel de professeurs
    # Générer aléatoirement les disponibilités pour ce professeur
    disponibilites_prof = generate_disponibilites(id_prof)

    # Insérer les disponibilités dans la base de données
    cursor.executemany(requete_disponibilites, disponibilites_prof)

# Validation de la transaction pour enregistrer les données dans la base de données
conn.commit()

# Fermeture de la connexion à la base de données
cursor.close()
conn.close()

import mysql.connector
from faker import Faker
import random
import datetime

# Se connecter à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mdp",
    database="projetinfo"
)
cursor = conn.cursor()

# Création d'un générateur de données aléatoires
fake = Faker()

# Liste des jours de la semaine
jours_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]

# Liste des heures de début et de fin de cours
heures_debut = [datetime.time(hour) for hour in range(8, 18)]
heures_fin = [datetime.time(hour) for hour in range(9, 19)]

# Nombre de cours à générer
nombre_cours = 20

# Préparation de la requête SQL pour insérer une nouvelle ligne dans Cours_Etudiants
requete_cours_etudiants = "INSERT INTO Cours_Etudiants (ID_Professeur, ID_Matiere, ID_Salle, JourSemaine, HeureDebut, HeureFin) VALUES (%s, %s, %s, %s, %s, %s)"

# Sélection des professeurs, matières et salles existants dans la base de données
cursor.execute("SELECT ID_Professeur FROM Professeurs")
professeurs = cursor.fetchall()

cursor.execute("SELECT ID_Matiere FROM Matieres")
matieres = cursor.fetchall()

cursor.execute("SELECT ID_Salle FROM Salles")
salles = cursor.fetchall()

# Boucle pour insérer des données aléatoires dans la table Cours_Etudiants
for _ in range(nombre_cours):
    id_professeur = random.choice(professeurs)[0]
    id_matiere = random.choice(matieres)[0]
    id_salle = random.choice(salles)[0]
    jour_semaine = random.choice(jours_semaine)
    heure_debut = random.choice(heures_debut)
    heure_fin = random.choice(heures_fin)

    # Exécution de la requête SQL avec les données spécifiées
    donnees_cours = (id_professeur, id_matiere, id_salle, jour_semaine, heure_debut, heure_fin)
    cursor.execute(requete_cours_etudiants, donnees_cours)

# Validation de la transaction pour enregistrer les données dans la base de données
conn.commit()

# Affichage d'un message de confirmation
print(f"{nombre_cours} cours ont été générés avec succès.")

# Fermeture de la connexion à la base de données
cursor.close()
conn.close()

import mysql.connector
from faker import Faker
import random

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

# Préparation de la requête SQL pour insérer une nouvelle ligne dans la table Professeurs
requete_professeurs = "INSERT INTO Professeurs (Nom, Prenom) VALUES (%s, %s)"

# Boucle pour insérer 25 lignes dans la table Professeurs
for _ in range(25):
    # Génération de données aléatoires pour les professeurs
    nom_prof = fake.last_name()
    prenom_prof = fake.first_name()

    # Données à insérer pour les professeurs
    donnees_prof = (nom_prof, prenom_prof)

    # Exécution de la requête SQL pour insérer un nouveau professeur
    cursor.execute(requete_professeurs, donnees_prof)

# Préparation de la requête SQL pour insérer une nouvelle ligne dans la table Matieres
requete_matieres = "INSERT INTO Matieres (Nom, ProfesseurResponsable, Duree, NombreCoursSemaine) VALUES (%s, %s, %s, %s)"

# Liste pour garder une trace du nombre de professeurs associés à chaque matière
professeurs_par_matiere = {}

# Boucle pour insérer 10 lignes dans la table Matieres
for _ in range(10):
    # Génération de données aléatoires pour les matières
    nom_matiere = fake.word()

    # Déterminer le nombre de professeurs pour cette matière (maximum 3)
    nb_professeurs = random.randint(1, 3)

    # Sélectionner aléatoirement les IDs de professeurs
    ids_professeurs = random.sample(range(1, 26), nb_professeurs)  # Supposons que vous ayez 25 professeurs

    # Ajouter cette information à la liste professeurs_par_matiere
    professeurs_par_matiere[nom_matiere] = ids_professeurs

    # Génération d'une durée aléatoire pour chaque matière, avec une durée maximale de 4 heures
    duree_heures = random.randint(0, 4)
    duree_minutes = random.randint(0, 59)
    duree_secondes = random.randint(0, 59)
    duree = f"{duree_heures:02}:{duree_minutes:02}:{duree_secondes:02}"

    # Nombre de cours par semaine pour cette matière
    nombre_cours_semaine = random.randint(1, 5)  # Par exemple, entre 1 et 5 cours par semaine

    # Pour chaque professeur associé à cette matière, insérer une ligne dans la table Matieres
    for id_prof in ids_professeurs:
        donnees_matiere = (nom_matiere, id_prof, duree, nombre_cours_semaine)
        cursor.execute(requete_matieres, donnees_matiere)

# Validation de la transaction pour enregistrer les données dans la base de données
conn.commit()

# Afficher les associations matière-professeur
print("Associations Matière-Professeur :")
for matiere, professeurs in professeurs_par_matiere.items():
    print(f"{matiere}: {professeurs}")

# Fermeture de la connexion à la base de données
cursor.close()
conn.close()
print("Connexion à la base de données fermée.")

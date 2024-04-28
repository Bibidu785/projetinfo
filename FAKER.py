import mysql.connector
from openpyxl import Workbook
from datetime import datetime
from faker import Faker
import random
import os
import copy

def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Utopie39*",
            database="projetinfo"
        )
        print("Connexion à la base de données réussie.")
        return conn
    except mysql.connector.Error as err:
        print(f"Erreur de connexion à la base de données : {err}")
        return None

def get_capacite_salle():
    return random.randint(10, 50)  # Génère une capacité aléatoire entre 10 et 50

def saisie_professeurs(cursor, conn):
    global fake
    nom = fake.last_name()
    prenom = fake.first_name()
    try:
        cursor.execute("INSERT INTO Professeurs (Nom, Prenom) VALUES (%s, %s)", (nom, prenom))
        conn.commit()
        print("Enregistrement du professeur réussi.")
    except mysql.connector.Error as err:
        print(f"Erreur MySQL : {err}")
        conn.rollback()

def saisie_matieres(cursor, conn):
    global fake
    nom = fake.word()
    id_professeur = random.randint(1, 10)  # Supposons que vous avez 10 professeurs
    nb_cours = random.randint(1, 5)  # Supposons que chaque matière a entre 1 et 5 cours par semaine
    duree = fake.time(pattern="%H:%M:%S", end_datetime=None)
    try:
        cursor.execute("INSERT INTO Matieres (Nom, ID_Professeur, Nb_Cours, Duree) VALUES (%s, %s, %s, %s)", (nom, id_professeur, nb_cours, duree))
        conn.commit()
        print("Enregistrement de la matière réussi.")
    except mysql.connector.Error as err:
        print(f"Erreur MySQL : {err}")
        conn.rollback()

def saisie_salles(cursor, conn):
    global fake
    nom = fake.word()
    capacite = get_capacite_salle()
    try:
        cursor.execute("INSERT INTO Salles (Nom, Capacite) VALUES (%s, %s)", (nom, capacite))
        conn.commit()
        print("Enregistrement de la salle réussi.")
    except mysql.connector.Error as err:
        print(f"Erreur MySQL : {err}")
        conn.rollback()

def saisie_classes(cursor, conn):
    global fake
    nom = fake.word()
    try:
        cursor.execute("INSERT INTO Classes (Nom) VALUES (%s)", (nom,))
        conn.commit()
        print("Enregistrement de la classe réussi.")
    except mysql.connector.Error as err:
        print(f"Erreur MySQL : {err}")
        conn.rollback()

def saisie_cours_etudiants(cursor, conn):
    global fake
    try:
        id_professeur = random.randint(1, 10)  # Supposons que vous avez 10 professeurs
        id_matiere = random.randint(1, 20)  # Supposons que vous avez 20 matières
        id_salle = random.randint(1, 5)  # Supposons que vous avez 5 salles
        jour = fake.date_time().strftime('%A')  # Génère un jour de la semaine aléatoire
        heure_debut = fake.date_time_between(datetime(2022, 1, 1, 8, 0, 0), datetime(2022, 1, 1, 18, 0, 0)).strftime("%H:%M:%S")  # Génère une heure entre 8h et 18h
        heure_fin = fake.date_time_between(datetime(2022, 1, 1, 9, 0, 0), datetime(2022, 1, 1, 19, 0, 0)).strftime("%H:%M:%S")  # Génère une heure entre 9h et 19h

        cursor.execute("INSERT INTO Cours_Etudiants (ID_Professeur, ID_Matiere, ID_Salle, JourSemaine, HeureDebut, HeureFin) VALUES (%s, %s, %s, %s, %s, %s)",
                       (id_professeur, id_matiere, id_salle, jour, heure_debut, heure_fin))
        conn.commit()
        print("Enregistrement du cours réussi.")
    except mysql.connector.Error as err:
        print(f"Erreur MySQL : {err}")
        conn.rollback()

def saisie_eleves(cursor, conn):
    global fake
    nom = fake.last_name()
    prenom = fake.first_name()
    id_classe = random.randint(1, 5)  # Supposons que vous avez 5 classes
    try:
        cursor.execute("INSERT INTO Eleves (Nom, Prenom, ID_Classe) VALUES (%s, %s, %s)", (nom, prenom, id_classe))
        conn.commit()
        print("Enregistrement de l'élève réussi.")
    except mysql.connector.Error as err:
        print(f"Erreur MySQL : {err}")
        conn.rollback()

def saisie_disponibilites(cursor, conn):
    global fake
    id_professeur = random.randint(1, 10)  # Supposons que vous avez 10 professeurs
    jour = fake.date_time().strftime('%A')  # Génère un jour de la semaine aléatoire
    heure_debut = fake.date_time_between(datetime(2022, 1, 1, 8, 0, 0), datetime(2022, 1, 1, 18, 0, 0)).strftime("%H:%M:%S")  # Génère une heure entre 8h et 18h
    heure_fin = fake.date_time_between(datetime(2022, 1, 1, 9, 0, 0), datetime(2022, 1, 1, 19, 0, 0)).strftime("%H:%M:%S")  # Génère une heure entre 9h et 19h

    try:
        cursor.execute("INSERT INTO Disponibilites (ID_Professeur, JourSemaine, HeureDebut, HeureFin) VALUES (%s, %s, %s, %s)",
                       (id_professeur, jour, heure_debut, heure_fin))
        conn.commit()
        print("Enregistrement de la disponibilité réussi.")
    except mysql.connector.Error as err:
        print(f"Erreur MySQL : {err}")
        conn.rollback()

def saisie_cours_classe(cursor, conn):
    try:
        cursor.execute("SELECT * FROM Cours_Etudiants")
        cours = cursor.fetchall()
        id_cours = random.choice(cours)[0]  # Sélectionne un cours aléatoire

        cursor.execute("SELECT * FROM Classes")
        classes = cursor.fetchall()
        id_classe = random.choice(classes)[0]  # Sélectionne une classe aléatoire

        cursor.execute("INSERT INTO Cours_Classe (ID_Cours, ID_Classe) VALUES (%s, %s)", (id_cours, id_classe))
        conn.commit()
        print("Enregistrement du cours pour la classe réussi.")
    except mysql.connector.Error as err:
        print(f"Erreur MySQL : {err}")
        conn.rollback()

def saisie_disponibilites_salle(cursor, conn):
    global fake
    try:
        id_salle = random.randint(1, 5)  # Supposons que vous avez 5 salles
        jour = fake.date_time().strftime('%A')  # Génère un jour de la semaine aléatoire
        heure_debut = fake.date_time_between(datetime(2022, 1, 1, 8, 0, 0), datetime(2022, 1, 1, 18, 0, 0)).strftime("%H:%M:%S")  # Génère une heure entre 8h et 18h
        heure_fin = fake.date_time_between(datetime(2022, 1, 1, 9, 0, 0), datetime(2022, 1, 1, 19, 0, 0)).strftime("%H:%M:%S")  # Génère une heure entre 9h et 19h

        cursor.execute("INSERT INTO Disponibilites_salle (ID_Salle, JourSemaine, HeureDebut, HeureFin) VALUES (%s, %s, %s, %s)",
                       (id_salle, jour, heure_debut, heure_fin))
        conn.commit()
        print("Enregistrement de la disponibilité de la salle réussi.")
    except mysql.connector.Error as err:
        print(f"Erreur MySQL : {err}")
        conn.rollback()

def fetch_data(cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    return cursor.fetchall()

def generate_initial_timetable(cours, professeurs, matieres, salles):
    # Création d'un emploi du temps vide
    timetable = {}

    for cours_item in cours:
        id_cours = cours_item[0]
        id_professeur = cours_item[1]
        id_matiere = cours_item[2]
        id_salle = cours_item[3]
        jour = cours_item[4]
        heure_debut = cours_item[5]
        heure_fin = cours_item[6]

        # Récupération des informations sur le professeur et la matière
        professeur_info = [prof for prof in professeurs if prof[0] == id_professeur][0]
        matiere_info = [matiere for matiere in matieres if matiere[0] == id_matiere][0]

        # Récupération du nom de la salle
        salle_info = [salle for salle in salles if salle[0] == id_salle][0]

        if jour not in timetable:
            timetable[jour] = {}
        if heure_debut not in timetable[jour]:
            timetable[jour][heure_debut] = []

        timetable[jour][heure_debut].append({
            "Cours": matiere_info[1],
            "Professeur": f"{professeur_info[1]} {professeur_info[2]}",
            "Salle": salle_info[1],
            "Heure fin": heure_fin
        })

    return timetable

def evaluate_timetable(timetable, disponibilites, capacites_salles):
    conflicts_salle = 0
    conflicts_professeur = 0
    capacity_constraints = 0
    prof_availability_constraints = 0
    individual_preferences = 0

    for jour, heures in timetable.items():
        for heure, cours in heures.items():
            for course in cours:
                salle = course['Salle']
                professeur = course['Professeur']
                heure_debut = heure
                heure_fin = course['Heure fin']

                # Vérification des conflits de salle
                salle_dispo = [disp for disp in disponibilites if disp[1] == jour and disp[2] <= heure_debut and disp[3] >= heure_fin and disp[0] == salle]
                if not salle_dispo:
                    conflicts_salle += 1

                # Vérification des conflits de professeur
                prof_dispo = [disp for disp in disponibilites if disp[1] == jour and disp[2] <= heure_debut and disp[3] >= heure_fin and disp[0] == professeur]
                if not prof_dispo:
                    conflicts_professeur += 1

                # Vérification des contraintes de capacité des salles
                if capacites_salles[salle] < len(cours):
                    capacity_constraints += 1

                # Vérification des contraintes de disponibilité des professeurs
                if not prof_dispo:
                    prof_availability_constraints += 1

                # Vérification des préférences individuelles (non implémentées)

    evaluation = {
        'conflicts_salle': conflicts_salle,
        'conflicts_professeur': conflicts_professeur,
        'capacity_constraints': capacity_constraints,
        'prof_availability_constraints': prof_availability_constraints,
        'individual_preferences': individual_preferences
    }

    return evaluation

def generate_neighborhood(timetable):
    # Génère un voisinage en effectuant un échange aléatoire de deux cours
    # Nous allons simplement choisir deux cours aléatoires et échanger leurs horaires
    new_timetable = copy.deepcopy(timetable)

    # Choix aléatoire d'un jour et d'une heure
    jour1 = random.choice(list(new_timetable.keys()))
    heure1 = random.choice(list(new_timetable[jour1].keys()))

    # Choix aléatoire d'un autre jour et d'une autre heure
    jour2 = random.choice(list(new_timetable.keys()))
    heure2 = random.choice(list(new_timetable[jour2].keys()))

    # Échange des cours entre les deux horaires
    cours1 = new_timetable[jour1][heure1]
    cours2 = new_timetable[jour2][heure2]
    new_timetable[jour1][heure1] = cours2
    new_timetable[jour2][heure2] = cours1

    return new_timetable

def recherche_locale(initial_timetable, disponibilites, capacites_salles, max_iterations=1000):
    current_timetable = initial_timetable
    best_timetable = initial_timetable
    best_evaluation = evaluate_timetable(initial_timetable, disponibilites, capacites_salles)

    iterations = 0
    while iterations < max_iterations:
        new_timetable = generate_neighborhood(current_timetable)
        new_evaluation = evaluate_timetable(new_timetable, disponibilites, capacites_salles)

        if (new_evaluation['conflicts_salle'] + new_evaluation['conflicts_professeur'] + new_evaluation['capacity_constraints'] + 
            new_evaluation['prof_availability_constraints'] + new_evaluation['individual_preferences'] < 
            best_evaluation['conflicts_salle'] + best_evaluation['conflicts_professeur'] + best_evaluation['capacity_constraints'] + 
            best_evaluation['prof_availability_constraints'] + best_evaluation['individual_preferences']):
            best_timetable = new_timetable
            best_evaluation = new_evaluation

        current_timetable = new_timetable
        iterations += 1

    return best_timetable

def optimize_timetable(cursor, conn):
    # Récupération des données
    cours = fetch_data(cursor, "Cours_Etudiants")
    professeurs = fetch_data(cursor, "Professeurs")
    matieres = fetch_data(cursor, "Matieres")  
    salles = fetch_data(cursor, "Salles")
    disponibilites = fetch_data(cursor, "Disponibilites")
    capacites_salles = {salle[1]: salle[2] for salle in salles}  # Création d'un dictionnaire des capacités des salles

    # Création de l'emploi du temps initial
    initial_timetable = generate_initial_timetable(cours, professeurs, matieres, salles)

    # Optimisation de l'emploi du temps
    optimized_timetable = recherche_locale(initial_timetable, disponibilites, capacites_salles)

    return optimized_timetable

def main():
    global fake
    fake = Faker()
    conn = connect_to_database()
    if not conn:
        return

    cursor = conn.cursor()

    optimized_timetable = optimize_timetable(cursor, conn)

    # Création d'un nouveau classeur Excel pour l'emploi du temps optimisé
    wb = Workbook()
    ws = wb.active

    # Écriture de l'emploi du temps optimisé dans le classeur Excel
    for jour, heures in optimized_timetable.items():
        ws.append([jour])
        for heure, cours in heures.items():
            for course in cours:
                ws.append([heure, course["Cours"], course["Professeur"], course["Salle"]])
            ws.append([])  # Ajoute une ligne vide entre les heures

    wb.save("emploi_du_temps_optimise.xlsx")
    print("L'emploi du temps optimisé a été enregistré avec succès sous le nom 'emploi_du_temps_optimise.xlsx'.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()

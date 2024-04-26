import mysql.connector
from openpyxl import Workbook
from datetime import datetime
from faker import Faker
import random

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
    nom = fake.word()
    try:
        cursor.execute("INSERT INTO Classes (Nom) VALUES (%s)", (nom,))
        conn.commit()
        print("Enregistrement de la classe réussi.")
    except mysql.connector.Error as err:
        print(f"Erreur MySQL : {err}")
        conn.rollback()

def saisie_cours_etudiants(cursor, conn):
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

def generate_timetable(cursor, conn):
    # Fetching data
    cours = fetch_data(cursor, "Cours_Etudiants")
    professeurs = fetch_data(cursor, "Professeurs")
    matieres = fetch_data(cursor, "Matieres")  # Ajout pour récupérer les données des matières
    salles = fetch_data(cursor, "Salles")
    disponibilites = fetch_data(cursor, "Disponibilites")

    # Création d'un emploi du temps vide
    timetable = {}

    # Remplissage de l'emploi du temps
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

        # Vérification de la disponibilité du professeur
        prof_dispo = [disp for disp in disponibilites if disp[1] == jour and disp[2] <= heure_debut and disp[3] >= heure_fin and disp[0] == id_professeur]

        # Vérification de la disponibilité de la salle
        salle_dispo = [disp for disp in disponibilites if disp[1] == jour and disp[2] <= heure_debut and disp[3] >= heure_fin and disp[0] == id_salle]

        if prof_dispo and salle_dispo:
            # Si le professeur et la salle sont disponibles, ajoutez le cours à l'emploi du temps
            if jour not in timetable:
                timetable[jour] = []
            timetable[jour].append({
                "Cours": matiere_info[1],
                "Professeur": f"{professeur_info[1]} {professeur_info[2]}",
                "Salle": salle_info[1],
                "Heure début": heure_debut,
                "Heure fin": heure_fin
            })
        else:
            print(f"Impossible de planifier le cours {matiere_info[1]} le {jour} de {heure_debut} à {heure_fin}. Professeur ou salle non disponible.")

    # Création d'un nouveau classeur Excel
    wb = Workbook()
    ws = wb.active
    ws.title = "Emploi du temps"

    # En-têtes
    headers = ["Jour", "Heure début", "Heure fin", "Cours", "Professeur", "Salle"]
    ws.append(headers)

    # Ajout des données dans le classeur Excel
    for jour, cours_jour in timetable.items():
        for cours_item in cours_jour:
            ws.append([jour, cours_item['Heure début'], cours_item['Heure fin'], cours_item['Cours'], cours_item['Professeur'], cours_item['Salle']])

    # Enregistrement du fichier Excel
    filename = "emploi_du_temps.xlsx"
    wb.save(filename)
    print(f"Emploi du temps enregistré dans le fichier Excel : {filename}")

def optimize_timetable(cursor, conn):
    # Cette fonction devrait contenir la logique pour optimiser l'emploi du temps.
    # Étant donné que l'optimisation dépend fortement des contraintes spécifiques et de la logique métier,
    # elle doit être adaptée en fonction des besoins spécifiques du projet. Nous ne l'implémenterons pas ici.
    pass

def main_menu():
    print("\nMenu Principal :")
    print("1. Saisir un professeur")
    print("2. Saisir une matière")
    print("3. Saisir une salle")
    print("4. Saisir une classe")
    print("5. Saisir un cours")
    print("6. Saisir un élève")
    print("7. Saisir une disponibilité pour un professeur")
    print("8. Associer un cours à une classe")
    print("9. Saisir une disponibilité pour une salle")
    print("10. Générer et sauvegarder l'emploi du temps dans un fichier Excel")
    print("11. Optimiser l'emploi du temps")
    print("0. Quitter")
    return input("Entrez votre choix : ")

def main():
    global fake
    fake = Faker()
    conn = connect_to_database()
    if not conn:
        return

    cursor = conn.cursor()

    while True:
        choice = main_menu()

        if choice == '1':
            saisie_professeurs(cursor, conn)
        elif choice == '2':
            saisie_matieres(cursor, conn)
        elif choice == '3':
            saisie_salles(cursor, conn)
        elif choice == '4':
            saisie_classes(cursor, conn)
        elif choice == '5':
            saisie_cours_etudiants(cursor, conn)
        elif choice == '6':
            saisie_eleves(cursor, conn)
        elif choice == '7':
            saisie_disponibilites(cursor, conn)
        elif choice == '8':
            saisie_cours_classe(cursor, conn)
        elif choice == '9':
            saisie_disponibilites_salle(cursor, conn)
        elif choice == '10':
            generate_timetable(cursor, conn)
        elif choice == '11':
            optimize_timetable(cursor, conn)
        elif choice == '0':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

    cursor.close()
    conn.close()
    print("Connexion à la base de données fermée.")

if __name__ == "__main__":
    main()

import mysql.connector

# Se connecter à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="votre_nom_utilisateur",
    password="votre_mot_de_passe",
    database="projet"
)
cursor = conn.cursor()

# Validation des entrées utilisateur pour les capacités des salles
def get_capacite_salle():
    while True:
        capacite = input("Entrez la capacité de la salle : ")
        if capacite.isdigit():
            return int(capacite)
        else:
            print("Veuillez entrer un nombre valide pour la capacité.")

# Saisie des valeurs pour la table Professeurs
def saisie_professeurs():
    nom = input("Entrez le nom du professeur : ")
    prenom = input("Entrez le prénom du professeur : ")
    cursor.execute("INSERT INTO Professeurs (Nom, Prenom) VALUES (%s, %s)", (nom, prenom))
    conn.commit()
    print("Enregistrement du professeur réussi.")

# Saisie des valeurs pour la table Matières
def saisie_matieres():
    nom = input("Entrez le nom de la matière : ")
    cursor.execute("INSERT INTO Matières (Nom) VALUES (%s)", (nom,))
    conn.commit()
    print("Enregistrement de la matière réussi.")

# Saisie des valeurs pour la table Salles
def saisie_salles():
    nom = input("Entrez le nom de la salle : ")
    capacite = get_capacite_salle()
    cursor.execute("INSERT INTO Salles (Nom, Capacite) VALUES (%s, %s)", (nom, capacite))
    conn.commit()
    print("Enregistrement de la salle réussi.")

# Saisie des valeurs pour la table Eleves
def saisie_eleves():
    nom = input("Entrez le nom de l'élève : ")
    prenom = input("Entrez le prénom de l'élève : ")
    classe = input("Entrez la classe de l'élève : ")
    cursor.execute("INSERT INTO Eleves (Nom, Prenom, Classe) VALUES (%s, %s, %s)", (nom, prenom, classe))
    conn.commit()
    print("Enregistrement de l'élève réussi.")

# Afficher le nombre d'élèves dans chaque classe
def afficher_nombre_eleves_par_classe():
    cursor.execute("SELECT Classe, COUNT(*) FROM Eleves GROUP BY Classe")
    classes = cursor.fetchall()
    print("Nombre d'élèves par classe :")
    for classe in classes:
        print(f"{classe[0]} : {classe[1]} élèves")

# Saisie des valeurs pour la table Cours_Eleves
def saisie_cours_eleves():
    try:
        id_eleve = int(input("Entrez l'ID de l'élève : "))
        id_prof = int(input("Entrez l'ID du professeur : "))
        id_matiere = int(input("Entrez l'ID de la matière : "))
        id_salle = int(input("Entrez l'ID de la salle : "))
        jour = input("Entrez le jour du cours : ")
        heure_debut = input("Entrez l'heure de début du cours (format HH:MM:SS) : ")
        heure_fin = input("Entrez l'heure de fin du cours (format HH:MM:SS) : ")
        cursor.execute("INSERT INTO Cours_Eleves (ID_Eleve, ID_Prof, ID_Matière, ID_Salle, Jour, HeureDebut, HeureFin) VALUES (%s, %s, %s, %s, %s, %s, %s)", (id_eleve, id_prof, id_matiere, id_salle, jour, heure_debut, heure_fin))
        conn.commit()
        print("Enregistrement du cours pour l'élève réussi.")
    except mysql.connector.Error as err:
        print(f"Erreur MySQL : {err}")
        conn.rollback()

# Menu principal
def menu():
    while True:
        print("\n1. Saisir un professeur")
        print("2. Saisir une matière")
        print("3. Saisir une salle")
        print("4. Saisir un élève")
        print("5. Saisir un cours pour un élève")
        print("6. Afficher le nombre d'élèves par classe")
        print("0. Quitter")
        choix = input("Entrez votre choix : ")

        if choix == '1':
            saisie_professeurs()
        elif choix == '2':
            saisie_matieres()
        elif choix == '3':
            saisie_salles()
        elif choix == '4':
            saisie_eleves()
        elif choix == '5':
            saisie_cours_eleves()
        elif choix == '6':
            afficher_nombre_eleves_par_classe()
        elif choix == '0':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

menu()

# Fermer la connexion à la base de données
try:
    cursor.close()
    conn.close()
    print("Connexion à la base de données fermée.")
except mysql.connector.Error as err:
    print(f"Erreur MySQL : {err}")

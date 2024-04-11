import mysql.connector
from datetime import datetime, timedelta

# Fonction pour se connecter à la base de données
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

# Fonction principale
def main():
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()

        # Exécution d'une requête SQL pour récupérer toutes les lignes de la table Cours_Etudiants
        requete = "SELECT * FROM Cours_Etudiants"
        cursor.execute(requete)

        # Récupération des résultats de la requête
        resultats = cursor.fetchall()

        # Affichage de toutes les lignes de la table Cours_Etudiants
        print("Liste des cours d'étudiants :")
        for cours in resultats:
            # Convertir les heures en format HH:MM:SS
            heure_debut = datetime.min + cours[5]
            heure_fin = datetime.min + cours[6]

            # Afficher les informations du cours
            print(
                f"ID: {cours[0]}, Professeur: {cours[1]}, Matière: {cours[2]}, Salle: {cours[3]}, Jour: {cours[4]}, Heure de début: {heure_debut.strftime('%H:%M:%S')}, Heure de fin: {heure_fin.strftime('%H:%M:%S')}")

        # Fermeture de la connexion à la base de données
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()

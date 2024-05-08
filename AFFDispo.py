import mysql.connector

# Se connecter à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MDP",
    database="projetinfo"
)
cursor = conn.cursor()

# Exécution d'une requête SQL pour récupérer les disponibilités des professeurs
requete = "SELECT ID_Dispo, ID_Prof, JourSemaine, HeureDebut, HeureFin FROM Disponibilites"
cursor.execute(requete)

# Récupération des résultats de la requête
resultats = cursor.fetchall()

# Affichage des disponibilités
print("Liste des disponibilités des professeurs :")
for disponibilite in resultats:
    print(f"ID: {disponibilite[0]}, Professeur: {disponibilite[1]}, Jour: {disponibilite[2]}, Heure de début: {disponibilite[3]}, Heure de fin: {disponibilite[4]}")

# Fermeture de la connexion à la base de données
cursor.close()
conn.close()

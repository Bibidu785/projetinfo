from random import random, randint


def saisir_disponibilites():
    jours_semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
    disponibilites = {}

    while True:
        jour_saisi = input("Entrez le jour ou le prof est disponible ou 'q' pour quitter : ").lower()
        if jour_saisi == 'q':
            break

        if jour_saisi in jours_semaine:
            disponibilites[jour_saisi] = []
            while True:
                debut = input(f"Entrez l'heure de début pour {jour_saisi} (ex. 9) : ")
                fin = input(f"Entrez l'heure de fin pour {jour_saisi} (ex. 12) : ")

                if debut.isdigit() and fin.isdigit():
                    debut_heure = int(debut.strip())
                    fin_heure = int(fin.strip())

                    if 8 <= debut_heure < 20 and 8 <= fin_heure <= 20 and debut_heure < fin_heure:
                        disponibilites[jour_saisi].append((debut_heure, fin_heure))
                    else:
                        print("Heures invalides. Veuillez saisir des heures entre 8h et 20h et assurez-vous que l'heure de début est inférieure à l'heure de fin.")
                else:
                    print("Heures invalides. Veuillez saisir des heures en utilisant uniquement des chiffres.")

                continuer = input("Voulez-vous ajouter d'autres disponibilités pour ce jour ? (o/n) : ")
                if continuer.lower() != 'o':
                    break
        else:
            print("Jour invalide. les cours sont de lundi a vendredi")

    return disponibilites

while True:
    nbcours = int(input("Entrez le nombre de cours : "))
    nb_eleve = int(input("Entrez le nombre d'élèves : "))
    if nbcours < 1 or nb_eleve < 1:
        print("Erreur : on ne peut pas faire cours si il n'y pas de cours ni d'eleves")
    else:
        for i in range(nbcours):
            cours = len(input("Entrez le nom du cours : "))
            nom_professeur = len(input("Entrez le nom du professeur : "))
            horaires_disponibles = saisir_disponibilites()
            print("les disponibilites de ce prof sont donc : ", horaires_disponibles)
        break

class SalleDeClasse:
    def __init__(self, nom, capacite):
        self.nom = nom
        self.capacite = capacite

def creer_salles():
    nombre_salles = int(input("Combien de salles de classe il y a dans l'université : "))
    salles = []
    for i in range(nombre_salles):
        nom_salle = input(f"Nom de la salle de classe {i + 1}: ")
        capacite_salle = randint(20,300)
        salles.append(SalleDeClasse(nom_salle, capacite_salle))
    return salles

def afficher_salles(salles):
    print("\nListe des salles de classe créées :")
    for salle in salles:
        print(f"{salle.nom} - Capacité : {salle.capacite} élèves")

if __name__ == "__main__":
    mes_salles = creer_salles()
    afficher_salles(mes_salles)
import random

class Cours:
    def __init__(self, jour, heure, duree, salle, professeur, nb_etudiants, pref):
        self.jour = jour
        self.heure = heure
        self.duree = duree
        self.salle = salle
        self.professeur = professeur
        self.nb_etudiants = nb_etudiants
        self.pref = pref

class EmploiDuTemps:
    def __init__(self, nb_cours, nb_salles, capacites_salles, nb_professeurs, disponibilites_professeurs, nb_jours, temps_max):
        self.nb_cours = nb_cours
        self.nb_salles = nb_salles
        self.capacites_salles = capacites_salles
        self.nb_professeurs = nb_professeurs
        self.disponibilites_professeurs = disponibilites_professeurs
        self.nb_jours = nb_jours
        self.temps_max = temps_max
        self.cours = []

def evaluer_emploi_du_temps(edt):
    conflits = 0

    for i in range(edt.nb_cours - 1):
        for j in range(i + 1, edt.nb_cours):
            if (edt.cours[i].salle == edt.cours[j].salle and
                edt.cours[i].jour == edt.cours[j].jour and
                ((edt.cours[i].heure < edt.cours[j].heure and
                  edt.cours[i].heure + edt.cours[i].duree > edt.cours[j].heure) or
                 (edt.cours[i].heure > edt.cours[j].heure and
                  edt.cours[i].heure < edt.cours[j].heure + edt.cours[j].duree))):
                conflits += 1

    for i in range(edt.nb_cours - 1):
        for j in range(i + 1, edt.nb_cours):
            if (edt.cours[i].professeur == edt.cours[j].professeur and
                edt.cours[i].jour == edt.cours[j].jour and
                ((edt.cours[i].heure < edt.cours[j].heure and
                  edt.cours[i].heure + edt.cours[i].duree > edt.cours[j].heure) or
                 (edt.cours[i].heure > edt.cours[j].heure and
                  edt.cours[i].heure < edt.cours[j].heure + edt.cours[j].duree))):
                conflits += 1

    for i in range(edt.nb_cours):
        if edt.cours[i].nb_etudiants > edt.capacites_salles[edt.cours[i].salle]:
            conflits += 1

    for i in range(edt.nb_cours):
        if edt.disponibilites_professeurs[edt.cours[i].professeur][edt.cours[i].heure] == 0:
            conflits += 1

    for i in range(edt.nb_cours):
        if not edt.cours[i].pref:
            conflits += 1

    return conflits

def generer_voisinage(edt, voisin):
    a = random.randint(0, edt.nb_cours - 1)
    b = random.randint(0, edt.nb_cours - 1)

    while b == a:
        b = random.randint(0, edt.nb_cours - 1)

    voisin.nb_cours = edt.nb_cours
    voisin.nb_salles = edt.nb_salles
    voisin.capacites_salles = edt.capacites_salles
    voisin.nb_professeurs = edt.nb_professeurs
    voisin.disponibilites_professeurs = edt.disponibilites_professeurs
    voisin.nb_jours = edt.nb_jours
    voisin.temps_max = edt.temps_max

    voisin.cours = edt.cours[:]

    voisin.cours[a], voisin.cours[b] = voisin.cours[b], voisin.cours[a]

def recherche_locale(edt):
    meilleure_eval = evaluer_emploi_du_temps(edt)
    iterations_sans_amelioration = 0
    iterations_max = 1000

    while iterations_sans_amelioration < iterations_max:
        voisin = EmploiDuTemps(0, 0, [], 0, [], 0, 0)
        generer_voisinage(edt, voisin)

        eval_voisin = evaluer_emploi_du_temps(voisin)

        if eval_voisin < meilleure_eval:
            meilleure_eval = eval_voisin
            edt = voisin
            iterations_sans_amelioration = 0
        else:
            iterations_sans_amelioration += 1

    return edt

def main():
    edt = EmploiDuTemps(10, 3, [30, 40, 50], 2, [[1, 0, 1, 1, 0, 1, 1, 1], [1, 1, 0, 1, 1, 1, 0, 1]], 5, 8)

    random.seed()

    for i in range(edt.nb_cours):
        jour = random.randint(0, edt.nb_jours - 1)
        heure = random.randint(0, edt.temps_max - 1)
        duree = random.randint(1, 3)
        salle = random.randint(0, edt.nb_salles - 1)
        professeur = random.randint(0, edt.nb_professeurs - 1)
        nb_etudiants = random.randint(1, 50)
        pref = random.randint(0, 1)
        edt.cours.append(Cours(jour, heure, duree, salle, professeur, nb_etudiants, pref))

    edt = recherche_locale(edt)

    print("Emploi du temps optimal:")
    for i, cours in enumerate(edt.cours):
        print(f"Cours {i}: Jour {cours.jour}, Heure {cours.heure}, Duree {cours.duree}, Salle {cours.salle}, Professeur {cours.professeur}, Etudiants {cours.nb_etudiants}, Pref {cours.pref}")

if __name__ == "__main__":
    main()

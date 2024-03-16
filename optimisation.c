#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

typedef struct {
    int jour;
    int heure;
    int duree;
    int salle;
    int professeur;
    int nb_etudiants;
    bool pref;
} Cours;

typedef struct {
    Cours cours[100];
    int nb_cours;
    int nb_salles;
    int capacites_salles[10];
    int nb_professeurs;
    int disponibilites_professeurs[10][8];
    int nb_jours;
    int temps_max;
} EmploiDuTemps;

int evaluer_emploi_du_temps(EmploiDuTemps *edt) {
    int conflits = 0;

    // Vérifier les conflits de salle
    for (int i = 0; i < edt->nb_cours - 1; i++) {
        for (int j = i + 1; j < edt->nb_cours; j++) {
            if (edt->cours[i].salle == edt->cours[j].salle &&
                edt->cours[i].jour == edt->cours[j].jour &&
                ((edt->cours[i].heure < edt->cours[j].heure &&
                  edt->cours[i].heure + edt->cours[i].duree > edt->cours[j].heure) ||
                 (edt->cours[i].heure > edt->cours[j].heure &&
                  edt->cours[i].heure < edt->cours[j].heure + edt->cours[j].duree))) {
                conflits++;
            }
        }
    }

    // Vérifier les conflits de professeur
    for (int i = 0; i < edt->nb_cours - 1; i++) {
        for (int j = i + 1; j < edt->nb_cours; j++) {
            if (edt->cours[i].professeur == edt->cours[j].professeur &&
                edt->cours[i].jour == edt->cours[j].jour &&
                ((edt->cours[i].heure < edt->cours[j].heure &&
                  edt->cours[i].heure + edt->cours[i].duree > edt->cours[j].heure) ||
                 (edt->cours[i].heure > edt->cours[j].heure &&
                  edt->cours[i].heure < edt->cours[j].heure + edt->cours[j].duree))) {
                conflits++;
            }
        }
    }

    // Vérifier les contraintes de capacité des salles
    for (int i = 0; i < edt->nb_cours; i++) {
        if (edt->cours[i].nb_etudiants > edt->capacites_salles[edt->cours[i].salle]) {
            conflits++;
        }
    }

    // Vérifier les contraintes de disponibilité des professeurs
    for (int i = 0; i < edt->nb_cours; i++) {
        if (edt->disponibilites_professeurs[edt->cours[i].professeur][edt->cours[i].heure] == 0) {
            conflits++;
        }
    }

    // Vérifier les préférences individuelles
    for (int i = 0; i < edt->nb_cours; i++) {
        if (!edt->cours[i].pref) {
            conflits++;
        }
    }

    return conflits;
}

void generer_voisinage(EmploiDuTemps *edt, EmploiDuTemps *voisin) {
    int a = rand() % edt->nb_cours;
    int b = rand() % edt->nb_cours;

    while (b == a) {
        b = rand() % edt->nb_cours;
    }

    voisin->nb_cours = edt->nb_cours;
    voisin->nb_salles = edt->nb_salles;
    for (int i = 0; i < edt->nb_salles; i++) {
        voisin->capacites_salles[i] = edt->capacites_salles[i];
    }
    voisin->nb_professeurs = edt->nb_professeurs;
    for (int i = 0; i < edt->nb_professeurs; i++) {
        for (int j = 0; j < edt->temps_max; j++) {
            voisin->disponibilites_professeurs[i][j] = edt->disponibilites_professeurs[i][j];
        }
    }
    voisin->nb_jours = edt->nb_jours;
    voisin->temps_max = edt->temps_max;

    for (int i = 0; i < edt->nb_cours; i++) {
        voisin->cours[i] = edt->cours[i];
    }

    Cours tmp = voisin->cours[a];
    voisin->cours[a] = voisin->cours[b];
    voisin->cours[b] = tmp;
}

void recherche_locale(EmploiDuTemps *edt) {
    int meilleure_eval = evaluer_emploi_du_temps(edt);
    int iterations_sans_amelioration = 0;
    int iterations_max = 1000;

    while (iterations_sans_amelioration < iterations_max) {
        EmploiDuTemps voisin;
        generer_voisinage(edt, &voisin);

        int eval_voisin = evaluer_emploi_du_temps(&voisin);

        if (eval_voisin < meilleure_eval) {
            meilleure_eval = eval_voisin;
            *edt = voisin;
            iterations_sans_amelioration = 0;
        } else {
            iterations_sans_amelioration++;
        }
    }
}

int main() {
    // Initialiser l'emploi du temps avec des données d'exemple
    EmploiDuTemps edt;
    edt.nb_cours = 10;
    edt.nb_salles = 3;
    edt.capacites_salles[0] = 30;
    edt.capacites_salles[1] = 40;
    edt.capacites_salles[2] = 50;
    edt.nb_professeurs = 2;
    edt.disponibilites_professeurs[0][0] = 1;
    edt.disponibilites_professeurs[0][1] = 0;
    edt.disponibilites_professeurs[0][2] = 1;
    edt.disponibilites_professeurs[0][3] = 1;
    edt.disponibilites_professeurs[0][4] = 0;
    edt.disponibilites_professeurs[0][5] = 1;
    edt.disponibilites_professeurs[0][6] = 1;
    edt.disponibilites_professeurs[0][7] = 1;
    edt.disponibilites_professeurs[1][0] = 1;
    edt.disponibilites_professeurs[1][1] = 1;
    edt.disponibilites_professeurs[1][2] = 0;
    edt.disponibilites_professeurs[1][3] = 1;
    edt.disponibilites_professeurs[1][4] = 1;
    edt.disponibilites_professeurs[1][5] = 1;
    edt.disponibilites_professeurs[1][6] = 0;
    edt.disponibilites_professeurs[1][7] = 1;
    edt.nb_jours = 5;
    edt.temps_max = 8;

    srand(time(NULL));

    for (int i = 0; i < edt.nb_cours; i++) {
        edt.cours[i].jour = rand() % edt.nb_jours;
        edt.cours[i].heure = rand() % edt.temps_max;
        edt.cours[i].duree = rand() % 3 + 1;
        edt.cours[i].salle = rand() % edt.nb_salles;
        edt.cours[i].professeur = rand() % edt.nb_professeurs;
        edt.cours[i].nb_etudiants = rand() % 50 + 1;
        edt.cours[i].pref = rand() % 2;
    }

    recherche_locale(&edt);

    printf("Emploi du temps optimal:\n");
    for (int i = 0; i < edt.nb_cours; i++) {
        printf("Cours %d: Jour %d, Heure %d, Duree %d, Salle %d, Professeur %d, Etudiants %d, Pref %d\n",
               i, edt.cours[i].jour, edt.cours[i].heure, edt.cours[i].duree,
               edt.cours[i].salle, edt.cours[i].professeur, edt.cours[i].nb_etudiants, edt.cours[i].pref);
    }

    return 0;
}

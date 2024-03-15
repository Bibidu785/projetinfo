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

int evaluer_emploi_du_temps(EmploiDuTemps *edt);
void generer_voisinage(EmploiDuTemps *edt, EmploiDuTemps *voisin);
void recherche_locale(EmploiDuTemps *edt);
void saisir_donnees(EmploiDuTemps *edt);
int evaluer_emploi_du_temps(EmploiDuTemps *edt) {
    // ... (Même implémentation que précédemment)
}

void generer_voisinage(EmploiDuTemps *edt, EmploiDuTemps *voisin) {
    // ... (Même implémentation que précédemment)
}

void recherche_locale(EmploiDuTemps *edt) {
    // ... (Même implémentation que précédemment)
}

void saisir_donnees(EmploiDuTemps *edt) {
    printf("Nombre de cours: ");
    scanf("%d", &(edt->nb_cours));

    printf("Nombre de salles: ");
    scanf("%d", &(edt->nb_salles));
    for (int i = 0; i < edt->nb_salles; i++) {
        printf("Capacite de la salle %d: ", i + 1);
        scanf("%d", &(edt->capacites_salles[i]));
    }

    printf("Nombre de professeurs: ");
    scanf("%d", &(edt->nb_professeurs));
    for (int i = 0; i < edt->nb_professeurs; i++) {
        for (int j = 0; j < edt->temps_max; j++) {
            printf("Disponibilite du professeur %d a l'heure %d (0 ou 1): ", i + 1, j);
            scanf("%d", &(edt->disponibilites_professeurs[i][j]));
        }
    }

    printf("Nombre de jours: ");
    scanf("%d", &(edt->nb_jours));

    printf("Temps maximum par jour: ");
    scanf("%d", &(edt->temps_max));

    for (int i = 0; i < edt->nb_cours; i++) {
        printf("\nCours %d:\n", i + 1);
        printf("Jour (entre 0 et %d): ", edt->nb_jours - 1);
        scanf("%d", &(edt->cours[i].jour));
        printf("Heure (entre 0 et %d): ", edt->temps_max - 1);
        scanf("%d", &(edt->cours[i].heure));
        printf("Duree (en heures): ");
        scanf("%d", &(edt->cours[i].duree));
        printf("Salle (entre 0 et %d): ", edt->nb_salles - 1);
        scanf("%d", &(edt->cours[i].salle));
        printf("Professeur (entre 0 et %d): ", edt->nb_professeurs - 1);
        scanf("%d", &(edt->cours[i].professeur));
        printf("Nombre d'etudiants: ");
        scanf("%d", &(edt->cours[i].nb_etudiants));
        printf("Preference (0 ou 1): ");
        scanf("%d", &(edt->cours[i].pref));
    }
}
int main() {
    EmploiDuTemps edt;

    saisir_donnees(&edt);

    recherche_locale(&edt);

    printf("Emploi du temps optimal:\n");
    for (int i = 0; i < edt.nb_cours; i++) {
        printf("Cours %d: Jour %d, Heure %d, Duree %d, Salle %d, Professeur %d, Etudiants %d, Pref %d\n",
               i, edt.cours[i].jour, edt.cours[i].heure, edt.cours[i].duree,
               edt.cours[i].salle, edt.cours[i].professeur, edt.cours[i].nb_etudiants, edt.cours[i].pref);
    }


    return 0;
}



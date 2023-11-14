"""
CLASSE JOUEUR_INTERFACE

Cette classe est la classe qui définit le joueur et ses actions au sein du jeu.

Attributs:
    + etat_jeu
    + grille
"""

from Grille import Grille
import numpy as np

class Joueur:
    # Initialisation du joueur
    def __init__(self):
        self.etat_jeu = False

    def GetEtat_jeu(self):
        return self.etat_jeu

    # Fonction qui initialise l'attribut de difficulté selon le choix appelé dans l'interface
    def choix_difficulte(self, difficulte):
        if int(difficulte) in [1, 2, 3]:
            self.grille = Grille(int(difficulte))

    # Fonction qui prend les coordonnées de la case de départ choisie dans l'interface pour générer la grille
    def choix_case_depart(self, case_dep_x, case_dep_y):
        grilliade = self.grille

        grilliade.matrice[int(case_dep_x), int(case_dep_y)] = "X"
        # Nous générons la matrice depuis la classe Grille grâce aux coordonnées de la case de départ
        grilliade.generation_matrice([int(case_dep_x), int(case_dep_y)])
        # Nous adaptons la matrice autour de la case de départ avec les numéros
        grilliade.faire_zone([int(case_dep_x), int(case_dep_y)])
        # Mise à jour de l'état de jeu
        self.etat_jeu = 'en jeu'

    # Fonction de mise en drapeau selon choix dans l'interface par le joueur
    def mettre_drapeau(self, x, y):
        grilliade = self.grille
        # Actualisation de la matrice pour mettre un drapeau ou l'enlever s'il est déjà posé sur la case
        if grilliade.matrice[x, y] == 'D':
            grilliade.matrice[x, y] = 'O'
        else:
            grilliade.matrice[x, y] = 'D'
        # Test si le joueur a gagné ou non
        if len(np.where(grilliade.matrice == 'D')) == len(grilliade.liste_bombe):
            r_etat = grilliade.fini_ou_non()
            if r_etat:
                self.etat_jeu = 'gagne'
            else:
                self.etat_jeu = 'perdu'
        print('Vous avez mis un drapeau ')

    # Fonction qui démine selon choix dans l'interface par le joueur
    def mettre_bombe(self, x, y):
        grilliade = self.grille
        case = [x, y]
        if case in grilliade.liste_bombe:
            # Mise à jour de la grille
            grilliade.matrice[x, y] = "B"
            self.etat_jeu = 'perdu'
        else:
            grilliade.matrice[x, y] = grilliade.nombre_bombe_autour([x, y])
        # Test si le joueur a gagné ou non
        if len(np.where(grilliade.matrice == 'D')) == len(grilliade.liste_bombe):
            r_etat = grilliade.fini_ou_non()
            if r_etat:
                self.etat_jeu = 'gagne'
            else:
                self.etat_jeu = 'perdu'
                print('Les drapeaux sont placés au mauvais endroit')
        grilliade.nouv_zone([x, y])
        print("Vous avez déminé")

    # Fonction qui indique si le jeu est terminé ou non
    def fini(self):
        if self.etat_jeu == 'perdu':
            return True
        elif self.etat_jeu == 'gagne':
            return True
        elif self.etat_jeu == 'abandon':
            print('Vous avez abandonné')
            self.grille.devoiler_matrice()
            return True
        else:
            return False

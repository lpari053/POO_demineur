"""
CLASSE GRILLE

Cette classe définit notre grille de jeu et ses actualisations et sa génération.

Cette classe est utilisée par la joueur_interface.

Attributs :
        + difficulte
        + nombre_ligne
        + nombre_colonne
        + combien_bombe
        + matrice
"""

import numpy as np
import random
import sys

class Grille:
 
    def __init__(self, difficulte):

        # Pour définir la grille, il nous faut la difficulté qui permet de définir ensuite les autres attributs
        self.difficulte = difficulte
        
        if (self.difficulte == 1):
            self.nombre_ligne = 5
            self.nombre_colonne = 5
            self.combien_bombe = 5
            
        elif (self.difficulte == 2):
            self.nombre_ligne = 10
            self.nombre_colonne = 10
            self.combien_bombe = 10
            
        elif (self.difficulte == 3):
            self.nombre_ligne = 20
            self.nombre_colonne = 20
            self.combien_bombe = 20

        # La matrice est de taille selon la difficulté
        self.matrice = np.zeros((self.nombre_ligne, self.nombre_colonne), dtype=object)
        for i in range(self.matrice.shape[0]):
            for j in range(self.matrice.shape[1]):
                # Pour l'instant aucune case de départ sélectionnée donc initialisée à zero
                self.matrice[i, j] = 'O'

    # Avec l'information de case de départ, nous pouvons générer la matrice avec les bombes    
    def generation_matrice(self, case_dep):
        liste_bombe = []

        # Place de manière aléatoire dans la matrice les bombes sans qu'il y ait des bombes sur la case de départ
        while len(liste_bombe) != self.nombre_ligne:
            casie = [random.randint(0, self.nombre_ligne-1), random.randint(0, self.nombre_ligne-1)]
            
            if casie != case_dep:

                if casie not in liste_bombe:
                    liste_bombe.append(casie)

        # On met la position des bombes dans une liste    
        self.liste_bombe = liste_bombe

    # Fonction pour savoir le nombre autour de bombe pour une case
    def nombre_bombe_autour(self, case):
        grilliade = self
        count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if [case[0]+i, case[1]+j] in grilliade.liste_bombe:
                    count += 1
        
        return count

    # Fonction d'aide développeur pour afficher la matrice du jeu
    def afficher_matrice(self):
        custom_format = np.array2string(self.matrice, separator=', ', formatter={'all': lambda x: str(x)})
        print(custom_format)

    # Fonction qui fait les zones avec les nombres autour d'une case
    def faire_zone(self, case):
        liste_bombe = self.liste_bombe
        self.matrice[case[0], case[1]] = self.nombre_bombe_autour(case)
        liste_zero = []
        c = 0
        C = []
        for i in [-1, 1, 0]:
            for j in [-1, 0, 1]:
                if [case[0]+i, case[1]+j] not in liste_bombe:
                    if [case[0]+i, case[1]+j] not in liste_bombe and case[0]+i < self.matrice.shape[0] and case[1]+j >= 0 and case[0]+i >= 0 and case[1]+j < self.matrice.shape[0]:
                        if(self.nombre_bombe_autour([case[0]+i, case[1]+j]) == 0):
                            c += 1
                            C.append([case[0]+i, case[1]+j])
                            self.matrice[case[0]+i, case[1]+j] = self.nombre_bombe_autour([case[0]+i, case[1]+j])
                            liste_zero.append([case[0]+i, case[1]+j])
                        else:
                            if i != j:
                                self.matrice[case[0]+i, case[1]+j] = self.nombre_bombe_autour([case[0]+i, case[1]+j])

        if c == 9:
            dd = np.random.choice(C)
            self.faire_zone(dd)

    # Actualise la matrice quand une action est faite pour afficher un nombre de façon aléatoire
    def nouv_zone(self, case):
        liste_bombe = self.liste_bombe
        self.matrice[case[0], case[1]] = self.nombre_bombe_autour(case)

        i = np.random.choice([-1, 0, 1])
        j = np.random.choice([-1, 0, 1])

        if i != 0 and j != 0:

            if [case[0]+i, case[1]+j] not in liste_bombe:
                try:
                    self.matrice[case[0]+i, case[1]+j] = self.nombre_bombe_autour([case[0]+i, case[1]+j])

                except:
                    self.nouv_zone(case)
            else:
                self.nouv_zone(case)
        else:
            self.nouv_zone(case)

    # Savoir si le jeu est gagné ou perdu selon les drapeaux placés
    def fini_ou_non(self):
        grilliade = self
        a = grilliade.matrice
        ou_drapeau = np.where(a == 'D')
        liste_drapeau = [list(x) for x in zip(ou_drapeau[0], ou_drapeau[1])]
        k = 0
        for l in liste_drapeau:
            if l in grilliade.liste_bombe:
                k += 1
            if k == len(grilliade.liste_bombe):
                print("Vous avez gagné")
                return True
        else:
            return False

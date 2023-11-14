"""
CLASSE FENETRE_JEU

Cette classe est la classe où il y aura l'interaction de jeu et la grille du démineur visualisée.

Cette classe hérite de la classe QWidget pour hériter des propriétés créant l'interface graphique.

Attributs :
        + joueur
        + fenetre_final
        + etat            (caractérise si le joueur doit encore jouer ou s'il a fini de jouer)
        + difficulte
        + buttons           (tous les boutons qui définissent la grille)
"""

from PyQt5.QtWidgets import QGridLayout, QPushButton, QWidget, QLabel
from PyQt5.QtCore import Qt
from fenetre_fin import final_fenetre

class jeu_action(QWidget):
    def __init__(self, difficulte, joueur, final_window):

        # Héritage des fonctionnalités et attributs de QWidget
        super().__init__()

        # Définition des attributs de la classe
        self.joueur = joueur
        self.final_window = final_window 
        self.etat = False
        self.difficulte = difficulte
        self.buttons = {}

        # Définition des propriétés de notre fenêtre de jeu : Titre, taille
        self.setWindowTitle("Fenêtre de Jeu")
        self.resize(500, 500)

        self.layout = QGridLayout()

        # Définition de la taille de la grille à afficher selon la difficulté
        if (self.difficulte == 1):
            max = 5
        if (self.difficulte == 2):
            max = 10
        if (self.difficulte == 3):
            max = 20

        # Mise en place des boutons qui représenteront les cases de la grille
        for x in range(0, max):
            for y in range(0, max):
                button = QPushButton('?')        # Les boutons neutres auront le texte '?'
                coords = (x, y)                  # Coordonnées du bouton dans la grille 
                button.setFixedSize(50, 50)

                # Event listener quand on clique sur le bouton pour d'abord définir la case de départ 
                button.clicked.connect(lambda _, coords=coords, btn=button: self.appui_bouton_case_depart(coords[0], coords[1], btn, joueur))
                button.setStyleSheet("background-color: grey ; color: white;")
                # Ajout des boutons dans la fenêtre
                self.layout.addWidget(button, x, y)
                self.buttons[coords] = button

        # Mise à jour du layout de la fenêtre
        self.setLayout(self.layout)

    # Fonction qui permet de définir la grille selon le bouton coché au début qui représente la case de départ
    def appui_bouton_case_depart(self, x, y, button, joueur):
        button.setText("X")
        # Mise à jour du joueur avec son attribut de case de départ selon les coordonnées du bouton cliqué
        joueur.choix_case_depart(x, y)

        # Récupération de la grille alors générée à la suite du choix de la case de départ
        mat = joueur.grille.matrice

        # Affichage du nombre de bombe de la case de départ
        self.actualiser_texte_bouton(x, y, str(mat[x, y]))

        # Enlève l'event listener du bouton de la case de départ
        button.clicked.disconnect()

        # Récupération des coordonnées des boutons non choisis
        for other_coords, other_button in self.buttons.items():
            if other_coords != (x, y):  # On ne le fait pas pour le bouton de la case de départ

                coords = other_coords

                if mat[coords[0], coords[1]] != 'O':   # On regarde que les boutons dont on doit afficher un chiffre
                    self.actualiser_texte_bouton(coords[0], coords[1], str(mat[coords[0], coords[1]]))

                # Définition d'une nouvelle fonction event listener selon clic droit ou clic gauche pour chaque bouton
                other_button.clicked.disconnect()
                other_button.clicked.connect(lambda _, coords=other_coords, btn=other_button, ev=Qt.LeftButton: self.appui_bouton(coords[0], coords[1], btn, ev, joueur))
                other_button.setContextMenuPolicy(Qt.CustomContextMenu)
                other_button.customContextMenuRequested.connect(lambda _, coords=other_coords, btn=other_button, ev=Qt.RightButton: self.appui_bouton(coords[0], coords[1], btn, ev, joueur))
                other_button.setStyleSheet("background-color: grey ; color: white;")

        self.actualiser_grille(joueur)

    # Définition des actions de jeu : déminer, mettre un drapeau quand on clique sur un bouton selon gauche ou droite 
    def appui_bouton(self, x, y, button, event_button, joueur):

        if event_button == Qt.LeftButton:

            joueur.mettre_drapeau(x, y)  # Si clic droit, mise de drapeau

            if button.text() == 'D' or button.text() == '?':      # Ne pas mettre de drapeau sur les boutons avec un nombre
                if button.text() == 'D':
                    self.actualiser_texte_bouton(x, y, '?')      # On enlève le drapeau dans l'affichage de la grille
                    joueur.grille.matrice[x, y] == 'O'
                    button.setStyleSheet("background-color: grey ; color: white;")
                elif self.contains_integer(button.text()):
                    button.setStyleSheet("background-color: purple ; color: white;")
                else:
                    self.actualiser_texte_bouton(x, y, 'D')          # Mise à jour de l'affichage de la grille  
                    button.setStyleSheet("background-color: green ; color: white;") 

            self.etat = joueur.fini()   # Test pour voir si le jeu est fini ou non 

        elif event_button == Qt.RightButton: 

            joueur.mettre_bombe(x, y)           # Si clic gauche, démine

            if button.text() == 'B' or button.text() == '?':  # Ne pas déminer sur les boutons avec un nombre
                self.actualiser_texte_bouton(x, y, 'B')  # Mise à jour de l'affichage de la grille
                button.setStyleSheet("background-color: red; color: white;")

            self.etat = joueur.fini()   # Test pour voir si le jeu est fini ou non 

        if self.etat:                # Si True, le jeu est fini 
            self.final_window.update_score(joueur.etat_jeu)   # Affichage de la fenêtre de fin avec le résultat   
            self.final_window.show()

        self.actualiser_grille(joueur)

    def actualiser_grille(self, joueur):
        mat = joueur.grille.matrice

        for i in range(joueur.grille.nombre_ligne):
            for j in range(joueur.grille.nombre_colonne):
                if str(mat[i, j]) == 'O':
                    self.actualiser_texte_bouton(i, j, '?')
                else:
                    self.actualiser_texte_bouton(i, j, str(mat[i, j]))

                if [i, j] in joueur.grille.liste_bombe and str(mat[i, j]) != 'D':
                    self.actualiser_texte_bouton(i, j, '?')

    def contains_integer(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    # Définition de la fonction qui change le texte d'un bouton 
    def actualiser_texte_bouton(self, x, y, text):
        button = self.buttons[(x, y)]
        button.setText(text)

        if self.contains_integer(text):
            button.setStyleSheet("background-color: purple ; color: white;")

        if text == 'D':
            button.setStyleSheet("background-color: green ; color: white;")

        if text == '?':
            button.setStyleSheet("background-color: grey ; color: white;")

        if text == 'B':
            button.setStyleSheet("background-color: red ; color: white;")

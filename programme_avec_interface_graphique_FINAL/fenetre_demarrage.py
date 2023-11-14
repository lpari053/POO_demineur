"""
CLASSE FENETRE_DEMARRAGE

Cette classe est la classe qui doit être lancée pour démarrer le jeu du démineur.

Elle contient la définition de la fenêtre de départ,
                            de la fenêtre de jeu,
                            de la fenêtre finale
                        mais aussi définit le joueur.

Cette classe hérite de la classe QWidget pour hériter des propriétés créant l'interface graphique.

Attributs :
        + joueur
        + fenetre_final
"""

# Importation des bibliothèques et des fichiers dont on a besoin
import sys
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget, QPushButton, QApplication, QComboBox

from fenetre_jeu import jeu_action      # Importation de la classe qui définit l'interface de la grille de jeu
from joueur_interface import Joueur     # Importation de la classe qui définit un joueur et ses actions
from fenetre_fin import final_fenetre   # Importation de la fenêtre finale du jeu

class FenetreDemarrage(QWidget):                 # Définition de la classe FenetreDemarrage qui hérite de QWidget
    def __init__(self):
        # Héritage des fonctionnalités et attributs de QWidget
        super().__init__()

        # Définition des attributs de la classe
        self.joueur = Joueur()    # Initialisation de notre Joueur
        self.final_window = final_fenetre("")  # Initialisation de notre fenêtre finale qui ne comporte pas encore de score/résultat

        # Définition des propriétés de notre fenêtre de démarrage : Titre, taille
        self.setWindowTitle("Fenêtre de Démarrage")
        self.resize(300, 150)

        # Définition de notre layout vertical pour afficher les labels et boutons de notre fenêtre
        layout = QVBoxLayout()

        # Définition de notre label d'introduction
        label = QLabel("Bonjour, bienvenue dans Démineur.\nVeuillez choisir une difficulté de jeu :")
        layout.addWidget(label)

        # Définition de notre menu déroulant pour choisir la difficulté
        qcombo = QComboBox()
        qcombo.addItems(["Facile", "Moyen", "Difficile"])  # Possibilités de difficulté
        layout.addWidget(qcombo)

        # Définition de notre bouton pour commencer à démarrer le jeu après choix de la difficulté
        demarrer_button = QPushButton("Démarrer")
        demarrer_button.clicked.connect(lambda: self.ouvrir_fenetre_jeu(qcombo.currentIndex()))  # Ajout d'événement quand appui bouton
        layout.addWidget(demarrer_button)

        # Mise à jour du layout de notre fenêtre
        self.setLayout(layout)

    # Définition de la fonction quand on appuie sur le bouton démarrer
    def ouvrir_fenetre_jeu(self, difficulte):
        # On cache la fenêtre de démarrage
        self.hide()

        # Mise à jour du profil du joueur en lui attribuant la difficulté choisie à l'aide de la fonction définie dans la classe joueur_interface
        self.joueur.choix_difficulte(int(difficulte) + 1)

        # Définition de notre fenêtre de jeu qui comportera la grille pour pouvoir l'afficher après l'appui sur le bouton et donc le choix de la difficulté
        fenetre_jeu = jeu_action(int(difficulte) + 1, self.joueur, self.final_window)
        # Affichage de notre fenêtre de jeu
        fenetre_jeu.show()

if __name__ == '__main__':
    # Initialisation de notre application PyQt
    app = QApplication(sys.argv)

    # Initialisation de notre fenêtre de démarrage
    fenetre_demarrage = FenetreDemarrage()
    # Affichage de notre fenêtre de démarrage
    fenetre_demarrage.show()

    # Mise en place de la sortie du code quand l'application est fermée
    sys.exit(app.exec_())

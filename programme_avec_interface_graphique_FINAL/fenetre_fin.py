"""
CLASSE FENETRE_FIN

Cette classe est la classe de fin de jeu qui affiche simplement si le joueur a perdu ou gagné.

Cette classe hérite de la classe QWidget pour hériter des propriétés créant l'interface graphique.

Attribut :
        + score   (selon l'attribut etat_jeu du joueur)
"""

from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget
from PyQt5.QtCore import Qt

class final_fenetre(QWidget):
    def __init__(self, score):
        super().__init__()

        # Définition de l'attribut présentant le résultat du jeu
        self.score = score

        # Définition de la taille et du titre de la fenêtre de fin de jeu 
        self.setWindowTitle("Résultat")
        self.resize(300, 100)

        layout = QVBoxLayout()

        # Ajout du label de résultat
        self.label = QLabel(score)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        self.setLayout(layout)
    
    # Fonction qui change les scores selon l'état du jeu
    def update_score(self, score):
        self.label.setText(str.upper(str(score)))
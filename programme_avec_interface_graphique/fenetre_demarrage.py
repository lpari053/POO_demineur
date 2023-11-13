# fichier_demarrage.py
import sys
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget, QPushButton, QApplication, QComboBox
from fenetre_choix_case_depart import class_choix  # Importe la classe MaFenetre depuis l'autre fichier
from joueur_interface import Joueur
from fenetre_fin import final_fenetre


class FenetreDemarrage(QWidget):
    def __init__(self):
        super().__init__()

        self.joueur=Joueur()

        self.final_window = final_fenetre("")

        self.setWindowTitle("Fenetre de Demarrage")
        self.resize(300, 150)

        layout = QVBoxLayout()

        label = QLabel("Choisissez la difficulte:")
        layout.addWidget(label)

        qcombo = QComboBox()
        qcombo.addItems(["Facile", "Moyen", "Difficile"])
        layout.addWidget(qcombo)

        demarrer_button = QPushButton("Demarrer")
        demarrer_button.clicked.connect(lambda: self.ouvrir_fenetre_jeu(qcombo.currentIndex()))
        layout.addWidget(demarrer_button)

        self.setLayout(layout)

    def ouvrir_fenetre_jeu(self, difficulte):
        self.hide()  # Cache la fenêtre de démarrage

        self.joueur.choix_difficulte(int(difficulte)+1)

        fenetre_jeu = class_choix(int(difficulte)+1,self.joueur,self.final_window)
        fenetre_jeu.show()  # Affiche la fenêtre de jeu



if __name__ == '__main__':
    app = QApplication(sys.argv)

    fenetre_demarrage = FenetreDemarrage()
    fenetre_demarrage.show()

    sys.exit(app.exec_())

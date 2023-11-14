# fenetre_jeu.py
from PyQt5.QtWidgets import QGridLayout, QPushButton, QWidget
from joueur_interface_graphique import Joueur
class MaFenetre(QWidget):
    def __init__(self, difficulte):
        super().__init__()

        joueur=Joueur()

        self.setWindowTitle("Fenetre de Jeu")
        self.resize(500, 250)

        self.difficulte = difficulte

        joueur.grille.difficulte=difficulte

        layout = QGridLayout()

        for x in range(0, 5):
            for y in range(0, 5):
                button = QPushButton('?')
                button.clicked.connect(lambda _, x=x, y=y: self.appui_bouton(x, y))
                layout.addWidget(button, x, y)

        self.setLayout(layout)

    def appui_bouton(self, x, y):
        print(f'Appui sur le bouton en position ({x}, {y})')



if __name__ == '__main__':
    # Ce bloc ne sera exécuté que si ce fichier est exécuté directement
    # Vous pouvez y ajouter un code supplémentaire si nécessaire
    pass

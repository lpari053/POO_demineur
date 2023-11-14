"""""
CLASSE FENETRE_FIN

Cette classe est la classe de fin de jeu qui affihe juste si le joueur a perdu ou gagne

Cette classe herite de la classe QWIdget pour heriter des proprietes creant l'interface graphique

Attribut :

        + score   (selon l'attribut etat_jeu du joueur)


"""""



from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget, QPushButton
from PyQt5.QtCore import Qt

class final_fenetre(QWidget):
    def __init__(self, score):
        super().__init__()

        #definiton de l'attribut presentant le resultat du jeu
        self.score = score

        #definiton taille et titre de la fenetre de fin de jeu 
        self.setWindowTitle("Résultat")
        self.resize(300, 100)

        layout = QVBoxLayout()

        #ajout du label de resultat
        self.label = QLabel(score)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        self.setLayout(layout)
    
    #fonction qui change les score selon etat du jeu
    def update_score(self, score):
        self.label.setText(str.upper(str(score)))
        print('coucou')

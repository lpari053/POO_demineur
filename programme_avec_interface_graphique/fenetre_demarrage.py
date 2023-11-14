"""""
CLASSE FENETRE_DEMARRAGE

Cette classe est la classe qui devra etre lancé pour demarrer le jeu du demineur.

Elle contient la definiton de la fenetre de depart , 
                            de la fenetre de jeu , 
                            de la fenetre final 
                        mais aussi defini le joueur


Cette classe herite de la classe QWIdget pour heriter des proprietes créant l'interface graphique


Attribut :
        + joueur
        + fenetre_final

"""""

#Importation des bibliteque et des fichiers que l'ont a besoin 

import sys
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget, QPushButton, QApplication, QComboBox


from fenetre_jeu import jeu_action      #Importation de la classe qui defini l'interface de grille de jeu
from joueur_interface import Joueur                       # Importation de la classe qui definit un joueur et ses actions
from fenetre_fin import final_fenetre           # Importation de la fenetre final du jeu


class FenetreDemarrage(QWidget):                 #Defintion de la classe FenetreDemarrage qui herite de Qwidget
    def __init__(self):

        #Heritage des fonctionnalite et attribut de QWidget
        super().__init__()


        #Definition des attributs de la classe


        self.joueur=Joueur()    #Initialisation de notre Joueur

        self.final_window = final_fenetre("")  #Initialisation de notre fenetre final qui ne comporte pas encore de score/resultat


        #definition des proprietes de notre fenetre de demarrage : Titre , taille 
        self.setWindowTitle("Fenetre de Demarrage")
        self.resize(300, 150)

        #definiton de notre layout vertical pour afficher les label et boutons de notre fenetre 
        layout = QVBoxLayout()

        #definiton de notre label d'introduction
        label = QLabel("BOnjour Bienvenue dans Demineur \n Veuillez choisir une difficulté de jeu:")
        layout.addWidget(label)

        #definiton de notre menu deroulant pour choisir la difficulté
        qcombo = QComboBox()
        qcombo.addItems(["Facile", "Moyen", "Difficile"])  #Posiibilite de difficulte
        layout.addWidget(qcombo)


        #defintion de notre bouton pour commencer a demarrer le jeu apres choix de la difficulte
        demarrer_button = QPushButton("Demarrer")
        demarrer_button.clicked.connect(lambda: self.ouvrir_fenetre_jeu(qcombo.currentIndex()))  #Ajoute d'evenment quand appui bouton
        layout.addWidget(demarrer_button)

        #Mise a jour du layout de notre fenetre
        self.setLayout(layout)


    #definiton de la fonction quand on appuie sur le bouton demarrer
    def ouvrir_fenetre_jeu(self, difficulte):

        #On cache la fenetre de demarrage
        self.hide() 

        #Mise a joueur du profiul du joeur en lui attribuant la difficulte choisi a l'aide fonction defini dans classe joueur_interface
        self.joueur.choix_difficulte(int(difficulte)+1)


        #Definition de notre fenetre de jeu qui comportera la grille pour pouvoir l'afficher apres l'appui sur bouton et donc choix de la difficulté
        fenetre_jeu = jeu_action(int(difficulte)+1,self.joueur,self.final_window)
        #Affichage de notre fenetre de jeu
        fenetre_jeu.show() 



if __name__ == '__main__':

    #Initialisation de notre application PyQt
    app = QApplication(sys.argv)


    #Initialisation de notre fenetre de demarrage
    fenetre_demarrage = FenetreDemarrage()  
    #Affichage de notre fenetre de demarrage
    fenetre_demarrage.show()


    #Mise en place de sortie du code quand ferme application
    sys.exit(app.exec_())

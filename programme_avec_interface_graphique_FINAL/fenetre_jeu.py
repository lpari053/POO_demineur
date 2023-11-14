"""""
CLASSE FENETRE_JEU

Cette classe est la classe ou il y aura l'iteraction de jeu et la grille du demineur visualiser.

Cette classe herite de la classe QWIdget pour heriter des proprietes creant l'interface graphique

Attribut :

        + joueur
        + fenetre_final
        + etat            (caracterise si le joueur doit encore jouer ou si fini de jouer)
        + diffcilute
        + buttons           (tous le sbouons qui definissent la grille)


"""""



from PyQt5.QtWidgets import QGridLayout, QPushButton, QWidget,QLabel
from PyQt5.QtCore import Qt
from fenetre_fin import final_fenetre

class jeu_action(QWidget):
    def __init__(self, difficulte, joueur, final_window):

        #Heritage des fonctionnalite et attribut de QWidget
        super().__init__()


        #Definition des attributs de la classe
        self.joueur = joueur
        self.final_window = final_window 
        self.etat = False
        self.difficulte = difficulte
        self.buttons = {}


        #definition des proprietes de notre fenetre de demarrage : Titre , taille <
        self.setWindowTitle("Fenetre de Jeu")
        self.resize(500, 500)

        self.layout = QGridLayout()

        #definition de la taille de la grille a afficher selon la difficulte
        if (self.difficulte==1):
            max=5
        if (self.difficulte==2):
            max=10
        if (self.difficulte==3):
            max=20


        #mise en place des boutons qui representeront les cases de la grille
        for x in range(0, max):
            for y in range(0, max):
                button = QPushButton('?')        #les boutons neutre auront texte ?
                coords = (x, y)                  #coorodnne du bouton dans la grille 
                button.setFixedSize(50, 50)

                #event listener quand on click sur le bouton pour d'abord definir la case de depart 
                button.clicked.connect(lambda _, coords=coords, btn=button: self.appui_bouton_case_depart(coords[0], coords[1], btn, joueur))
                button.setStyleSheet("background-color: grey ; color: white;")
                #ajout des bouton dans la fenetre
                self.layout.addWidget(button, x, y)
                self.buttons[coords] = button

        #mise a jour du layout de la fenetre
        self.setLayout(self.layout)


    #fonction qui permet de definir la grille selon le bouton cocher au debut qui represente la case depart
    def appui_bouton_case_depart(self, x, y, button, joueur):
        # print(f'Appui sur le bouton en position ({x}, {y})')

        button.setText("X")
        #mise jur du joueur avce son attribut de case depart selon coordonne du buton cliquer
        joueur.choix_case_depart(x, y)

        #recuperation de la grille alors generer a la suit du choix de la case depart
        mat=joueur.grille.matrice

        #affichage nombre de bombe de la case depart
        self.actualiser_texte_bouton(x,y, str(mat[x,y]))

        #enleve l'event listener du bouton de la case depart
        button.clicked.disconnect()

        #recuperation des coordonnées des boutons non choisi
        for other_coords, other_button in self.buttons.items():
            if other_coords != (x, y):  #on ne le fait pas pour le bouton de la case depart

                coords=other_coords

                if mat[coords[0], coords[1]]!='O':   #on regarde que les boutons dont on doit afficher un chiffre
                    self.actualiser_texte_bouton(coords[0], coords[1], str(mat[coords[0], coords[1]]))

                #definition d'une nouvelle fonction event listener selon clic droit ou clic gauche pour chaque bouton
                other_button.clicked.disconnect()
                other_button.clicked.connect(lambda _, coords=other_coords, btn=other_button, ev=Qt.LeftButton: self.appui_bouton(coords[0], coords[1], btn, ev, joueur))
                other_button.setContextMenuPolicy(Qt.CustomContextMenu)
                other_button.customContextMenuRequested.connect(lambda _, coords=other_coords, btn=other_button, ev=Qt.RightButton: self.appui_bouton(coords[0], coords[1], btn, ev, joueur))
                other_button.setStyleSheet("background-color: grey ; color: white;")


        self.actualiser_grille(joueur)



    #definiton des actions de jeu deminer mettre un drapeau quand on clic sur un bouton selon gaiche ou droite 
    def appui_bouton(self, x, y, button, event_button, joueur):
        # print(f'Appui sur le bouton en position ({x}, {y})')

        if event_button == Qt.LeftButton:

            joueur.mettre_drapeau(x, y)  #si clic droit mise de drapeau

            if button.text()=='D' or button.text()=='?':      #ne pas mettre de drapeau sur les boutons avec nombre
                print(button.text()=='D')
                if button.text()=='D':

                    self.actualiser_texte_bouton(x, y,'?')      #on enleve le drapeau dans affichage de la grille
                    joueur.grille.matrice[x,y]=='O'

                    button.setStyleSheet("background-color: grey ; color: white;")

                elif self.contains_integer(button.text()):
                    button.setStyleSheet("background-color: purple ; color: white;")
                
                else:

                    self.actualiser_texte_bouton(x, y, 'D')          #mise a jour affichage de la grille  
                    button.setStyleSheet("background-color: green ; color: white;") 


            self.etat = joueur.fini()   #test pour voir si le jeu est fini ou non 

        elif event_button == Qt.RightButton: 

            joueur.mettre_bombe(x, y)           #si clic gauche on demine 

            if button.text()=='B' or button.text()=='?':  #ne pas deminer sur les boutons avec nombre

                self.actualiser_texte_bouton(x, y, 'B')  #mise a jour affichage de la grille

                button.setStyleSheet("background-color: red; color: white;")

            self.etat = joueur.fini()   #test pour voir si le jeu est fini ou non 

        if self.etat:                #si True nous avons fini le jeu 
            # self.hide()  #on enleve la fenetre de jeu

            print(joueur.etat_jeu)

            self.final_window.update_score(joueur.etat_jeu)   #affichage de la fenetre d efin avec resultat   
            self.final_window.show()

        self.actualiser_grille(joueur)

    

    def actualiser_grille(self,joueur):

        print(joueur.grille.liste_bombe)


        mat=joueur.grille.matrice

        for i in range(joueur.grille.nombre_ligne):

            for j in range(joueur.grille.nombre_colonne):

                if  str(mat[i,j])=='O':
                    
                    self.actualiser_texte_bouton(i, j,'?')

                else:

                    self.actualiser_texte_bouton(i, j, str(mat[i,j]))

                if [i,j] in joueur.grille.liste_bombe and str(mat[i,j])!='D':
                    self.actualiser_texte_bouton(i, j, '?')

                



    def contains_integer(self,s):
        try:
            int(s)
            return True
        except ValueError:
            return False

   #definiton de la fonction qui change le texte d'un bouton 
    def actualiser_texte_bouton(self, x, y, text):
        button = self.buttons[(x, y)]
        button.setText(text)

        if self.contains_integer(text):
            button.setStyleSheet("background-color: purple ; color: white;")

        if text=='D':
            button.setStyleSheet("background-color: green ; color: white;")

        if text=='?':
            button.setStyleSheet("background-color: grey ; color: white;")

        if text=='B':
            button.setStyleSheet("background-color: red ; color: white;")





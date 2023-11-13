# class_choix.py
from PyQt5.QtWidgets import QGridLayout, QPushButton, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from fenetre_fin import final_fenetre

class class_choix(QWidget):
    def __init__(self, difficulte, joueur, final_window):
        super().__init__()

        self.joueur = joueur
        self.final_window = final_window  # Store the reference to the final window
        self.etat = False

        self.setWindowTitle("Fenetre de Jeu")
        self.resize(500, 250)

        self.difficulte = difficulte

        layout = QGridLayout()

        self.buttons = {}

        if (self.difficulte==1):
            

            max=5
                
        if (self.difficulte==2):
            
            max=10
            
            
        if (self.difficulte==3):

            max=20

        for x in range(0, max):
            for y in range(0, max):
                button = QPushButton('?')
                coords = (x, y)
                button.clicked.connect(lambda _, coords=coords, btn=button: self.appui_bouton_case_depart(coords[0], coords[1], btn, joueur))
                layout.addWidget(button, x, y)
                self.buttons[coords] = button

        self.setLayout(layout)

    def appui_bouton_case_depart(self, x, y, button, joueur):
        print(f'Appui sur le bouton en position ({x}, {y})')

        button.setText("X")
        joueur.choix_case_depart(x, y)

        mat=joueur.grille.matrice

        print(mat)


        button.clicked.disconnect()

        for other_coords, other_button in self.buttons.items():
            if other_coords != (x, y):

                coords=other_coords

                if mat[coords[0], coords[1]]!='O':
                    self.actualiser_texte_bouton(coords[0], coords[1], str(mat[coords[0], coords[1]]))

                other_button.clicked.disconnect()
                other_button.clicked.connect(lambda _, coords=other_coords, btn=other_button, ev=Qt.LeftButton: self.appui_bouton(coords[0], coords[1], btn, ev, joueur))
                other_button.setContextMenuPolicy(Qt.CustomContextMenu)
                other_button.customContextMenuRequested.connect(lambda _, coords=other_coords, btn=other_button, ev=Qt.RightButton: self.appui_bouton(coords[0], coords[1], btn, ev, joueur))





    def appui_bouton(self, x, y, button, event_button, joueur):
        # print(f'Appui sur le bouton en position ({x}, {y})')

        if event_button == Qt.LeftButton:
            # print("Clic gauche")

            joueur.mettre_drapeau(x, y)
            self.actualiser_texte_bouton(x, y, 'D')

            self.etat = joueur.fini()

        elif event_button == Qt.RightButton:
            # print("Clic droit")

            joueur.mettre_bombe(x, y)
            self.actualiser_texte_bouton(x, y, 'B')

            self.etat = joueur.fini()

        if self.etat:
            self.hide()

            # Use the existing instance of final_fenetre
            self.final_window.update_score(joueur.etat_jeu)
            self.final_window.show()  # Show the final window


    def actualiser_texte_bouton(self, x, y, text):
        button = self.buttons[(x, y)]
        button.setText(text)

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout ,QHBoxLayout,QLabel


app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv)

fen = QWidget()


label = QLabel("Voici mon premier texte avec un QLabel")
label.show()


fen.setWindowTitle("Premiere fenetre")

fen.resize(500,250)

fen.move(300,50)

def appui_bouton():
    print("Appui sur le bouton")
    
    
bouton_demarrer = QPushButton("Demarrer")

bouton_demarrer.clicked.connect(appui_bouton)

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(bouton_demarrer)


fen.setLayout(layout)

fen.show()
app.exec_()
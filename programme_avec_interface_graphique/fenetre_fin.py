# fenetre_fin.py
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget, QPushButton
from PyQt5.QtCore import Qt

class final_fenetre(QWidget):
    def __init__(self, score):
        super().__init__()

        self.score = score

        self.setWindowTitle("Résultat")
        self.resize(300, 100)

        layout = QVBoxLayout()

        self.label = QLabel(score)
        layout.addWidget(self.label)

        close_button = QPushButton("Fermer")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)

    def update_score(self, score):
        self.label.setText(score)

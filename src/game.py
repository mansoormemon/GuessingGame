import random as rndm
from time import time

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QPushButton,
    QGridLayout,
    QLineEdit,
    QLabel,
    QMessageBox
)


class Game(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set boundaries.
        self.min = 1
        self.max = 20

        # Generate a random number.
        rndm.seed(time())
        self.answer = rndm.randint(self.min, self.max)
        print('Answer:', self.answer)

        # Set window attributes.
        self.setFixedSize(QSize(480, 120))
        self.setWindowTitle('Guessing Game')

        # Set the central widget.
        central_wgt = QWidget()
        self.setCentralWidget(central_wgt)

        # Set layout of the central widget.
        self.grid = QGridLayout()
        central_wgt.setLayout(self.grid)

        # Add a description message.
        msg = QLabel(f'Guess a number between {self.min} and {self.max}:')
        self.grid.addWidget(msg)

        # Add an input box to the grid.
        self.line_edt = QLineEdit()
        # Set input validator.
        self.line_edt.setValidator(QIntValidator())
        self.grid.addWidget(self.line_edt)

        # Add a button to the grid.
        button = QPushButton('Check')
        button.clicked.connect(self.verify_guess)
        self.grid.addWidget(button)

        # Click button when enter is pressed.
        self.line_edt.returnPressed.connect(button.click)

    def verify_guess(self):
        text = self.line_edt.text()
        if not text:
            return
        guess = int(text)

        # Display an appropriate message based on user's input.
        dialog = QMessageBox()
        if guess == self.answer:
            dialog.setText('Congratulations, you guessed it!')
        else:
            dialog.setText('Whoops, wrong answer!')
        dialog.exec()

        self.line_edt.clear()
        self.line_edt.setFocus()

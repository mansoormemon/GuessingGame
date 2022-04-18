import sys

from PyQt6.QtCore import QFile
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget, QVBoxLayout

from game import *

app = QApplication(sys.argv)

with open('/home/mansoorahmed/OSS/GuessingGame/src/res/style.qss') as file:
    stylesheet = file.read()
    app.setStyleSheet(stylesheet)

my_game = Game()
my_game.show()

sys.exit(app.exec())

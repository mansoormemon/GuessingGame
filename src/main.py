import sys

from PyQt6.QtWidgets import QApplication

from game import *


app = QApplication(sys.argv)

my_game = Game()
my_game.show()

sys.exit(app.exec())

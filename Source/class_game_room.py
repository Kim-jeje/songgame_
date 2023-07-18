import sys

from PyQt5.QtWidgets import QApplication, QWidget

from ui.ui_game_room import Ui_gameroom

class GameRoom(QWidget, Ui_gameroom):
    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller
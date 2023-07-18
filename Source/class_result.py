import sys

from PyQt5.QtWidgets import QApplication, QWidget

from ui.ui_result import Ui_result

class Result(QWidget, Ui_result):
    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller
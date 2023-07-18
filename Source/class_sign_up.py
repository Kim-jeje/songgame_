import sys

from PyQt5.QtWidgets import QApplication, QWidget

from ui.ui_sign_up import Ui_signup

class SignUp(QWidget, Ui_signup):
    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller
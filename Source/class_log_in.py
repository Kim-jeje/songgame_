import sys

from PyQt5.QtWidgets import QApplication, QWidget

from ui.ui_log_in import Ui_login

class LogIn(QWidget, Ui_login):
    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = LogIn()
#     ex.show()
#     sys.exit(app.exec_())
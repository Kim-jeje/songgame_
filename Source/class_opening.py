import sys

from PyQt5.QtWidgets import QApplication, QWidget

from ui.ui_opening import Ui_opening

class Opening(QWidget, Ui_opening):
    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller
        self.login_btn.clicked.connect(self.gotologin)
        self.signup_btn.clicked.connect(self.gotosignup)

    def gotologin(self):
        # self.close()
        self.controller.login.show()

    def gotosignup(self):
        self.controller.signup.show()

    # def close(self):
    #     self.controller.close()
    #     super().close()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Opening()
    ex.show()
    sys.exit(app.exec_())
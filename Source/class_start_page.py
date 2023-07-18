import sys

from PyQt5.QtWidgets import QApplication, QWidget

from ui.ui_start_page import Ui_startpage

class StartPage(QWidget, Ui_startpage):
    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
# #     ex = StartPage()
# #     ex.show()
# #     sys.exit(app.exec_())
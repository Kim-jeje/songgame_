import sys

from PyQt5 import QtCore, QtWidgets

import Source.class_main_controller

def main():
    app = QtWidgets.QApplication(sys.argv)

    main_controller = Source.class_main_controller.MainController()
    main_controller.opening.show()
    # main_controller.login.show()
    # main_controller.signup.show()
    # main_controller.start_page.show()
    # main_controller.game_room.show()
    # main_controller.result.show()
    app.exec_()

if __name__ == '__main__':
    main()
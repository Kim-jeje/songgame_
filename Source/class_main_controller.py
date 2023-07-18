from PyQt5.QtWidgets import QWidget

from Source.class_start_page import StartPage
from Source.class_opening import Opening
from Source.class_log_in import LogIn
from Source.class_sign_up import SignUp
from Source.class_game_room import GameRoom
from Source.class_result import Result

class MainController(QWidget):
    def __init__(self):
        super().__init__()
        self.opening = Opening(self)
        self.login = LogIn(self)
        self.signup = SignUp(self)
        self.start_page = StartPage(self)
        self.game_room = GameRoom(self)
        self.result = Result(self)

    def close(self):
        self.opening.close()
        self.login.close()
        self.signup.close()
        self.start_page.close()
        self.game_room.close()
        self.result.close()

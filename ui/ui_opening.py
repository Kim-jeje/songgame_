# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/opening.ui'
#
# Created by: PyQt5 UI Source generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_opening(object):
    def setupUi(self, opening):
        opening.setObjectName("opening")
        opening.resize(900, 600)
        self.frame = QtWidgets.QFrame(opening)
        self.frame.setGeometry(QtCore.QRect(0, 0, 900, 600))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(270, 80, 371, 71))
        self.label.setStyleSheet("font: 36pt \"Amiri Quran\";")
        self.label.setObjectName("label")
        self.login_btn = QtWidgets.QPushButton(self.frame)
        self.login_btn.setGeometry(QtCore.QRect(220, 370, 171, 81))
        self.login_btn.setObjectName("login_btn")
        self.signup_btn = QtWidgets.QPushButton(self.frame)
        self.signup_btn.setGeometry(QtCore.QRect(490, 370, 161, 81))
        self.signup_btn.setObjectName("signup_btn")

        self.retranslateUi(opening)
        QtCore.QMetaObject.connectSlotsByName(opening)

    def retranslateUi(self, opening):
        _translate = QtCore.QCoreApplication.translate
        opening.setWindowTitle(_translate("opening", "Form"))
        self.label.setText(_translate("opening", "노래 맞히기 게임"))
        self.login_btn.setText(_translate("opening", "로그인"))
        self.signup_btn.setText(_translate("opening", "회원가입"))

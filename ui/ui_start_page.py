# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/start_page.ui'
#
# Created by: PyQt5 UI Source generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_startpage(object):
    def setupUi(self, startpage):
        startpage.setObjectName("startpage")
        startpage.resize(900, 600)
        self.frame = QtWidgets.QFrame(startpage)
        self.frame.setGeometry(QtCore.QRect(0, 0, 900, 600))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(270, 80, 371, 71))
        self.label.setStyleSheet("font: 36pt \"Amiri Quran\";")
        self.label.setObjectName("label")
        self.start_btn = QtWidgets.QPushButton(self.frame)
        self.start_btn.setGeometry(QtCore.QRect(220, 370, 171, 81))
        self.start_btn.setObjectName("start_btn")
        self.rank_btn = QtWidgets.QPushButton(self.frame)
        self.rank_btn.setGeometry(QtCore.QRect(490, 370, 161, 81))
        self.rank_btn.setObjectName("rank_btn")

        self.retranslateUi(startpage)
        QtCore.QMetaObject.connectSlotsByName(startpage)

    def retranslateUi(self, startpage):
        _translate = QtCore.QCoreApplication.translate
        startpage.setWindowTitle(_translate("startpage", "Form"))
        self.label.setText(_translate("startpage", "노래 맞히기 게임"))
        self.start_btn.setText(_translate("startpage", "게임시작"))
        self.rank_btn.setText(_translate("startpage", "랭킹"))
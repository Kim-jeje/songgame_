# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/result.ui'
#
# Created by: PyQt5 UI Source generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_result(object):
    def setupUi(self, result):
        result.setObjectName("result")
        result.resize(900, 600)
        self.label = QtWidgets.QLabel(result)
        self.label.setGeometry(QtCore.QRect(180, 190, 581, 151))
        self.label.setStyleSheet("font: 16pt \"Alef\";\n"
"font: 22pt \"Alef\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(result)
        self.label_2.setGeometry(QtCore.QRect(210, 40, 511, 71))
        self.label_2.setStyleSheet("font: 22pt \"Alef\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(result)
        self.pushButton.setGeometry(QtCore.QRect(380, 470, 181, 61))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(result)
        QtCore.QMetaObject.connectSlotsByName(result)

    def retranslateUi(self, result):
        _translate = QtCore.QCoreApplication.translate
        result.setWindowTitle(_translate("result", "Form"))
        self.label.setText(_translate("result", "00님이 이겼습니다."))
        self.label_2.setText(_translate("result", "게임 결과"))
        self.pushButton.setText(_translate("result", "나가기"))

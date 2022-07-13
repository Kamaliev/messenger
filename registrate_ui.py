# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\exporter\registrate.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(376, 305)
        Dialog.setFocusPolicy(QtCore.Qt.WheelFocus)
        Dialog.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.first_name = QtWidgets.QLineEdit(Dialog)
        self.first_name.setGeometry(QtCore.QRect(120, 60, 113, 20))
        self.first_name.setObjectName("first_name")
        self.last_name = QtWidgets.QLineEdit(Dialog)
        self.last_name.setGeometry(QtCore.QRect(120, 90, 113, 20))
        self.last_name.setObjectName("last_name")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 60, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 71, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 220, 111, 23))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_2.setObjectName("pushButton_2")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(120, 150, 113, 20))
        self.password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.password2 = QtWidgets.QLineEdit(Dialog)
        self.password2.setGeometry(QtCore.QRect(120, 180, 113, 20))
        self.password2.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.password2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password2.setObjectName("password2")
        self.login = QtWidgets.QLineEdit(Dialog)
        self.login.setGeometry(QtCore.QRect(120, 120, 113, 20))
        self.login.setObjectName("login")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 120, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 150, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 180, 71, 16))
        self.label_6.setObjectName("label_6")
        self.password_match = QtWidgets.QLabel(Dialog)
        self.password_match.setEnabled(True)
        self.password_match.setGeometry(QtCore.QRect(240, 180, 111, 16))
        self.password_match.setStyleSheet("color: red\n"
"")
        self.password_match.setScaledContents(False)
        self.password_match.setWordWrap(False)
        self.password_match.setObjectName("password_match")
        self.login_unique = QtWidgets.QLabel(Dialog)
        self.login_unique.setGeometry(QtCore.QRect(240, 120, 101, 16))
        self.login_unique.setStyleSheet("color: red\n"
"")
        self.login_unique.setObjectName("login_unique")
        self.password_len = QtWidgets.QLabel(Dialog)
        self.password_len.setGeometry(QtCore.QRect(240, 150, 131, 20))
        self.password_len.setStyleSheet("color: red\n"
"")
        self.password_len.setObjectName("password_len")
        self.first_name_empty = QtWidgets.QLabel(Dialog)
        self.first_name_empty.setGeometry(QtCore.QRect(240, 60, 47, 13))
        self.first_name_empty.setStyleSheet("color: red\n"
"")
        self.first_name_empty.setObjectName("first_name_empty")
        self.last_name_empty = QtWidgets.QLabel(Dialog)
        self.last_name_empty.setGeometry(QtCore.QRect(240, 90, 47, 13))
        self.last_name_empty.setStyleSheet("color: red\n"
"")
        self.last_name_empty.setObjectName("last_name_empty")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "First name"))
        self.label_2.setText(_translate("Dialog", "Last name"))
        self.pushButton_2.setText(_translate("Dialog", "Регистрация"))
        self.label_4.setText(_translate("Dialog", "Login"))
        self.label_5.setText(_translate("Dialog", "Paswword"))
        self.label_6.setText(_translate("Dialog", "Password"))
        self.password_match.setText(_translate("Dialog", "Password don\'t match"))
        self.login_unique.setText(_translate("Dialog", "Login is not unique"))
        self.password_len.setText(_translate("Dialog", "The password is too short"))
        self.first_name_empty.setText(_translate("Dialog", "*"))
        self.last_name_empty.setText(_translate("Dialog", "*"))
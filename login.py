import sys
from hashlib import md5
import requests as requests
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize, QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog
import subprocess
import os
from PyQt5.uic.properties import QtCore, QtGui
from main import MainWin
import settings

if settings.DEBUG:
    ui_list = ['login', 'registrate']
    for file in ui_list:
        result = subprocess.run(['pyuic5', os.path.abspath(f'{file}.ui')],
                                stdout=subprocess.PIPE)
        script = result.stdout.decode('utf-8')
        with open(f'{file}_ui.py', 'w', encoding='utf-8') as f:
            f.write(script)
import registrate_ui
import login_ui


class RegistrateWin(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('icon.png'))
        self.ui = registrate_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.registrate)
        self.ui.password.textChanged.connect(self.password_validate)
        self.ui.password2.textChanged.connect(self.password_match)
        self.ui.login.textChanged.connect(self.login_validate)
        self.hide_labels()
        self.setWindowTitle('Registration')

    def password_validate(self):
        if len(self.ui.password.text()) >= 6:
            self.ui.password_len.hide()
        else:
            self.ui.password_len.show()

    def password_match(self):
        if self.ui.password.text() == self.ui.password2.text():
            self.ui.password_match.hide()
        else:
            self.ui.password_match.show()

    def registrate(self):
        flag = False
        first_name = self.ui.first_name.text()
        last_name = self.ui.last_name.text()
        login = self.ui.login.text()
        password = self.ui.password.text()
        password2 = self.ui.password2.text()
        if first_name == '':
            self.ui.first_name_empty.show()
            flag = True
        else:
            self.ui.first_name_empty.hide()
        if last_name == '':
            self.ui.last_name_empty.show()
            flag = True
        else:
            self.ui.last_name_empty.hide()
        if password == '':
            self.ui.password_len.show()
            flag = True
        if login == '':
            self.ui.login_unique.show()
            flag = True

        if flag or password != password2:
            return

        if self.send(login, password, first_name, last_name):
            self.main = MainWin(login, f'{first_name} {last_name}')
            self.main.show()
            self.close()

    @staticmethod
    def send(login, password, first_name, last_name):
        password = md5(password.encode('utf-8')).hexdigest()
        response = requests.post(f"{settings.URL}/registrate", json={'data': [first_name, last_name, login, password]})
        if response.status_code != 200:
            return False
        print(response.json())
        return True

    @staticmethod
    def check_login(login):
        response = requests.post(f"{settings.URL}/check_login", json={'login': login})
        if response.status_code != 200:
            return

        return response.json().get('login')

    def hide_labels(self):
        self.ui.first_name_empty.hide()
        self.ui.last_name_empty.hide()
        self.ui.login_unique.hide()
        self.ui.password_len.hide()
        self.ui.password_match.hide()

    def login_validate(self):
        login = self.ui.login.text()
        if self.check_login(login) or login == '':
            self.ui.login_unique.show()
        else:
            self.ui.login_unique.hide()


class LoginWin(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.reg = None
        self.setWindowIcon(QIcon('icon.png'))
        self.ui = login_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton_2.clicked.connect(self.registrate)
        self.main = None
        self.setWindowTitle('Authorization')
        self.ui.not_found.hide()

    def login(self):
        login = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        if login == '' or password == '':
            return

        response = requests.post(f"{settings.URL}/login",
                                 json={'login': login, 'password': md5(password.encode('utf-8')).hexdigest()})
        if response.status_code != 200:
            return
        data = response.json()
        found = data.get('login')
        if found:
            self.main = MainWin(login, data['username'])
            self.main.show()
            self.close()
        self.ui.not_found.show()

    def registrate(self):
        self.reg = RegistrateWin()
        self.reg.show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = LoginWin()
    application.show()
    app.exec()

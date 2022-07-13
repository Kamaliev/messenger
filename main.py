import logging
import sys

import requests as requests
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize, QTimer
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog
import subprocess
import os
from PyQt5.uic.properties import QtCore, QtGui
import settings

if settings.DEBUG:
    result = subprocess.run(['pyuic5', os.path.abspath('main.ui')], stdout=subprocess.PIPE)
    script = result.stdout.decode('utf-8')
    with open('ui.py', 'w', encoding='utf-8') as f:
        f.write(script)

import ui

info_template = '''Пользователь: {}
Онлайн: {}'''


class MainWin(QtWidgets.QMainWindow):
    def __init__(self, user, username):
        super().__init__()
        self.user = user
        self.username = username
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.get_message)
        self.timer.start(100)
        self.url = settings.URL
        self.message_id = 0
        self.ui.pushButton.clicked.connect(self.send_message)
        self.setWindowIcon(QIcon('icon.png'))
        self.ui.label.setText(info_template.format(user, 5))

    def keyPressEvent(self, e):

        if e.key() in [Qt.Key_Enter, Qt.Key_Return]:
            self.send_message()

    def get_message(self):
        try:
            response = requests.get(f"{self.url}/get", json={'id': self.message_id, 'login': self.user})
        except Exception as e:
            logging.error(e)
        if response.status_code != 200:
            return
        data = response.json()
        for message in data['data']:
            id, user, time, text = message
            time = time[:time.rfind('.')]
            print(time)
            print(type(time))
            self.ui.textBrowser.append(f"{time} {user}\n{text}\n")
            if self.message_id < id:
                self.message_id = id

        self.ui.label.setText(info_template.format(self.username, data['online']))

    def send_message(self):
        text = self.ui.plainTextEdit.toPlainText().strip()
        if text == '':
            return
        response = requests.post(f"{settings.URL}/send", json={'login': self.user, 'message': text})
        if response.status_code != 200:
            return
        self.ui.plainTextEdit.clear()
        verScrollBar = self.ui.textBrowser.verticalScrollBar()
        verScrollBar.setValue(verScrollBar.maximum())


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWin(settings.URL)
    application.show()
    app.exec()

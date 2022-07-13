from login import LoginWin
from PyQt5 import QtWidgets


app = QtWidgets.QApplication([])
application = LoginWin()
application.show()
app.exec()
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
import MySQLdb as mdb
import sys

class Ui1(QtWidgets.QMainWindow):

    s2_layout2 = QtCore.pyqtSignal()
    s2_layout4 = QtCore.pyqtSignal()

    def __init__(self,parent=None):
        super(Ui1, self).__init__(parent) # Call the inherited classes __init__ method
        Form, Window = uic.loadUiType('../ui/Layout1.ui', self) # Load the .ui file

        self.form = Form()
        self.window = Window()
        self.form.setupUi(self.window)

        # for new user button
        self.form.pushButton_1.clicked.connect(self.new_user)

        # for feedback button
        self.form.pushButton_2.clicked.connect(self.feedback)


    def new_user(self):
        self.window.close()
        self.s2_layout2.emit()

    def feedback(self):
        self.window.close()
        self.s2_layout4.emit()

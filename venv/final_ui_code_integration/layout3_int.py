from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
import MySQLdb as mdb
import sys

class Ui3(QtWidgets.QMainWindow):

    s2_layout1 = QtCore.pyqtSignal()
    s2_layout5 = QtCore.pyqtSignal(int)

    def __init__(self,parent=None):
        super(Ui3, self).__init__(parent) # Call the inherited classes __init__ method
        Form, Window = uic.loadUiType('../ui/Layout3.ui', self) # Load the .ui file

        self.form = Form()
        self.window = Window()
        self.form.setupUi(self.window)

        # for temp-licence
        self.form.pushButton_1.clicked.connect(self.learn_license)

        # for perm-licence
        self.form.pushButton_2.clicked.connect(self.perm_license)

        # for vehicle registration
        self.form.pushButton_3.clicked.connect(self.veh_regis)

        # for fine pay
        self.form.pushButton_4.clicked.connect(self.fine)

        # for cancel button
        self.form.pushButton_5.clicked.connect(self.cancel)

    def learn_license(self):
        self.window.close()
        self.s2_layout5.emit(1)

    def perm_license(self):
        self.window.close()
        self.s2_layout5.emit(2)

    def veh_regis(self):
        self.window.close()
        self.s2_layout5.emit(3)

    def fine(self):
        self.window.close()
        self.s2_layout5.emit(4)

    def cancel(self):
        self.window.close()
        self.s2_layout1.emit()
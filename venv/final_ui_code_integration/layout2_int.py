from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QApplication, QMainWindow
import MySQLdb as mdb
import sys

class Ui2(QtWidgets.QMainWindow):

    s2_layout1 = QtCore.pyqtSignal()
    s2_layout3 = QtCore.pyqtSignal()

    def __init__(self,parent=None):
        super(Ui2, self).__init__(parent)  # Call the inherited classes __init__ method
        Form, Window = uic.loadUiType('../ui/Layout2.ui', self)  # Load the .ui file

        self.form = Form()
        self.window = Window()
        self.form.setupUi(self.window)

        # for submit button
        self.form.pushButton_1.clicked.connect(self.login)

        # for back button
        self.form.pushButton_2.clicked.connect(self.back)

    def login(self):
        # for username qline
        n = self.form.lineEdit_1.text()
        # for password qline
        p = self.form.lineEdit_2.text()

        if n == "" or p == "" or len(p) < 10 or p.isdigit() == False or n == " " or type(p) != str :
            self.choice = QtWidgets.QMessageBox.warning(self, 'Incorrect Data',
                                                            "Please enter information",
                                                            QtWidgets.QMessageBox.Close)
            self.form.lineEdit_1.setText("")
            self.form.lineEdit_2.setText("")

        else:
            try:
                db = mdb.connect('your-host-name','username','password','database-name')
                print(self, 'Connection', 'Successful')
                cur = db.cursor()
                mySql_insert_query = """INSERT INTO user (name,phone_number)
                                               VALUES (%s, %s) """
                recordTuple = (n,p)
                cur.execute(mySql_insert_query, recordTuple)

                self.window.close()
                self.s2_layout3.emit()

            except mdb.Error as e:
                print(self, 'Connection', 'Failed')
                self.window.close()
                self.s2_layout1.emit()

    def back(self):
        self.window.close()
        self.s2_layout1.emit()

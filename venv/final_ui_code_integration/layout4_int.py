from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QMessageBox
import MySQLdb as mdb
import sys

class Ui4(QtWidgets.QMainWindow):

    s2_layout1_on_cancel = QtCore.pyqtSignal()
    s2_layout1_on_done = QtCore.pyqtSignal()

    def __init__(self,parent=None):
        super(Ui4, self).__init__(parent)  # Call the inherited classes __init__ method
        Form, Window = uic.loadUiType('../ui/Layout4.ui', self)  # Load the .ui file

        self.form = Form()
        self.window = Window()
        self.form.setupUi(self.window)

        # for combobox
        list1 = [
            self.tr('Problem With Permanent License Department'),
            self.tr('Problem With Learning License Department'),
            self.tr('Problem With Vehicle Registration Department'),
        ]

        self.form.comboBox.addItems(list1)

        # for done button
        self.form.pushButton_1.clicked.connect(self.done)

        # for cancel button
        self.form.pushButton_2.clicked.connect(self.back)

    def done(self):
        feedback = self.form.comboBox.currentText()
        print(feedback)
        try:
            db = mdb.connect('localhost', 'root', '', 'desktop_application')
            print(self, 'Connection', 'Successful')
            cur = db.cursor()
            mySql_insert_query = ("INSERT INTO feedback (feed_desc) VALUES('{0}') ").format(feedback)

            cur.execute(mySql_insert_query)

            self.choice = QtWidgets.QMessageBox.information(self, 'Status',
                                                         "Thank you for the feedback",
                                                         QtWidgets.QMessageBox.Close)
            self.window.close()
            self.s2_layout1_on_done.emit()

        except mdb.Error as e:
            print(self, 'Connection', 'Failed')
            self.window.close()
            self.s2_layout1_on_cancel()
            #sys.exit(1)

    def back(self):
        self.choice = QtWidgets.QMessageBox.question(self, 'Status',
                                            "Do you really want go back ?",
                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if self.choice == QtWidgets.QMessageBox.Yes:
            self.window.close()
            self.s2_layout1_on_cancel.emit()
        else:
            pass
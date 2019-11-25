from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QMessageBox
import MySQLdb as mdb
import sys, random

class Ui5(QtWidgets.QMainWindow):

    s2_layout1 = QtCore.pyqtSignal()

    def __init__(self,x,parent=None):
        n=x
        print(x)
        super(Ui5, self).__init__(parent) # Call the inherited classes __init__ method
        Form, Window = uic.loadUiType('../ui/Layout5.ui', self) # Load the .ui file

        self.form = Form()
        self.window = Window()
        self.form.setupUi(self.window)

        try:
            db = mdb.connect('your-host-name','username','password','database-name')
            print(self, 'Connection', 'Successful')
            cur = db.cursor()
            mySql_fetch_query = ("SELECT * FROM `document` WHERE doc_id= {0}").format(n)
            cur.execute(mySql_fetch_query)
            result = cur.fetchall()
            #print(result)
            self.form.label_6.setText(result[0][1])

            if(n == 1):
                category = 'll'
            elif(n == 2):
                category = 'pl'
            else:
                category = 'vr'

            mySql_fetch_employee = ("SELECT emp_desc FROM `employee_detail` WHERE status = 1 and category= '{0}'").format(category)
            cur.execute(mySql_fetch_employee)
            result1 = cur.fetchall()
            self.text = ""
            for i in result1:
                self.text = self.text + i[0] + "\n\n"

            self.text = self.text.replace("|","\n")
            print(self.text)

            self.form.label_5.setText(self.text)


        except mdb.Error as e:
            print(self, 'Connection', 'Failed')
            sys.exit(1)


        self.form.pushButton.clicked.connect(self.finish)

    def finish(self):
        empty = []
        x = random.randint(2000, 10000)
        empty.sort()
        if x not in empty:
            empty.append(x)
        else:
            print("List is full")

        self.choice = QtWidgets.QMessageBox.information(self, 'Status',
                                                        "You Registration id: " + str(empty),
                                                        QtWidgets.QMessageBox.Close)
        self.window.close()
        self.s2_layout1.emit()

from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
import MySQLdb as mdb
import sys
#from final_ui_code_integration.layout2_int import Ui2


class Ui1(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui1, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('../ui/Layout1.ui', self) # Load the .ui file

        # for new user button
        self.btn1 = self.findChild(QtWidgets.QPushButton, 'pushButton_1')
        self.btn1.clicked.connect(self.new_user)
        #self.show() # Show the GUI

        # for feedback button
        self.btn2 = self.findChild(QtWidgets.QPushButton, 'pushButton_2')
        self.btn2.clicked.connect(self.feedback)
        # self.show()  # Show the GUI



    def new_user(self):
        # from final_ui_code_integration.layout2_int import Ui2
        print("pressed")
        # self.next=Ui2()
        # self.close()
        obj = Ui2()
        obj.show()
        self.close()

    def feedback(self):
        print("pressed")
        uic.loadUi("../ui/Layout4.ui", self)


class Ui2(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui2, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('../ui/Layout2.ui', self)  # Load the .ui file

        # for new user button
        self.btn1 = self.findChild(QtWidgets.QPushButton, 'pushButton_1')
        self.btn1.clicked.connect(self.login)

        # for feedback button
        self.btn2 = self.findChild(QtWidgets.QPushButton, 'pushButton_2')
        self.btn2.clicked.connect(self.back)

        # for username qline
        self.uname = self.findChild(QtWidgets.QLineEdit, 'lineEdit_1')

        # for password qline
        self.passwd = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')

        # self.show()  # Show the GUI

    def login(self):
        print("pressed")
        n = self.uname.text()
        p = self.passwd.text()
        print(n)
        print(p)
        if(n == "" or p == ""):
            print("Please insert data")
        else:
            try:
                db = mdb.connect('localhost', 'root', '', 'desktop_application')
                print(self, 'Connection', 'Successful')
                cur = db.cursor()
                mySql_insert_query = """INSERT INTO user (name,phone_number) 
                                               VALUES (%s, %s) """
                recordTuple = (n,p)
                cur.execute(mySql_insert_query, recordTuple)

            except mdb.Error as e:
                print(self, 'Connection', 'Failed')
                sys.exit(1)

        # uic.loadUi("../ui/Layout3.ui", self)

    def back(self):
        # from final_ui_code_integration.layout1_int import Ui1
        print("Back button pressed")
        # self.next=Ui1()
        obj = Ui1()
        obj.show()
        self.close()
        #uic.loadUi("../ui/Layout1.ui", self)

app = QtWidgets.QApplication(sys.argv)
window = Ui1()
window.show()
app.exec_()
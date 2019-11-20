import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from layout1_int import Ui1
from layout2_int import Ui2
from layout3_int import Ui3
from layout4_int import Ui4
from layout5_int import Ui5

class Controller:

    def __init__(self):
        pass

    def showl1(self):
        self.l1 = Ui1()
        self.l1.s2_layout2.connect(self.showl2)
        self.l1.s2_layout4.connect(self.showl4)
        self.l1.window.show()

    def showl2(self):
        self.l2 = Ui2()
        self.l2.s2_layout1.connect(self.showl1)
        self.l2.s2_layout3.connect(self.showl3)
        self.l1.window.close()
        self.l2.window.show()

    def showl3(self):
        self.l3 = Ui3()
        self.l3.s2_layout1.connect(self.showl1)
        self.l3.s2_layout5.connect(self.showl5)
        self.l2.window.close()
        self.l3.window.show()

    def showl4(self):
        self.l4 = Ui4()
        self.l4.s2_layout1_on_done.connect(self.showl1)
        self.l4.s2_layout1_on_cancel.connect(self.showl1)
        self.l1.window.close()
        self.l4.window.show()

    def showl5(self,x):
        #print(x)
        self.l5 = Ui5(x)
        self.l5.s2_layout1.connect(self.showl1)
        self.l3.window.close()
        self.l5.window.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.showl1()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
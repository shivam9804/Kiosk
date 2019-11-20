import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # style = "screen_1.css"
        # with open(style, 'r') as fh:
        #     app.setStyleSheet(fh.read())

        self.setWindowTitle("screen1")
        self.setGeometry(0, 0, 1280, 720)
        # grid = QGridLayout()
        #
        # label1 = QLabel("Welcome")
        # label1.setStyleSheet("color:black; font:30pt Cormorant Garamond serif; qproperty-alignment: AlignCenter")
        # grid.addWidget(label1, 0, 0, 1, 2)
        #
        # button = QPushButton("New User")
        # # button.setFixedHeight(100)
        # # button.setFixedWidth(150)
        # grid.addWidget(button, 2, 1, 1, 1)
        lbl = QLabel("Welcome")
        btn = QPushButton("New User")
        btn.setFixedWidth(150)
        btn.setFixedHeight(50)
        lbl.setFont(QFont("Calibri", 30))
        lbl.setAlignment(Qt.AlignHCenter)

        lyt = QVBoxLayout()
        lyt.addWidget(lbl)
        lyt.addWidget(btn)

        self.setLayout(lyt)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
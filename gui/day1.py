import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QPushButton,
                             QMessageBox, QLineEdit, QGridLayout, QCheckBox, QRadioButton, QGroupBox)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Welcome Screen'
        self.left = 20
        self.top = 30
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.darkCyan)
        self.setPalette(p)

        # self.nameLabel = QLabel(self)
        # self.nameLabel.setText("Name: ")
        # self.line = QLineEdit(self)

        # self.line.move(80,20)
        # self.line.resize(200, 32)
        # self.nameLabel.move(20, 20)

        # button1 = QPushButton('Button', self)
        # button1.clicked.connect(self.getName)
        # button1.resize(200,32)
        # button1.move(80,60)

        # button = QPushButton('btn', self)
        # button.move(5,10)
        # button.setToolTip("I am push-button")
        # button.clicked.connect(self.clickfun)

        grid = QGridLayout()
        grid.addWidget(self.createExampleGroup(), 0, 0)
        grid.addWidget(self.createExampleGroup(), 1, 0)
        grid.addWidget(self.createExampleGroup(), 0, 1)
        grid.addWidget(self.createExampleGroup(), 1, 1)
        self.setLayout(grid)

        self.show()

    def clickfun(self):
        QMessageBox.about(self, "Hello", "hello")

    def getName(self):
        print("Your Name: " + self.line.text())

    def createExampleGroup(self):
        groupBox = QGroupBox("Best Food")

        radio1 = QRadioButton("&Radio pizza")
        radio2 = QRadioButton("R&adio taco")
        radio3 = QRadioButton("Ra&dio burrito")

        radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

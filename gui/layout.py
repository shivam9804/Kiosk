import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QPushButton,
                             QMessageBox, QLineEdit, QGridLayout, QCheckBox, QRadioButton, QGroupBox)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("layout1")
        self.setGeometry(0, 0, 1280, 720)

        grid = QGridLayout()
        self.setLayout(grid)

        welcome1 = QLabel("WELCOME")
        welcome1.setStyleSheet("color:red; font: 30px")
        welcome1.setContentsMargins(250, 50, 250, 500)
        grid.addWidget(welcome1, 0, 0, 1, 2)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

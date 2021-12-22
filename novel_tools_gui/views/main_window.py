from PyQt6.QtWidgets import QWidget, QGridLayout, QLineEdit, QPushButton
from .open_button import OpenButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.text_edit = None
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        grid.setSpacing(10)
        self.setLayout(grid)

        line_filename = QLineEdit()
        grid.addWidget(line_filename, 0, 0)

        btn_open = OpenButton()
        grid.addWidget(btn_open, 0, 1)

        self.center()
        self.setWindowTitle('Novel Tools')

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


from pathlib import Path
from PyQt6.QtWidgets import QPushButton, QFileDialog


class OpenButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setText('Open')
        self.setShortcut('Ctrl+O')
        self.setToolTip('Open the workspace')
        self.clicked.connect(self.open_dialog)

    def open_dialog(self):
        home_dir = str(Path.home())
        dir_name = QFileDialog.getExistingDirectory(self, 'Open directory', home_dir)
        # TODO: update controller with dir_name
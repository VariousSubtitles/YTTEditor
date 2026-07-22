from PySide6.QtWidgets import QWidget, QListWidget, QVBoxLayout


class SubtitlePanel(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.list = QListWidget()

        layout.addWidget(self.list)
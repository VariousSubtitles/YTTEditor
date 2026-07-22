from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class VideoPanel(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        label = QLabel("動画エリア")
        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)
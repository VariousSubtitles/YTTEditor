from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout


class TagEditor(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.editor = QTextEdit()
        self.editor.setPlaceholderText("ここにYTTタグを入力")

        layout.addWidget(self.editor)
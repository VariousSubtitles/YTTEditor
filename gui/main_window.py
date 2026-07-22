from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QSplitter
)
from PySide6.QtCore import Qt

from gui.video_panel import VideoPanel
from gui.subtitle_panel import SubtitlePanel
from gui.tag_editor import TagEditor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YTT Editor")
        self.resize(1400, 850)

        self.create_menu()

        self.statusBar().showMessage("Ready")

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)

        splitter = QSplitter(Qt.Horizontal)

        self.video_panel = VideoPanel()
        self.subtitle_panel = SubtitlePanel()

        splitter.addWidget(self.video_panel)
        splitter.addWidget(self.subtitle_panel)

        splitter.setSizes([900, 500])

        self.tag_editor = TagEditor()

        main_layout.addWidget(splitter, 8)
        main_layout.addWidget(self.tag_editor, 2)

    def create_menu(self):
        menubar = self.menuBar()

        menubar.addMenu("ファイル")
        menubar.addMenu("編集")
        menubar.addMenu("字幕")
        menubar.addMenu("動画")
        menubar.addMenu("設定")
        menubar.addMenu("ヘルプ")
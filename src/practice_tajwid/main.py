import sys
from pathlib import Path

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget

from practice_tajwid import config

"""======================CONFIG======================"""
BASE_DIR = Path(__file__).resolve().parent
FILE_CONFIG = str(BASE_DIR / "config.json")
FONT_PATH = str(BASE_DIR / "font/Noto.ttf")
config_data = config.get_config(FILE_CONFIG)

WIDTH, HEIGHT = config_data["window"]["size"]
TITLE = config_data["window"]["title"]

"""======================FONT======================"""
words = ["التَّجْوِيدُ"]


class QuizTest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(TITLE)
        self.setMinimumSize(WIDTH, HEIGHT)
        self.init_ui()

    def init_ui(self):
        self.arabic_font = QFont(FONT_PATH, 50)

        self.central_ui = QWidget()
        self.setCentralWidget(self.central_ui)
        self.main_layout = QVBoxLayout()
        self.text = QLabel(words[0])
        self.main_layout.addWidget(self.text)
        self.central_ui.setLayout(self.main_layout)

        self.text.setStyleSheet("color: red;")
        self.central_ui.setStyleSheet("background-color: black;")

        self.text.setFont(self.arabic_font)
        self.text.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.text.setAlignment(Qt.AlignmentFlag.AlignCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuizTest()
    window.show()
    sys.exit(app.exec())

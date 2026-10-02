import sys
from pathlib import Path
from random import choice

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QKeySequence, QShortcut
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from practice_tajwid import config, word

"""======================CONFIG======================"""
BASE_DIR = Path(__file__).resolve().parent
FILE_CONFIG = str(BASE_DIR / "config.json")
config_data = config.Config(FILE_CONFIG)

words = word.get_words(str(BASE_DIR / config_data.db.name))


class QuizTest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(config_data.window.title)
        self.setMinimumSize(*config_data.window.size)
        self.init_ui()
        self.init_keyboard()

    def init_ui(self):
        self.arabic_font = QFont(config_data.text.font_path, config_data.text.sizes.ar)
        self.rus_font = QFont("Arial", config_data.text.sizes.ru)

        self.central_ui = QWidget()
        self.main_layout = QVBoxLayout()
        self.current_word = choice(words)
        self.text = QLabel(self.current_word.word_ar)
        self.text_rus = QLabel()

        self.text.setFont(self.arabic_font)
        self.text_rus.setFont(self.rus_font)
        self.text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_rus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.text.setMargin(20)
        self.main_layout.addStretch(1)
        self.main_layout.addWidget(self.text)
        self.main_layout.addSpacing(20)
        self.main_layout.addWidget(self.text_rus)
        self.main_layout.addStretch(1)

        self.text.setStyleSheet(f"color: {config_data.text.colors.default_qss};")
        self.text_rus.setStyleSheet(f"color: {config_data.text.colors.default_qss};")
        self.central_ui.setStyleSheet(f"background-color: {config_data.window.bg_qss};")

        self.setCentralWidget(self.central_ui)
        self.central_ui.setLayout(self.main_layout)

    def init_keyboard(self):
        self.enter_shortcut = QShortcut(QKeySequence(Qt.Key.Key_Return), self)
        self.enter_shortcut.activated.connect(self.next_word)

    def next_word(self):
        if self.text_rus.text():
            self.current_word = choice(words)
            self.text.setText(self.current_word.word_ar)
            self.text_rus.setText("")
        else:
            text_rus_format = self.get_highlighted_text(
                self.current_word.translation, self.current_word.ru_errors
            )
            self.text_rus.setText(text_rus_format)

    def get_highlighted_text(self, text: str, errors: list):
        for error in errors:
            text = text.replace(
                error,
                f"<span style='color: {config_data.text.colors.correct_qss};'>{error}</span>",
            )
        return text


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuizTest()
    window.show()
    sys.exit(app.exec())

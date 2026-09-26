import json


class Word:
    def __init__(
        self, word_ar: str, translation: str, ar_errors: list, ru_errors: list
    ):
        self.word_ar = word_ar
        self.translation = translation
        self.ar_errors = ar_errors
        self.ru_errors = ru_errors

    def __repr__(self) -> str:
        return f"Words(word_ar='{self.word_ar}', translation='{self.translation}')"

    def __str__(self) -> str:
        return f"{self.word_ar} — {self.translation}"


def get_words(path: str) -> list:
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    words = []
    for word in data:
        translation = data[word]["translation"]
        ar_errors: list = data[word]["ar_errors"]
        ru_errors: list = data[word]["ru_errors"]
        words.append(Word(word, translation, ar_errors, ru_errors))

    return words

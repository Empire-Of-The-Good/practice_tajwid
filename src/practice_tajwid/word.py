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


def save_db(path: str, data: dict):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def get_words(path: str) -> list[Word]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {
            "التَّجْوِيدُ": {
                "translation": "Ат-Таджвӣду",
                "ar_errors": ["تَّ"],
                "ru_errors": ["Ат"],
            },
            "قُرْآنٌ": {"translation": "К̣ур’а̄нун", "ar_errors": ["قُ"], "ru_errors": ["К̣"]},
            "خَالِدِينَ": {
                "translation": "Х̮о̄лидӣна",
                "ar_errors": ["خَا"],
                "ru_errors": ["Х̮о̄"],
            },
        }
        save_db(path, data)

    words = []
    for word in data:
        translation = data[word]["translation"]
        ar_errors: list = data[word]["ar_errors"]
        ru_errors: list = data[word]["ru_errors"]
        words.append(Word(word, translation, ar_errors, ru_errors))

    return words

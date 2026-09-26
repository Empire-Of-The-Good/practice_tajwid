import json


def get_words(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data

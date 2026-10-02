import json

base_config = {
    "db": {"name": "words_bd.json"},
    "window": {
        "size": [800, 600],
        "title": "Quiz - Practice Tajwid",
        "fps": 60,
        "background_color": [0, 0, 0],
    },
    "text": {
        "font_path": "font/Note.ttf",
        "sizes": {"ar": 50, "ru": 20},
        "colors": {"default": [242, 242, 242], "correct": [200, 0, 0]},
    },
}


def update_config(path: str, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def get_config(path: str) -> dict:
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    except FileNotFoundError:
        update_config(path, base_config)
        return base_config

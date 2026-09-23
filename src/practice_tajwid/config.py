import json


def get_config(path: str) -> dict:
    print(path)
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def update_config(path: str, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

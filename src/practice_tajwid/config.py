import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class DBConfig:
    name: str


@dataclass
class WindowConfig:
    size: list[int]
    title: str
    fps: int
    background_color: list[int]

    @property
    def bg_qss(self) -> str:
        bg = self.background_color
        return f"rgb({bg[0]}, {bg[1]}, {bg[2]})"


@dataclass
class TextSizes:
    ar: int
    ru: int


@dataclass
class TextColors:
    default: list[int]
    correct: list[int]

    @property
    def default_qss(self) -> str:
        return f"rgb({self.default[0]}, {self.default[1]}, {self.default[2]})"

    @property
    def correct_qss(self) -> str:
        return f"rgb({self.correct[0]}, {self.correct[1]}, {self.correct[2]})"


@dataclass
class TextConfig:
    font_path: str
    sizes: TextSizes
    colors: TextColors


class Config:
    def __init__(self, path_config: str):
        self.path_config = Path(path_config)
        self.load()

    def load(self) -> None:
        if not self.path_config.exists():
            self._create_default_config()

        with open(self.path_config, "r", encoding="utf-8") as file:
            data = json.load(file)

        self._init_from_dict(data)

    def _init_from_dict(self, data: dict) -> None:
        self.db = DBConfig(**data["db"])
        self.window = WindowConfig(**data["window"])
        text_sizes = TextSizes(**data["text"]["sizes"])
        text_colors = TextColors(**data["text"]["colors"])
        self.text = TextConfig(data["text"]["font_path"], text_sizes, text_colors)

    def save(self) -> None:
        data = {
            "db": asdict(self.db),
            "window": asdict(self.window),
            "text": asdict(self.text),
        }
        with open(self.path_config, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def _create_default_config(self) -> None:
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
        self._init_from_dict(base_config)
        self.save()

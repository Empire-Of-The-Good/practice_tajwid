import sys
from pathlib import Path

import arabic_reshaper
import pygame
from bidi.algorithm import get_display

from practice_tajwid import config

pygame.init()
pygame.font.init()

"""======================CONFIG======================"""
BASE_DIR = Path(__file__).resolve().parent
FILE_CONFIG = str(BASE_DIR / "config.json")
FONT_PATH = str(BASE_DIR / "font/Noto.ttf")
config_data = config.get_config(FILE_CONFIG)

WIDTH, HEIGHT = config_data["window"]["size"]
clock = pygame.time.Clock()
FPS = config_data["window"]["fps"]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(config_data["window"]["title"])

"""======================FONT======================"""
font = pygame.font.Font(FONT_PATH, 50)

words = ["التجويد"]
reshaped_text = arabic_reshaper.reshape(words[0])
bidi_text = get_display(reshaped_text)
text_surface = font.render(bidi_text, True, (255, 0, 0))


def quiz_window():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        screen.blit(text_surface, (300, 300))
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    quiz_window()

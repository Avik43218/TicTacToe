import sys
import pygame

from main import start_game
from assets.main_menu import MainMenuStyles
from assets.game_config import CongigSettings as C

pygame.init()
screen = pygame.display.set_mode((C.WIDTH, C.HEIGHT))
font = pygame.font.Font(None, C.FONT_SIZE)

main_menu = MainMenuStyles()


while True:

    main_menu.draw_menu(screen=screen, font=font)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for level, rect in main_menu.buttons.items():
                if rect.collidepoint(event.pos):
                    difficulty = level
                    print(f"Selected Difficulty: {difficulty}")

                    start_game(difficulty=difficulty)

                    pygame.quit()
                    exit()


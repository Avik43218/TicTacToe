import pygame
from assets.game_config import CongigSettings as C

class MainMenuStyles:

    buttons = {
        "EASY": pygame.Rect(C.EASY_BUTTON),
        "MEDIUM": pygame.Rect(C.MEDIUM_BUTTON),
        "HARD": pygame.Rect(C.HARD_BUTTON)
    }
    
    def draw_menu(self, screen, font):
        screen.fill(C.DARK_GRAY)
        title = font.render("Select Difficulty", True, C.WHITE)
        screen.blit(title, C.TITLE_COORDINATE)

        for text, rect in self.buttons.items():

            if text.lower() == "easy":
                pygame.draw.rect(screen, C.EASY_BUTTON_COLOR, rect)
                label = font.render(text, True, C.WHITE)
                screen.blit(label, (rect.x + 60, rect.y + 15))

            elif text.lower() == "medium":
                pygame.draw.rect(screen, C.MEDIUM_BUTTON_COLOR, rect)
                label = font.render(text, True, C.WHITE)
                screen.blit(label, (rect.x + 40, rect.y + 15))

            elif text.lower() == "hard":
                pygame.draw.rect(screen, C.HARD_BUTTON_COLOR, rect)
                label = font.render(text, True, C.WHITE)
                screen.blit(label, (rect.x + 60, rect.y + 15))

        pygame.display.flip()

    def __repr__(self):
        print("Main menu class")

import pygame
from constants import *

# an attempt was made to organize score and game over screens into objects. It did not go well

class GameOver:
    def __init__(self):
        self.retry_button = pygame.Rect(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 + 50, 150, 50)
        self.quit_button = pygame.Rect(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 + 120, 150, 50)

    def handle_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.retry_button.collidepoint(event.pos):
                return "retry"
            elif self.quit:
                sys.exit()
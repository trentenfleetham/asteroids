import pygame

# an attempt was made to organize score and game over screens into objects. It did not go well

class GameUI:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.button_font = pygame.font.Font(None, 36)
        self.game_font = pygame.font.Font(None, 48)

    def draw_score(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    def draw_text(self, screen, text, font, color, x, y):
        # Helper function to draw text on the screen.
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))
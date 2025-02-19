import pygame

# an attempt was made to organize score and game over screens into objects. It did not go well

class GameState:
    def __init__(self):
        self.is_running = True
        self.is_game_over = False
        self.groups = {
            'updatable': pygame.sprite.Group(),
            'drawable': pygame.sprite.Group(),
            'asteroids': pygame.sprite.Group(),
            'shots': pygame.sprite.Group()
        }
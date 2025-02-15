# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():

    #initialize pygame
    pygame.init()

    # set up display using constants file
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create clock object
    clock = pygame.time.Clock()
    dt = 0

    # creating player groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)

    # spawn player in middle of screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/ 2)



    # set up game loop
    while True:
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Black screen
        screen.fill((0,0,0))

        # player movements
        for obj in drawable:
            obj.draw(screen)
        updatable.update(dt)

        # display update and fps settings
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
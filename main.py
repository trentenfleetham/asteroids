# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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

    # creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # creating containers
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    # spawn player in middle of screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/ 2)



    # set up game loop
    while True:
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
                updatable.update(dt)

        # collisions
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()

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
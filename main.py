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


def draw_text(screen, text, font, color, x, y):
    #Helper function to draw text on the screen.
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def game_over_screen(screen, score):
    #Displays the Game Over screen with final score and Retry button.
    font = pygame.font.Font(None, 48)
    button_font = pygame.font.Font(None, 36)
    screen.fill((0, 0, 0))  # Black background

    # Draw final score
    draw_text(screen, f"Game Over!", font, (255, 0, 0), SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 3)
    draw_text(screen, f"Final Score: {score}", font, (255, 255, 255), SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 - 50)

    # Retry Button
    retry_button = pygame.Rect(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 + 50, 150, 50)
    pygame.draw.rect(screen, (0, 255, 0), retry_button)
    draw_text(screen, "Retry", button_font, (0, 0, 0), SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT // 2 + 60)

    # Quit Button
    quit_button = pygame.Rect(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 + 120, 150, 50)
    pygame.draw.rect(screen, (255, 0, 0), quit_button)
    draw_text(screen, "Quit", button_font, (0, 0, 0), SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT // 2 + 135)

    pygame.display.flip()  # Update screen

    # Wait for user to click Retry
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_button.collidepoint(event.pos):  # Check if Retry button was clicked
                    return  # Exit function to restart game
                elif quit_button.collidepoint(event.pos):
                    sys.exit()


def main():

    #initialize pygame
    pygame.init()
    # set up display using constants file
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # create clock object
    clock = pygame.time.Clock()
    dt = 0

    # Initialize score
    score = 0
    font = pygame.font.Font(None, 36)

    # Load background image
    background = pygame.image.load("assets/images/background.png").convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Scale if needed

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
                game_over_screen(screen, score) # Show game over screen
                return main() # Restart game when Retry is clicked

            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()
                    score += 100

        # draw background screen
        screen.blit(background, (0, 0))

        # player movements
        for obj in drawable:
            obj.draw(screen)
        updatable.update(dt)

        # display score
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10,10))

        # display update and fps settings
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
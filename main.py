# Import necessary modules
import pygame
from constants import *

def main():
    # Initialize pygame
    pygame.init()
    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

    # Get a new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create a basic game loop
    while True:
        screen.fill("black")
        pygame.display.flip()

        # Exit game loop once user closes the game window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    main()


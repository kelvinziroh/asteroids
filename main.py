# Import necessary modules
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidsfield import AsteroidField

def main():
    # Initialize pygame
    pygame.init()

    # Get a new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create a clock object
    clock = pygame.time.Clock()
    
    # Initialize a variable to 0
    dt = 0
    
    # Create groups to manage multiple objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    # Set both groups as containers for the Player class
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    # Instantiate a player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    # Create a basic game loop
    while True:
        # Exit game loop once user closes the game window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        updatable.update(dt) # Turn the player left or right
        for i in drawable:
            i.draw(screen) # Render each projects on the screen
        pygame.display.flip()

        # Limit the program's fps to 60 and record the delta 
        # time in seconds
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()


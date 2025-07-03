import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    # Override the draw method from parent class to draw the player
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            center=self.position,
            radius=self.radius,
            width=2
        )
    
    def update(self, dt):
        self.position += self.velocity * dt
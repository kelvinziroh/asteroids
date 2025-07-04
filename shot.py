import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    # Override the draw method from parent class to draw the shot
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
import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    
    def split(self):
        # Randomly select asteroid split angle on collision
        split_angle = random.uniform(20, 50)
        
        # Rotate the current asteroids velocity twice in opposite
        # directions
        velocity1 = self.velocity.rotate(split_angle)
        velocity2 =  self.velocity.rotate(-split_angle)
        
        # Update the radius of the split asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Instantiate the two new sub asteroids
        sub_ast1 = Asteroid(self.position[0], self.position[1], new_radius)
        sub_ast2 = Asteroid(self.position[0], self.position[1], new_radius)
        
        # Update the velocity of the split sub asteroids
        sub_ast1.velocity = velocity1 * 1.2
        sub_ast2.velocity = velocity2 * 1.2
        
        # Destroy the current asteroid
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
    
    # Override the draw method from parent class to draw the asteroid
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
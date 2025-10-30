import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return

        random_angle = random.uniform(20, 50)
        speed = self.velocity.length() or 150
        parent_dir = self.velocity.normalize() if speed else pygame.Vector2(0, -1)

        dir_1 = parent_dir.rotate(random_angle)
        dir_2 = parent_dir.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        

        a1 = Asteroid(self.position[0], self.position[1], new_radius)
        a1.velocity = dir_1 * speed * 1.2
        a2 = Asteroid(self.position[0], self.position[1], new_radius)
        a2.velocity = dir_2 * speed * 1.2

        self.kill()

        
        # if self.radius > ASTEROID_MIN_RADIUS:

import random

import pygame

from circleshape import CircleShape
from constants import *
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    # moves in a striaght line at a constant speed
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        new_vector = self.velocity.rotate(random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        x, y = self.position
        asteroid1 = Asteroid(x, y, new_radius)
        asteroid2 = Asteroid(x, y, new_radius)

        asteroid1.velocity = new_vector * 1.2

        new_vector = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid2.velocity = new_vector * 1.2

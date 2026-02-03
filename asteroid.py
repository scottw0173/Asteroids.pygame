import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def split(self):
        old_radius = self.radius
        old_pos = self.position.copy()
        old_vel = self.velocity.copy()
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20,50)
        vel1 = old_vel.rotate(random_angle)
        vel2 = old_vel.rotate(-random_angle)
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(old_pos.x, old_pos.y, new_radius)
        a2 = Asteroid(old_pos.x, old_pos.y, new_radius)
        a1.velocity = vel1 *1.2
        a2.velocity = vel2 *1.2
        return [a1,a2]
        
        

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
        )

    def update(self, dt):
        self.position += self.velocity * dt
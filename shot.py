import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH
class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x,y, SHOT_RADIUS)
        self.velocity = velocity
        self.rotation = 0
    
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
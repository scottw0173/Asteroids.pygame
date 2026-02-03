from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN_SECONDS
import pygame
from shot import Shot

class Player(CircleShape):
    def __init__(self,x,y,radius,rotation):
        super().__init__(x,y,radius)
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.shot_cooldown = 0

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.shot_cooldown > 0:
            return None
        else:
            direction = pygame.Vector2(0, 1).rotate(self.rotation)
            velocity = direction * PLAYER_SHOOT_SPEED
            spawn_pos = self.position + direction * (self.radius + SHOT_RADIUS)
            self.shot_cooldown += PLAYER_SHOOT_COOLDOWN_SECONDS
            return Shot(spawn_pos.x, spawn_pos.y, velocity)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1 * dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-1*dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.shot_cooldown -= dt
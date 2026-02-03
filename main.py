import pygame
import sys
from logger import log_state, log_event
import circleshape
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids with pygame version: 2.6.1 ")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2), PLAYER_RADIUS, 0)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for obj in asteroids:
            if player.collides_with(obj):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.kill()
        screen.fill('black')
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60))/1000


if __name__ == "__main__":
    main()

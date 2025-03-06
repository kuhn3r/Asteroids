import sys
import pygame # type: ignore
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, drawable, updateable)
    Shot.containers = (shots, drawable, updateable)
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()

    Player.containers = (drawable, updateable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                return

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()  
                    shot.kill()  
        
        screen.fill("black")

        for item in drawable:
            item.draw(screen)
        

        pygame.display.flip()
        dt = clock.tick(60) / 1000 
        

if __name__ == "__main__":
    main()
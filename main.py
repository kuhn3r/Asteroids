import pygame # type: ignore
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    asteroids = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, drawable, updateable)
    AsteroidField.containers = updateable
    
    Player.containers = (drawable, updateable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable.update(dt)
        
        screen.fill("black")

        for item in drawable:
            item.draw(screen)
        

        pygame.display.flip()
        dt = clock.tick(60) / 1000 
        

if __name__ == "__main__":
    main()
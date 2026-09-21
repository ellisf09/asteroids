from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame
import sys
from player import Player
from asteroid import *
from shot import *
from asteroidfield import AsteroidField
from logger import log_state, log_event
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock=pygame.time.Clock()
    dt=0.0
    updatable=pygame.sprite.Group()
    shots=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()
    Asteroid.containers=(asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers=(updatable)
    screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player=Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    af=AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
        updatable.update(dt)
        for ast in asteroids:
            if ast.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            else:
                for sh in shots:
                    if ast.collides_with(sh):
                        log_event("asteroid_shot")
                        sh.kill()
                        ast.split()
        screen.fill("black")
        for drawa in drawable:
            drawa.draw(screen)
        player.draw(screen)
        pygame.display.flip()
        dt=clock.tick(60) / 1000
       
if __name__ == "__main__":
    main()

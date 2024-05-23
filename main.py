import pygame
from settings import *
from player import Player
from ray_casting import ray_casting

pygame.init()

sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()        
    sc.fill(BLACK)
    pygame.draw.rect(sc, SKYBLUE,(0, 0, WIDTH, HALF_HEIGHT))
    pygame.draw.rect(sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))
    ray_casting(sc, player.pos, player.angle)
    pygame.display.flip()
    clock.tick(FPS)

import pygame
from settings import *
from player import Player
import math
from map import world_map
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

    ray_casting(sc, player.pos, player.angle)

    pygame.draw.circle(sc, GREEN, (int(player.x), int(player.y)), 12)
    
    # left green line
    left_x = player.x + WIDTH * math.cos(player.angle - HALF_FOV)
    left_y = player.y + WIDTH * math.sin(player.angle - HALF_FOV)
    pygame.draw.line(sc, GREEN, player.pos, (int(left_x), int(left_y)), 2)

    # right green line
    right_x = player.x + WIDTH * math.cos(player.angle + HALF_FOV)
    right_y = player.y + WIDTH * math.sin(player.angle + HALF_FOV)
    pygame.draw.line(sc, GREEN, player.pos, (int(right_x), int(right_y)), 2)

    for x, y in world_map:
        pygame.draw.rect(sc, DARKGREY, (x, y, TILE, TILE), 2)

    pygame.display.flip()
    clock.tick(FPS)

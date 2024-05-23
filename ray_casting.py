import pygame
import math
from settings import *
from map import world_map

def ray_casting(sc, player_pos, player_angle):
    cur_angle = player_angle - HALF_FOV
    xo, yo = player_pos
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(1, MAX_DEPTH):
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            if (int(x // TILE) * TILE, int(y // TILE) * TILE) in world_map:
                proj_height = PROJ_COEFF / (depth + 0.0001)
                pygame.draw.rect(sc, WHITE, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
                break
        cur_angle += DELTA_ANGLE

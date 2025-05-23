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
                # Fix fisheye effect
                depth *= math.cos(player_angle - cur_angle)
                depth = max(depth, 0.0001)  # Prevent division by zero or tiny numbers

                # Calculate projected wall slice height
                proj_height = PROJ_COEFF / depth
                proj_height = min(proj_height, HEIGHT * 2)  # Prevent extreme heights

                # Wall color shading based on depth
                c = 255 / (1 + depth * depth * 0.00002)
                color = (c, c // 2, c // 3)

                # Draw the vertical slice
                pygame.draw.rect(
                    sc,
                    color,
                    (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height)
                )
                break

        cur_angle += DELTA_ANGLE

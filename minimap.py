import pygame
import math
from map import world_map
from settings import TILE

def draw_minimap(screen, player_pos, player_angle):
    MINIMAP_SCALE = 0.2  # Adjust if too small or large
    MINI_TILE = int(TILE * MINIMAP_SCALE)

    # Dynamically get map size
    map_tiles_x = max(x for x, y in world_map) // TILE + 1
    map_tiles_y = max(y for x, y in world_map) // TILE + 1
    minimap_width = map_tiles_x * MINI_TILE
    minimap_height = map_tiles_y * MINI_TILE

    # Create minimap surface
    minimap_surface = pygame.Surface((minimap_width, minimap_height))
    minimap_surface.fill((30, 30, 30))  # Dark background

    # Draw walls
    for x, y in world_map:
        mini_x = int(x * MINIMAP_SCALE)
        mini_y = int(y * MINIMAP_SCALE)
        pygame.draw.rect(minimap_surface, (255, 255, 255), (mini_x, mini_y, MINI_TILE, MINI_TILE))

    # Draw player
    px = int(player_pos[0] * MINIMAP_SCALE)
    py = int(player_pos[1] * MINIMAP_SCALE)
    pygame.draw.circle(minimap_surface, (255, 0, 0), (px, py), 4)

    # Draw direction
    dx = math.cos(player_angle) * 20
    dy = math.sin(player_angle) * 20
    pygame.draw.line(minimap_surface, (255, 0, 0), (px, py), (px + dx, py + dy), 2)

    # Blit to top-right corner
    screen.blit(minimap_surface, (screen.get_width() - minimap_width - 500, 350))

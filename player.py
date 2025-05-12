import pygame
import math
from settings import *
from map import world_map

class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
    @property
    def pos(self):
        return (self.x, self.y)
    def check_collision(self, x, y):        
        if (int(x // TILE) * TILE, int(y // TILE) * TILE) not in world_map:
            return False
        return True
    def movement(self, delta_time):
        keys = pygame.key.get_pressed()
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = player_speed
        if keys[pygame.K_w]:
            dx += speed * cos_a
            dy += speed * sin_a
        if keys[pygame.K_s]:
            dx -= speed * cos_a
            dy -= speed * sin_a
        if keys[pygame.K_a]:
            dx += speed * sin_a
            dy -= speed * cos_a
        if keys[pygame.K_d]:
            dx -= speed * sin_a
            dy += speed * cos_a
        if not self.check_collision(self.x + dx, self.y):
            self.x += dx
        if not self.check_collision(self.x, self.y + dy):
            self.y += dy
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02
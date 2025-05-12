import pygame
from settings import *
from player import Player
from ray_casting import ray_casting
from drawing import Drawing
from minimap import draw_minimap


pygame.init()

sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    delta_time = clock.tick(60) / 1000  
    player.movement(delta_time)        
       
    sc.fill(BLACK)

    drawing.background()
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)
    draw_minimap(sc, player.pos, player.angle)
    pygame.display.flip()
    clock.tick()

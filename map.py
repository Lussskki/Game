from settings import *

text_map = [
    'wwwwwwwwwwwwwwwww',
    'w...............w',
    'w..w.........w..w',
    'w.......w.......w',
    'w...............w',
    'w..w....w.......w',
    'w...............w',
    'wwwwwwwwwwwwwwwww',                        
]
world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'w':
            world_map.add((i * TILE, j * TILE))

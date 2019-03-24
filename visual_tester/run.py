import random
import pygame

from env import *
from World import World
from Terrain import Terrain
from Player import Player

pygame.init()

window = pygame.display.set_mode(WINDOW_SIZE)

# Generate World
World.generate_world(100)

# Creating the terrain
terrain = Terrain()

pygame.display.set_caption('API Game')
running = True

# Event loop
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # keys = pygame.key.get_pressed()
            direction = -1

            if event.key == pygame.K_UP:
                # Move up
                # Here should be the API call
                # Let's just move the player for now
                direction = DIRECTIONS['UP']
            
            if event.key == pygame.K_DOWN:
                direction = DIRECTIONS['DOWN']
            
            if event.key == pygame.K_LEFT:
                direction = DIRECTIONS['LEFT']

            if event.key == pygame.K_RIGHT:
                direction = DIRECTIONS['RIGHT']
            
            terrain.refresh_environment(direction)

    # Draw tiles on terrain
    terrain.update()

    # Draw each player on terrain
    terrain.update_player(window)

    # Draw terrain on window
    terrain.draw(window)
    
    # Display window on the screen
    pygame.display.update()

# End of the game loop
pygame.quit()

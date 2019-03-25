import pygame

from env import *

from ResourcesManager import ResourcesManager

class Player:
    def __init__(self, row, col, sight_distance = 3):
        self.local_coord = [row, col]
        self.sight_distance = sight_distance
        self.load_sprites()
    
    def load_sprites(self):
        self.filename = 'characters.png'
        self.player_spritesheet = ResourcesManager.load_spritesheet(self.filename, 8, 12)
        self.tile = self.player_spritesheet.get_tile(4, 0)
        #.get_rect()
    
    def get_coord(self):
        return self.local_coord

    def get_sight(self):
        return self.sight_distance

    def move(self, direction):
        # if direction == DIRECTIONS['UP']:
        #     # Go up
        #     self.local_coord[POLES['VERTICAL']] -= 1
        # if direction == DIRECTIONS['DOWN']:
        #     # Go down
        #     self.local_coord[POLES['VERTICAL']] += 1
        # if direction == DIRECTIONS['LEFT']:
        #     # Go left
        #     self.local_coord[POLES['HORIZONTAL']] -= 1
        # if direction == DIRECTIONS['RIGHT']:
        #     # Go right
        #     self.local_coord[POLES['HORIZONTAL']] += 1
        pass

    def draw(self, terrain_surface, box_size):
        self.tile = pygame.transform.scale(self.tile, box_size)
        terrain_surface.blit(self.tile, (self.local_coord[POLES['HORIZONTAL']] * self.tile.get_rect().width - self.tile.get_rect().width/2, self.local_coord[POLES['VERTICAL']] * self.tile.get_rect().height - self.tile.get_rect().height/2))

import pygame

from env import *
from World import World
from Player import Player
from ResourcesManager import ResourcesManager

class Terrain:
    def __init__(self, rows=17, cols=17):
        self.grid_size = [rows, cols]
        self.grid = []
        self.scale = True
        self.surface = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA, 32)
        self.load_sprites()
        # Creating local player
        self.player = Player(self.get_center()[0], self.get_center()[1])
        self.refresh_environment(-1)
        # Creating other players ?

    def calculate_box_size(self):
        if self.scale:
            box_size = (int(WINDOW_SIZE[0] / self.grid_size[0]), int(WINDOW_SIZE[1] / self.grid_size[1]))
        else:
            box_size = (self.tile.get_rect().width, self.tile.get_rect().height)
        return box_size
    
    def load_sprites(self):
        self.filename = 'basictiles.png'
        self.terrain_spritesheet = ResourcesManager.load_spritesheet(self.filename, 15, 8)
        # tile is the default image used by terrain for box sizing
        self.tile = self.terrain_spritesheet.get_tile(1, 0)
        if self.scale:
            self.tile = pygame.transform.scale(self.tile, self.calculate_box_size())
    
    def refresh_environment(self, direction):
        # Make a call to the world class (API)
        if direction is -2:
            print("Direction problem (-2 instead of 0, 1, 2, 3 or -1 for refresh only)")
        else:
            # Fetch the new grid
            received_grid = World.explore_world(direction, self.player.get_sight())

            # Create the new grid
            new_grid = []
            for row in range(self.grid_size[POLES['VERTICAL']]):
                #print(row)
                new_row = []
                grid_update_row = int((self.grid_size[POLES['VERTICAL']] - len(received_grid))/2)
                for col in range(self.grid_size[POLES['HORIZONTAL']]):
                    if row >= grid_update_row and row < len(received_grid) + grid_update_row:
                        grid_update_col = int((self.grid_size[POLES['HORIZONTAL']] - len(received_grid[row-grid_update_row]))/2)
                        if col >= grid_update_col and col < len(received_grid[row-grid_update_row]) + grid_update_col:
                            #print(" => " + str(col-grid_update_col) + " " + str(received_grid[row-grid_update_row][col-grid_update_col]))
                            new_row.append(received_grid[row-grid_update_row][col-grid_update_col])
                        else:
                            new_row.append(TILES['OUT_OF_MAP'])
                    else:
                        new_row.append(TILES['OUT_OF_MAP'])
                new_grid.append(new_row)
            
            self.grid = new_grid
            #print(new_grid)

            # Player might move if the environment is static (next to map edges for example)
            self.player.move(direction)
    
    def update(self):
        for row in range(self.grid_size[POLES['VERTICAL']]):
            for col in range(self.grid_size[POLES['HORIZONTAL']]):
                # TODO: Generate tiles only once and put them in a list
                current_tile = self.terrain_spritesheet.get_tile(self.grid[row][col][0], self.grid[row][col][1])
                if self.scale:
                    current_tile = pygame.transform.scale(current_tile, self.calculate_box_size())
                self.surface.blit(current_tile, (col * current_tile.get_rect().width, row * current_tile.get_rect().height))
                #self.surface.blit(current_tile, (row * WINDOW_SIZE[0] / self.grid_size[0], col * WINDOW_SIZE[1] / self.grid_size[1]))
                #self.surface.blit(current_tile, (0, 0), (row * WINDOW_SIZE[0] / self.grid_size[0], row * WINDOW_SIZE[1] / self.grid_size[1], 16, 16))
        #self.surface.blit(current_tile, (50, 50))
        
    def update_player(self, window):
        self.player.draw(self.surface, self.calculate_box_size())
    
    def get_center(self):
        return [self.grid_size[POLES['VERTICAL']]/2, self.grid_size[POLES['HORIZONTAL']]/2]

    def draw(self, window):
        window.blit(self.surface, (0, 0))

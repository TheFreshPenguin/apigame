import random

from env import *

# The world class is the equivalent of the API
# It will later be filled with GET and POST requests to the API instead of generating everything by itself
class World:

    # TODO: Switch rowumns with col for better vizualization

    # Static Attributes
    size = 0
    grid = []
    player_absolute_coord = []

    @staticmethod
    def generate_world_from_grid(grid):
        World.size = len(grid)
        World.grid = grid
        # Make player spawn in the middle
        x = len(World.grid)//2
        y = len(World.grid[x])//2
        print(x)
        print(y)
        World.player_absolute_coord = [x, y]

    @staticmethod
    def generate_world(size):
        World.size = size
        World.grid = []
        possibilities = [
            TILES['GRASS_1'],
            TILES['GRASS_2'],
            TILES['SAND'],
        ]

        for i in range(World.size - 1):
            tmp_row = []
            for j in range(World.size - 1):
                tmp_tile = possibilities[random.randint(0, len(possibilities) - 1)]
                tmp_row.append(tmp_tile)
            World.grid.append(tmp_row)
        
        # Make player spawn in the middle
        x = len(World.grid)//2
        y = len(World.grid[x])//2
        print(x)
        print(y)
        World.player_absolute_coord = [x, y]

    @staticmethod
    def explore_world(direction, sight_distance):

        #print("Direction:")
        #print(direction)
        #print("Player coord before:")
        #print(World.player_absolute_coord)
        
        if direction == DIRECTIONS['UP']:
            # Go up
            if World.player_absolute_coord[POLES['VERTICAL']] > 0:
                World.player_absolute_coord[POLES['VERTICAL']] -= 1
        if direction == DIRECTIONS['DOWN']:
            # Go down
            if World.player_absolute_coord[POLES['VERTICAL']] < World.size - 1:
                World.player_absolute_coord[POLES['VERTICAL']] += 1
        if direction == DIRECTIONS['LEFT']:
            # Go left
            if World.player_absolute_coord[POLES['HORIZONTAL']] > 0:
                World.player_absolute_coord[POLES['HORIZONTAL']] -= 1
        if direction == DIRECTIONS['RIGHT']:
            # Go right
            if World.player_absolute_coord[POLES['HORIZONTAL']] < World.size - 1:
                World.player_absolute_coord[POLES['HORIZONTAL']] += 1
        
        #print("Player coord after:")
        #print(World.player_absolute_coord)

        # TODO: Fix bug when you go to the left border for example, only rowumns 0 to <player_sight> are returned
        # We should add as many rowumns as the difference between <start_row> and 0 and fill them with TILES['OUT_OF_MAP']
        # TODO: Same thing for each direction

        start_row = World.player_absolute_coord[POLES['VERTICAL']]-sight_distance
        end_row = World.player_absolute_coord[POLES['VERTICAL']]+sight_distance

        if start_row < 0:
            start_row = 0
        if end_row > World.size - 1:
            end_row = World.size - 1
        #print("Start row: " + str(start_row))
        #print("End row: " + str(end_row))

        sub_grid = World.grid[start_row:end_row+1:1]
        #print("Sub-grid:")
        #print(sub_grid)

        for i in range(end_row - start_row + 1):
            start_col = World.player_absolute_coord[POLES['HORIZONTAL']]-sight_distance
            end_col = World.player_absolute_coord[POLES['HORIZONTAL']]+sight_distance

            if start_col < 0:
                start_col = 0
            if end_col > World.size - 1:
                end_col = World.size - 1
            
            #print("Start col: " + str(start_col))
            #print("End col: " + str(end_col))

            tmp_col = sub_grid[i][start_col:end_col+1:1]
            #print(tmp_col)
            sub_grid[i] = tmp_col
        
        #print(sub_grid)
        print("New player coordinates:")
        print(World.player_absolute_coord)
        
        return sub_grid

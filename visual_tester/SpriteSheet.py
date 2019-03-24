import pygame

# Class to load tiles from spritesheets
class SpriteSheet:
    # Create the object instance using a path and the number of rows and cols
    # Static attributes
    #id = 0
    def __init__(self, path, cols_num, rows_num):
        #SpriteSheet.id += 1
        self.path = path
        self.size_rc = (cols_num, rows_num)
        self.sheet = pygame.image.load(self.path).convert_alpha()
    
    def get_tile(self, col, row):
        # Get the corresponding tile l, c, w, h from the sheet
        # Use: size, row, col
        grid_size_px = self.sheet.get_size()
        #print("Spritesheet size:" + str(grid_size_px))
        tile = pygame.Surface((grid_size_px[0]/self.size_rc[0], grid_size_px[1]/self.size_rc[1]), pygame.SRCALPHA, 32)
        #print((grid_size_px[0]/self.size_rc[0], grid_size_px[1]/self.size_rc[1]))
        tile.blit(self.sheet, (0, 0), (col * grid_size_px[0] / self.size_rc[0], row * grid_size_px[1] / self.size_rc[1], grid_size_px[0] / self.size_rc[0], grid_size_px[1] / self.size_rc[1]))
        return tile
    
    def get_full_image(self):
        return self.sheet

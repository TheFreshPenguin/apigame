import pygame

from SpriteSheet import SpriteSheet

# Class to manage the load of resources (images, audio, etc.)
class ResourcesManager:
    # Base path (images folder)
    base_path = 'img/tiny_16_basic/'
    
    @staticmethod
    def load_spritesheet(path, rows, cols):
        spritesheet = SpriteSheet(ResourcesManager.base_path + path, rows, cols)
        return spritesheet

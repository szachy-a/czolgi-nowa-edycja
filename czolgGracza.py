import pygame

import czolg

class CzolgGracza(czolg.Czolg):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.surf = pygame.image.load()
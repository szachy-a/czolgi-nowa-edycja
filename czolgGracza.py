import pygame
from pygame.locals import (
    K_a,
    K_d,
    K_w,
    K_s
)

import czolg

class CzolgGracza(czolg.Czolg):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.surf = pygame.image.load('czolgGracza.jpg').convert()
        self.rect = self.surf.get_rect(topleft=(x, y))
    def podejmijDecyzje(self):
        klawisze = pygame.key.get_pressed()
        if klawisze[K_a]:
            return czolg.CZOLG_W_LEWO
        if klawisze[K_d]:
            return czolg.CZOLG_W_PRAWO
        if klawisze[K_w]:
            return czolg.CZOLG_W_PRZOD
        if klawisze[K_s]:
            return czolg.CZOLG_W_TYL
        
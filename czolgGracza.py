import pygame
from pygame.locals import (
    K_a,
    K_d,
    K_w,
    K_s,
    K_SPACE,
    K_LEFT,
    K_RIGHT
)

import czolg

class CzolgGracza(czolg.Czolg):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.orgSurf = pygame.image.load('czolgGracza.png').convert_alpha()
        self.surf = self.orgSurf.copy()
        self.rect = self.surf.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.surf)
        self.maxWytrzymalosc = 3
        self.odlegloscStrzalu = 1
        self.zadajeObrazen = 1
        self.hp = self.maxWytrzymalosc
        self.maxCooldown = 5 * 30
        self.cooldown  = 0
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
        if klawisze[K_SPACE]:
            return czolg.STRZAL
        return czolg.BRAK_AKCJI
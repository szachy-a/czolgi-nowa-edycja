import pygame
import czolg
import abc
import algorytmy
import math
import czolgGracza as cg
import pocisk

import __main__

class CzolgWroga(czolg.Czolg):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.maxWytrzymalosc = 3
        self.odlegloscStrzalu = 1
        self.zadajeObrazen = 1
        self.hp = self.maxWytrzymalosc
    def podejmijDecyzje(self):
        p = pocisk.Pocisk(*self.rect.center, self.wektor, 100, 0, self)
        g = pygame.sprite.Group(p)
        for i in range(90):
            p.update(pygame.sprite.Group(__main__.g))
            if p not in g:
                break
        else:
            return czolg.CZOLG_W_LEWO
        p = pocisk.Pocisk(*self.rect.center, self.wektor, self.odlegloscStrzalu, 0, self)
        g = pygame.sprite.Group(p)
        for i in range(self.odlegloscStrzalu):
            p.update(pygame.sprite.Group(__main__.g))
            if p not in g:
                return czolg.STRZAL
        return czolg.CZOLG_W_PRZOD
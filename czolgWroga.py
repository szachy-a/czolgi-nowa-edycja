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
            obrot = 0
            pd = self.podejmijDecyzje
            self.podejmijDecyzje = lambda: czolg.CZOLG_W_LEWO
            while obrot < 360:
                obrot += 3
                self.ruch(None)
                p = pocisk.Pocisk(*self.rect.center, self.wektor, 100, 0, self)
                g = pygame.sprite.Group(p)
                for i in range(90):
                    p.update(pygame.sprite.Group(__main__.g))
                    if p not in g:
                        break
                else:
                    continue
                break
            self.podejmijDecyzje = pd
            if obrot > 180:
                return czolg.CZOLG_W_PRAWO
            else:
                return czolg.CZOLG_W_LEWO
        return czolg.STRZAL

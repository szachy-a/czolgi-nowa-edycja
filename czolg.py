import pygame

import abc
import czolg
import math
import pocisk

CZOLG_W_LEWO, CZOLG_W_PRAWO, CZOLG_W_PRZOD, CZOLG_W_TYL, STRZAL, BRAK_AKCJI, *_ = range(100)

WEKTORY = [pygame.math.Vector2() for _ in range(360)]
for i, v in enumerate(WEKTORY):
    v.from_polar((1, i))
    try:
        v.normalize_ip()
    except ValueError:
        pass
    v.x = -v.x

class Czolg(abc.ABC, pygame.sprite.Sprite):
    @abc.abstractmethod
    def __init__(self, x, y):
        super().__init__()
        self.kat = 0
        self.wektor = pygame.math.Vector2((1, 0))
    def update(self, wszystko):
        self.ruch(wszystko)
    def ruch(self, wszystko):
        match self.podejmijDecyzje():
            case czolg.CZOLG_W_LEWO:
                self.kat += 3
                if self.kat >= 360:
                    self.kat -= 360
                self.surf = pygame.transform.rotate(self.orgSurf, self.kat)
                self.rect = self.surf.get_rect(center=self.rect.center)
                self.wektor = WEKTORY[self.kat]
                self.mask = pygame.mask.from_surface(self.surf)
            case czolg.CZOLG_W_PRAWO:
                self.kat -= 3
                if self.kat <= -360:
                    self.kat += 360
                self.surf = pygame.transform.rotate(self.orgSurf, self.kat)
                self.rect = self.surf.get_rect(center=self.rect.center)
                self.wektor = WEKTORY[self.kat]
                self.mask = pygame.mask.from_surface(self.surf)
            case czolg.CZOLG_W_PRZOD:
                self.rect.x += self.wektor.x * 3
                self.rect.y += self.wektor.y * 3
            case czolg.CZOLG_W_TYL:
                self.rect.x -= self.wektor.x * 3
                self.rect.y -= self.wektor.y * 3
            case czolg.STRZAL:
                wszystko.add(pocisk.Pocisk(*self.rect.center, self.wektor, self.odlegloscStrzalu, self.zadajeObrazen))
    @abc.abstractmethod
    def podejmijDecyzje(self):
        pass
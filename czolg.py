import pygame

import abc
import czolg
import math

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
    def ruch(self):
        match self.podejmijDecyzje():
            case czolg.CZOLG_W_LEWO:
                self.kat += 3
                self.surf = pygame.transform.rotate(self.orgSurf, self.kat)
                self.rect = self.surf.get_rect(center=self.rect.center)
                self.wektor = WEKTORY[self.kat]
            case czolg.CZOLG_W_PRAWO:
                self.kat -= 3
                self.surf = pygame.transform.rotate(self.orgSurf, self.kat)
                self.rect = self.surf.get_rect(center=self.rect.center)
                self.wektor = WEKTORY[self.kat]
            case czolg.CZOLG_W_PRZOD:
                self.rect.x += self.wektor.x * 3
                self.rect.y += self.wektor.y * 3
            case czolg.CZOLG_W_TYL:
                self.rect.x -= self.wektor.x * 3
                self.rect.y -= self.wektor.y * 3
    @abc.abstractmethod
    def podejmijDecyzje(self):
        pass
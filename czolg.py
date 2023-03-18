import pygame

import abc
import czolg

CZOLG_W_LEWO, CZOLG_W_PRAWO, CZOLG_W_PRZOD, CZOLG_W_TYL, STRZAL, BRAK_AKCJI, *_ = range(100)

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
            case czolg.CZOLG_W_PRAWO:
                self.kat -= 3
                self.surf = pygame.transform.rotate(self.orgSurf, self.kat)
                self.rect = self.surf.get_rect(center=self.rect.center)
            case czolg.CZOLG_W_PRZOD:
                self.rect.x += self.wektor.x * 3
                self.rect.y += self.wektor.y * 3
            case czolg.CZOLG_W_TYL:
                self.rect.x -= self.wektor.x * 3
                self.rect.y -= self.wektor.y * 3
    @abc.abstractmethod
    def podejmijDecyzje(self):
        pass
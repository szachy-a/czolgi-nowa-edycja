import pygame

import abc
import czolg

CZOLG_W_LEWO, CZOLG_W_PRAWO, CZOLG_W_PRZOD, CZOLG_W_TYL, LUFA_W_LEWO, LUFA_W_PRAWO, STRZAL, BRAK_AKCJI, *_ = range(100)

class Czolg(abc.ABC, pygame.sprite.Sprite):
    @abc.abstractmethod
    def __init__(self, x, y):
        super().__init__()
        self.kat = 0
    def ruch(self):
        match self.podejmijDecyzje():
            case czolg.LUFA_W_LEWO:
                self.kat += 1
                self.surf = pygame.transform.rotate(self.orgSurf, self.kat)
                self.rect = self.surf.get_rect(center=self.rect.center)
            case czolg.LUFA_W_PRAWO:
                self.kat -= 1
                self.surf = pygame.transform.rotate(self.orgSurf, self.kat)
                self.rect = self.surf.get_rect(center=self.rect.center)
    @abc.abstractmethod
    def podejmijDecyzje(self):
        pass
import pygame

import abc

CZOLG_W_LEWO, CZOLG_W_PRAWO, CZOLG_W_PRZOD, CZOLG_W_TYL, LUFA_W_LEWO, LUFA_W_PRAWO, STRZAL, BRAK_AKCJI, *_ = range(100)

class Czolg(abc.ABC, pygame.sprite.Sprite):
    @abc.abstractmethod
    def __init__(self, x, y):
        super().__init__()
    def ruch(self):
        self.podejmijDecyzje()
    @abc.abstractmethod
    def podejmijDecyzje(self):
        pass
import pygame

import abc

class Czolg(abc.ABC, pygame.sprite.Sprite):
    @abc.abstractmethod
    def __init__(self, x, y):
        super().__init__()
    def ruch(self):
        self.podejmijDecyzje()
    @abc.abstractmethod
    def podejmijDecyzje(self):
        pass
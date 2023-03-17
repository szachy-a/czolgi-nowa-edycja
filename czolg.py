import pygame

class Czolg(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
    def ruch(self):
        self.podejmijDecyzje()
    def podejmijDecyzje(self):
        pass
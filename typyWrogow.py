import pygame

import czolgWroga

class Solider(czolgWroga.CzolgWroga):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.surf = pygame.image.load('solider.png').convert_alpha()
        self.rect = self.surf.get_rect(topleft=(x, y))
        self.maxWytrzymalosc = 2
        self.odlegloscStrzalu = 1
        self.zadajeObrazen = 1
        self.hp = self.maxWytrzymalosc

class Scout(czolgWroga.CzolgWroga):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.surf = pygame.image.load('solider.png').convert_alpha()
        self.rect = self.surf.get_rect(topleft=(x, y))
        self.maxWytrzymalosc = 2
        self.odlegloscStrzalu = 1
        self.zadajeObrazen = 1
        self.hp = self.maxWytrzymalosc
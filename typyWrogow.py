import pygame

import czolgWroga

class Solider(czolgWroga.CzolgWroga):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.orgSurf = pygame.image.load('solider.png').convert_alpha()
        self.surf = self.orgSurf.copy()
        self.rect = self.surf.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.surf)
        self.maxWytrzymalosc = 2
        self.odlegloscStrzalu = 1
        self.zadajeObrazen = 1
        self.hp = self.maxWytrzymalosc
        self.maxCooldown = 8 * 30
        self.cooldown = 0

class Scout(czolgWroga.CzolgWroga):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.orgSurf = pygame.image.load('solider.png').convert_alpha()
        self.surf = self.orgSurf.copy()
        self.rect = self.surf.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.surf)
        self.maxWytrzymalosc = 2
        self.odlegloscStrzalu = 1
        self.zadajeObrazen = 1
        self.hp = self.maxWytrzymalosc
        self.maxCooldown = 6 * 30
        self.cooldown = 0
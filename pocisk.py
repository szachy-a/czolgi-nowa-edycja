import pygame

class Pocisk(pygame.sprite.Sprite):
    def __init__(self, x, y, wektor):
        self.surf = pygame.image.load('pocisk Julka.png').convert()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
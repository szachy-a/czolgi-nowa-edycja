import pygame

class Pocisk(pygame.sprite.Sprite):
    def __init__(self, x, y, wektor):
        super().__init__()
        self.surf = pygame.image.load('pocisk Julka.png').convert()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect(center=(x, y))
        self.wektor = wektor
    def update(self, wszystko):
        self.rect.move_ip(*self.wektor * 10)
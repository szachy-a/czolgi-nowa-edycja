import pygame

class Pocisk(pygame.sprite.Sprite):
    def __init__(self, x, y, wektor, odlegloscStrzalu, zadajeObrazen):
        super().__init__()
        self.surf = pygame.image.load('pocisk.png').convert()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect(center=(x, y))
        self.wektor = wektor
        self.odlegloscStrzalu = odlegloscStrzalu * 30
        self.zadajeObrazen = zadajeObrazen
    def update(self, wszystko):
        if self.odlegloscStrzalu:
            self.rect.move_ip(*self.wektor * 10)
            self.odlegloscStrzalu -= 1
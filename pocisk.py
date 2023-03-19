import pygame

import czolg
import __main__

class Pocisk(pygame.sprite.Sprite):
    def __init__(self, x, y, wektor, odlegloscStrzalu, zadajeObrazen, ktoWystrzelil):
        super().__init__()
        self.surf = pygame.image.load('pocisk.png').convert_alpha()
        self.rect = self.surf.get_rect(center=(x, y))
        self.mask = pygame.mask.from_surface(self.surf)
        self.wektor = wektor
        self.odlegloscStrzalu = odlegloscStrzalu * 30
        self.zadajeObrazen = zadajeObrazen
        while pygame.sprite.collide_mask(self, ktoWystrzelil):
            self.rect.move_ip(*self.wektor * 10)
    def update(self, wszystko):
        if self.odlegloscStrzalu:
            self.rect.move_ip(*self.wektor * 10)
            self.odlegloscStrzalu -= 1
            for duszek in list(__main__.elementyGry):
                if duszek is self:
                    continue
                if pygame.sprite.collide_mask(self, duszek):
                    self.kill()
                    if isinstance(duszek, czolg.Czolg):
                        duszek.hp -= self.zadajeObrazen
                        if duszek.hp <= 0:
                            duszek.kill()
                            break
                    else:
                        duszek.kill()
                        break
        else:
            self.kill()
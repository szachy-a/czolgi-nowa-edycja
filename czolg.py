import pygame

import abc
import czolg
import math
import pocisk
import time

CZOLG_W_LEWO, CZOLG_W_PRAWO, CZOLG_W_PRZOD, CZOLG_W_TYL, STRZAL, BRAK_AKCJI, *_ = range(100)

WEKTORY = [pygame.math.Vector2() for _ in range(360)]
for i, v in enumerate(WEKTORY):
    v.from_polar((1, i))
    try:
        v.normalize_ip()
    except ValueError:
        pass
    v.x = -v.x

class Czolg(abc.ABC, pygame.sprite.Sprite):
    @abc.abstractmethod
    def __init__(self, x, y):
        super().__init__()
        self.orgSurf = None
        self.surf = None
        self.rect = None
        self.wektor = None
        self.kat = 0
        self.wektor = pygame.math.Vector2((1, 0))
        self.maxWytrzymalosc = None
        self.odlegloscStrzalu = None
        self.zadajeObrazen = None
        self.hp = None
        self.maxCooldown = None
        self.cooldown = None
        self.ostatnieOdtworzenie = time.time()
    def update(self, wszystko):
        self.ruch(wszystko)
        self.cooldown -= 1
        if self.cooldown < 0:
            self.cooldown = 0
        self.updateHealthBar()
    def ruch(self, wszystko):
        match self.podejmijDecyzje():
            case czolg.CZOLG_W_LEWO:
                self.kat += 3
                if self.kat >= 360:
                    self.kat -= 360
                self.surf = pygame.transform.rotate(self.orgSurf, self.kat)
                self.rect = self.surf.get_rect(center=self.rect.center)
                self.wektor = WEKTORY[self.kat]
                self.mask = pygame.mask.from_surface(self.surf)
            case czolg.CZOLG_W_PRAWO:
                self.kat -= 3
                if self.kat <= -360:
                    self.kat += 360
                self.surf = pygame.transform.rotate(self.orgSurf, self.kat)
                self.rect = self.surf.get_rect(center=self.rect.center)
                self.wektor = WEKTORY[self.kat]
                self.mask = pygame.mask.from_surface(self.surf)
            case czolg.CZOLG_W_PRZOD:
                self.rect.x += self.wektor.x * 3
                self.rect.y += self.wektor.y * 3
            case czolg.CZOLG_W_TYL:
                self.rect.x -= self.wektor.x * 3
                self.rect.y -= self.wektor.y * 3
            case czolg.STRZAL:
                if self.cooldown == 0:
                    wszystko.add(pocisk.Pocisk(*self.rect.center, self.wektor, self.odlegloscStrzalu, self.zadajeObrazen, self))
                    self.cooldown = self.maxCooldown
    @abc.abstractmethod
    def podejmijDecyzje(self):
        pass
    def __repr__(self):
        return '<' + self.__class__.__name__ + repr(self.__dict__) + '>'
    def updateHealthBar(self):
        surf = pygame.Surface((100, 10))
        surf.fill((255, 0, 0))
        pygame.draw.rect(surf, (0, 255, 0), ((0, 0), (int(self.hp / self.maxWytrzymalosc * 100), 10)))
        srodek = self.orgSurf.get_height() // 2
        self.surf.blit(surf, surf.get_rect(centerx=self.surf.get_width() // 2, top=self.surf.get_height() // 2 - srodek))
        pygame.image.save(surf, 'test2.png')
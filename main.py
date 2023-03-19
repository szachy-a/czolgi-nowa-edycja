import pygame
import algorytmy
from pygame.locals import (
    QUIT
)
pygame.init()

import czolgGracza
import typyWrogow

screen = pygame.display.set_mode((1280, 720))
czas = pygame.time.Clock()
pygame.key.set_repeat(1)

running = True
wszystko = pygame.sprite.Group()
elementyGry = pygame.sprite.Group()
g = czolgGracza.CzolgGracza(100, 100)
maska = pygame.mask.from_surface(pygame.image.load("testowaMaska.png").convert_alpha())
graf = algorytmy.utworzGraf(maska)

elementyGry.add(g)
wszystko.add(g)
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    screen.fill((255, 255, 255))
    wszystko.update(wszystko)
    for duszek in wszystko:
        screen.blit(duszek.surf, duszek.rect)
    pygame.display.flip()
    czas.tick(30)
pygame.quit()
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
gracze = pygame.sprite.Group()
wrogowie = pygame.sprite.Group()
g = czolgGracza.CzolgGracza(100, 100)
s = typyWrogow.Solider(500, 500)
maska = pygame.image.load("testowaMaska.png").convert_alpha()
graf = algorytmy.utworzGraf(maska)

gracze.add(g)
wrogowie.add(s)
wszystko.add(g)
wszystko.add(s)
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    screen.fill((255, 255, 255))
    gracze.update(wszystko)
    wrogowie.update(wszystko, screen.get_width, screen.get_height, graf)
    for duszek in wszystko:
        screen.blit(duszek.surf, duszek.rect)
    pygame.display.flip()
    czas.tick(30)
pygame.quit()
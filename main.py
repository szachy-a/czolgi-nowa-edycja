import pygame
from pygame.locals import (
    QUIT
)
pygame.init()

import czolgGracza
import czolgWroga
import typyWrogow
import usingTkinter
import json

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Czołgi Nowa Edycja')
czas = pygame.time.Clock()
pygame.key.set_repeat(1)

def nowyLevel():
    global level
    global running
    usingTkinter.askAndAdd(g)
    g.hp = g.maxWytrzymalosc
    g.cooldown = 0
    level += 1
    x = 10
    try:
        l = levels[level - 1]
    except IndexError:
        usingTkinter.wygrana()
        running = False
        return
    for cls, pos in l:
        czolg = getattr(typyWrogow, cls)(*pos)
        elementyGry.add(czolg)
        wszystko.add(czolg)

with open('wszystkiePlansze.json') as f:
    levels = json.load(f)
running = True
tlo = pygame.image.load('tlo.png').convert()
wszystko = pygame.sprite.Group()
elementyGry = pygame.sprite.Group()
g = czolgGracza.CzolgGracza(640, 700)
elementyGry.add(g)
wszystko.add(g)
level = 0
nowyLevel()
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    screen.fill((255, 255, 255))
    wszystko.update(wszystko)
    screen.blit(tlo, (0, 0))
    for duszek in wszystko:
        screen.blit(duszek.surf, duszek.rect)
    pygame.display.flip()
    for duszek in elementyGry:
        if isinstance(duszek, czolgWroga.CzolgWroga):
            break
    else:
        nowyLevel()
    for duszek in elementyGry:
        if isinstance(duszek, czolgGracza.CzolgGracza):
            break
    else:
        usingTkinter.przegrana()
        running = False
    czas.tick(30)
pygame.quit()

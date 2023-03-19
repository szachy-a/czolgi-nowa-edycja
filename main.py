import pygame
from pygame.locals import (
    QUIT
)
pygame.init()

import czolgGracza
import czolgWroga
import typyWrogow
import powerups

screen = pygame.display.set_mode((1280, 720))
czas = pygame.time.Clock()
pygame.key.set_repeat(1)

def nowyLevel():
    powerups.askAndAdd(g)
    global level
    g.hp = g.maxWytrzymalosc
    g.cooldown = 0
    level += 1
    x = 10
    c = [typyWrogow.Scout, typyWrogow.Solider, typyWrogow.Juggernaut][level // 3]
    for i in range(level % 3):
        czolg = c(x, 0)
        wszystko.add(czolg)
        elementyGry.add(czolg)
        x += czolg.rect.width + 10


running = True
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
    for duszek in elementyGry:
        if isinstance(duszek, czolgWroga.CzolgWroga):
            break
    else:
        nowyLevel()
    for duszek in elementyGry:
        if isinstance(duszek, czolgGracza.CzolgGracza):
            break
    else:
        running = False
    for duszek in wszystko:
        screen.blit(duszek.surf, duszek.rect)
    pygame.display.flip()
    czas.tick(30)
pygame.quit()
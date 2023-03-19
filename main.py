import pygame
from pygame.locals import (
    QUIT
)
pygame.init()

import czolgGracza
import czolgWroga
import typyWrogow

screen = pygame.display.set_mode((1280, 720))
czas = pygame.time.Clock()
pygame.key.set_repeat(1)

def nowyLevel():
    global level
    g.hp = g.maxWytrzymalosc
    g.cooldown = 0
    level += 1
    x = 10
    for i in range(level):
        s = typyWrogow.Scout(x, 0)
        wszystko.add(s)
        elementyGry.add(s)
        x += s.rect.width // 2 + 10
    for i in range(level // 5):
        s = typyWrogow.Solider(x, 0)
        wszystko.add(s)
        elementyGry.add(s)
        x += s.rect.width // 2 + 10
    for i in range(level // 20):
        b = typyWrogow.Boss(x, 0)
        wszystko.add(b)
        elementyGry.add(b)
        x += b.rect.width // 2 + 10

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
    for duszek in wszystko:
        screen.blit(duszek.surf, duszek.rect)
    pygame.display.flip()
    czas.tick(30)
pygame.quit()
import pygame
from pygame.locals import (
    QUIT
)
pygame.init()

import czolgGracza

screen = pygame.display.set_mode((1366, 768))
czas = pygame.time.Clock()
pygame.key.set_repeat(1)

running = True
wszystko = pygame.sprite.Group()
g = czolgGracza.CzolgGracza(100, 100)
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
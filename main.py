import pygame
from pygame.locals import (
    QUIT
)
pygame.init()

import czolgGracza

realScreen = pygame.display.set_mode((1366, 768))
screen = pygame.Surface((1920, 1080))
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
        g.ruch()
        for duszek in wszystko:
            screen.blit(duszek.surf, duszek.rect)
        pygame.transform.scale(screen, realScreen.get_size(), realScreen)
        pygame.display.flip()
pygame.quit()
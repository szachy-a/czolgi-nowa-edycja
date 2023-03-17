import pygame
from pygame.locals import (
    QUIT
)
pygame.init()

realScreen = pygame.display.set_mode((1366, 768))
screen = pygame.Surface((1920, 1080))

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        screen.fill((255, 255, 255))
        pygame.transform.scale(screen, realScreen.get_size(), realScreen)
        pygame.display.flip()
pygame.quit()
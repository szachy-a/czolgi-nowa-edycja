import pygame
from pygame.locals import (
    QUIT,
    KEYDOWN
)
pygame.init()

import json

screen = pygame.display.set_mode((1280, 720))

for name in ['scout', 'solider', 'juggernaut']:
    exec(f'{name.upper()} = pygame.image.load(name + ".png").convert()')

def dodajCzolg(char):
    if char in ['1', '2', '3']:
        zapis[-1].append([{'1':'Scout', '2':'Solider', '3':'Juggernaut'}[char], list(pygame.mouse.get_pos())])
        wszystko.append(({'1':SCOUT, '2':SOLIDER, '3':JUGGERNAUT}[char], pygame.mouse.get_pos()))
    elif char.lower() == 'n':
        zapis.append([])
        wszystko.clear()

zapis = [[]]
running = True
tlo = pygame.image.load('tlo.png').convert()
wszystko = []
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            dodajCzolg(event.unicode)
    screen.fill((255, 255, 255))
    screen.blit(tlo, (0, 0))
    for elem in wszystko:
        screen.blit(*elem)
    pygame.display.flip()
with open('wszystkiePlansze.json', 'w') as f:
    json.dump(zapis, f)
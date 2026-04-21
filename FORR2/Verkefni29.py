import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('Verkefni 29')

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

DISPLAYSURF.fill(RED)
pygame.draw.rect(DISPLAYSURF, BLUE, (150, 150, 100, 100))
pygame.draw.circle(DISPLAYSURF, GREEN, (200, 200), 50, 0)
pygame.draw.circle(DISPLAYSURF, BLACK, (200, 200), 75, 3)
pygame.draw.line(DISPLAYSURF, YELLOW, (0, 0), (400, 400), 4)
pygame.draw.line(DISPLAYSURF, YELLOW, (0, 400), (400, 0), 4)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        pygame.display.update()

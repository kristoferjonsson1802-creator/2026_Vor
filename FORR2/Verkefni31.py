import pygame, sys
from pygame.locals import *
pygame.init()
FPS = 170
fpsclock = pygame.time.clock()

DISPLAYSURF = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Verkefni 31")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
a = 0
b = 0
c = 0
teljari = 0

while True:
    teljari += 1
    if a< 255:
        a += 1
    elif b< 255:
        b +=1
    else:
        c += 1
        if a == 255 and b == 255 and c == 255:
            a = 0
            b = 0
            c = 0

    fontObj = pygame.font.Font('freesansbold.ttf', 50)
    textSurfaceObj = fontObj.render('Kristofer', True, ())
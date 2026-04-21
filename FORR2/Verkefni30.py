import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Verkefni 30")

clock = pygame.time.Clock()
FPS = 60


mynd = pygame.image.load("cat.png")

x = 0
y = 0

speed = 2
direction_x = 1 
direction_y = 1

step_down = 20

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill((150, 150, 150))

    x += speed * direction_x

    if x + mynd.get_width() >= 400:
        x = 400 - mynd.get_width()
        direction_x = -1
        y += step_down * direction_y

    elif x <= 0:
        x = 0
        direction_x = 1
        y += step_down * direction_y

    if y + mynd.get_height() >= 400:
        direction_y = -1
    elif y <= 0:
        direction_y = 1 

    DISPLAYSURF.blit(mynd, (x, y))

    pygame.display.update()
    clock.tick(FPS)

import pygame, sys, random
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((550, 600))
DISPLAYHEIGHT = DISPLAYSURF.get_height()
DISPLAYWIDTH = DISPLAYSURF.get_width()
pygame.display.set_caption("Antibody Blast!")


def menu():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    
    pygame.display.update()
    
menu()
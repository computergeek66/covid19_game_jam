import pygame, sys
from pygame.locals import *




FPS=60
PLAYER_SPEED = 5

pygame.init()

block = pygame.image.load("sprites/block.png")
blockRect = block.get_bounding_rect()

DISPLAYSURF = pygame.display.set_mode((400, 600))

DISPLAYHEIGHT = DISPLAYSURF.get_height()
DISPLAYWIDTH = DISPLAYSURF.get_width()

pygame.display.set_caption("We have Galaga at home!")

BLACK = (0, 0, 0)


def main():
    fpsClock = pygame.time.Clock()

    global blockRect
    

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        ##Fill the frame with black
        DISPLAYSURF.fill(BLACK)

        keys = pygame.key.get_pressed()

        if keys[K_a]:
            blockRect.x -= PLAYER_SPEED
        if keys[K_d]:
            blockRect.x += PLAYER_SPEED
        if keys[K_w]:
            blockRect.y -= PLAYER_SPEED
        if keys[K_s]:
            blockRect.y += PLAYER_SPEED

        DISPLAYSURF.blit(block, (blockRect.x,blockRect.y))

        pygame.display.update()
        fpsClock.tick(FPS)


main()

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

BG_COLOR = (136, 0, 21)


def main():
    fpsClock = pygame.time.Clock()

    global blockRect
    
    blockRect.x = 0.5 * DISPLAYWIDTH
    blockRect.y = 0.8 * DISPLAYHEIGHT

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        ##Fill the frame with background color
        DISPLAYSURF.fill(BG_COLOR)

        keys = pygame.key.get_pressed()

        if keys[K_a] and blockRect.x > (0):
            blockRect.x -= PLAYER_SPEED
        if keys[K_d] and blockRect.x <= (DISPLAYWIDTH - block.get_width()):
            blockRect.x += PLAYER_SPEED
        if keys[K_w] and blockRect.y > DISPLAYHEIGHT / 2:
            blockRect.y -= PLAYER_SPEED
        if keys[K_s] and blockRect.y <= (DISPLAYHEIGHT - block.get_height()):
            blockRect.y += PLAYER_SPEED

        DISPLAYSURF.blit(block, (blockRect.x,blockRect.y))

        pygame.display.update()
        fpsClock.tick(FPS)


main()

import pygame, sys, random
from pygame.locals import *
from drawable import Drawable

#constants
FPS=60
PLAYER_SPEED = 5
BG_SPRITES = [pygame.image.load("sprites/background/bg1.png"),
              pygame.image.load("sprites/background/bg2.png"),
              pygame.image.load("sprites/background/bg3.png"),
              pygame.image.load("sprites/background/bg4.png")]
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYHEIGHT = DISPLAYSURF.get_height()
DISPLAYWIDTH = DISPLAYSURF.get_width()
BG_COLOR = (136, 0, 21)

bg_tiles = []
block = Drawable(pygame.image.load("sprites/block.png"), (int)(0.5 * DISPLAYWIDTH), (int)(0.8 * DISPLAYHEIGHT))

pygame.init()
pygame.display.set_caption("COVID-19 Game")

def main():
    fpsClock = pygame.time.Clock()

    for i in range(5):
        bg_tile_sprite = random.choice(BG_SPRITES)
        bg_tile = Drawable(bg_tile_sprite, random.randrange(DISPLAYWIDTH), random.randrange(DISPLAYHEIGHT))
        bg_tiles.append(bg_tile)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        ##Fill the frame with background color
        DISPLAYSURF.fill(BG_COLOR)

        for bg_tile in bg_tiles:
            bg_tile.rect.y += 1
            if(bg_tile.rect.y > DISPLAYHEIGHT):
                bg_tile.rect.y = -bg_tile.sprite.get_height()
            DISPLAYSURF.blit(bg_tile.sprite, bg_tile.rect)

        #detect player input
        keys = pygame.key.get_pressed()
        if keys[K_a] and block.rect.x > (0):
            block.rect.x -= PLAYER_SPEED
        if keys[K_d] and block.rect.x <= (DISPLAYWIDTH - block.sprite.get_width()):
            block.rect.x += PLAYER_SPEED
        if keys[K_w] and block.rect.y > DISPLAYHEIGHT / 2:
            block.rect.y -= PLAYER_SPEED
        if keys[K_s] and block.rect.y <= (DISPLAYHEIGHT - block.sprite.get_height()):
            block.rect.y += PLAYER_SPEED

        DISPLAYSURF.blit(block.sprite, block.rect)

        pygame.display.update()
        fpsClock.tick(FPS)


main()

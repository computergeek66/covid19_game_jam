import pygame, sys, random
from pygame.locals import *


class Drawable:
    def __init__(self, sprite, x, y):
        self.sprite = sprite
        self.rect = sprite.get_bounding_rect()
        self.rect.x = x
        self.rect.y = y
    


FPS=60
PLAYER_SPEED = 5

pygame.init()

block = pygame.image.load("sprites/block.png")
blockRect = block.get_bounding_rect()

BG_SPRITES = [pygame.image.load("sprites/background/bg1.png"),
              pygame.image.load("sprites/background/bg2.png")]

DISPLAYSURF = pygame.display.set_mode((400, 600))

DISPLAYHEIGHT = DISPLAYSURF.get_height()
DISPLAYWIDTH = DISPLAYSURF.get_width()

pygame.display.set_caption("We have Galaga at home!")

BG_COLOR = (136, 0, 21)

bg_tiles = []

def main():
    fpsClock = pygame.time.Clock()

    for i in range(5):
        bg_tile_sprite = random.choice(BG_SPRITES)
        bg_tile = Drawable(bg_tile_sprite, random.randrange(DISPLAYWIDTH), random.randrange(DISPLAYHEIGHT))
        #print(bg_tile_rect.x, ", ", bg_tile_rect.y)
        bg_tiles.append(bg_tile)

    print(len(bg_tiles))

    global blockRect
    
    blockRect.x = (int)(0.5 * DISPLAYWIDTH)
    blockRect.y = (int)(0.8 * DISPLAYHEIGHT)

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

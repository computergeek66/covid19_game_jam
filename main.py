import pygame, sys, random
from pygame.locals import *
from drawable import Drawable
from player import Player
from enemy import Enemy
from levels import *

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
BG_COLOR = (140, 0, 21)
BULLET_SPRITE = pygame.image.load("sprites/bullet.png")
BULLET_SPEED = 10
SHOOT_TICKER_MAX = 8
TICK_COUNTER_MAX = 30

bg_tiles = []
player = Player(DISPLAYWIDTH, DISPLAYHEIGHT)
bullets = []
drawables = []
enemies = []

#enemy = Enemy("rb", 200, 0)
#drawables.append(enemy.drawable)
#enemies.append(enemy)

pygame.init()
pygame.display.set_caption("COVID-19 Game")

def main():
    fpsClock = pygame.time.Clock()
    shoot_ticker = 0
    pause_counter = 0
    tick_counter = 0
    current_level_line = 0
    current_level = LEVEL1

    for i in range(40):
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

        #draw background tiles
        for bg_tile in bg_tiles:
            bg_tile.rect.y += 7
            if(bg_tile.rect.y > DISPLAYHEIGHT):
                bg_tile.rect.y = -bg_tile.sprite.get_height()
                bg_tile.rect.x = random.randrange(DISPLAYWIDTH)
            DISPLAYSURF.blit(bg_tile.sprite, bg_tile.rect)

        #detect player movement
        keys = pygame.key.get_pressed()
        player.move_player(keys)
        DISPLAYSURF.blit(player.drawable.sprite, player.drawable.rect)

        #bullet generation logic
        if(keys[K_SPACE] and shoot_ticker == 0):
            shoot_ticker = SHOOT_TICKER_MAX
            bullet_x = (int)(((player.drawable.rect.x * 2) + player.drawable.sprite.get_width() - BULLET_SPRITE.get_width()) / 2)
            bullet_y = player.drawable.rect.y - (int)(BULLET_SPRITE.get_height() / 2)
            bullet = Drawable(BULLET_SPRITE, bullet_x, bullet_y)
            bullets.append(bullet)
        
        for bullet in bullets:
            bullet.rect.y -= BULLET_SPEED
            if(bullet.rect.y < 0 - bullet.sprite.get_height()):
                bullets.remove(bullet)
            DISPLAYSURF.blit(bullet.sprite, bullet.rect)

        #level generation logic
        if(current_level_line >= len(current_level)): 
            current_level_line = 0
        if(tick_counter == TICK_COUNTER_MAX and current_level_line < len(current_level)):
            tick_counter = 0
            if(pause_counter == 0):
                #parse line
                line = list(current_level[current_level_line])
                if(line[0] == 'P'):
                    pause_counter = int(line[1])
                else:
                    for i in range(len(line)):
                        if(line[i] == 'R'):
                            enemy = Enemy("rb", (int)(DISPLAYWIDTH / 8) * i, 0)
                            drawables.append(enemy.drawable)
                            enemies.append(enemy)
                        if(line[i] == 'W'):
                            enemy = Enemy("wb", (int)(DISPLAYWIDTH / 8) * i, 0)
                            drawables.append(enemy.drawable)
                            enemies.append(enemy)
                current_level_line += 1
            else:
                pause_counter -= 1
        else:
            tick_counter += 1

        for enemy in enemies:
            enemy.update()

        for drawable in drawables:
            DISPLAYSURF.blit(drawable.sprite, drawable.rect)

        if shoot_ticker > 0:
            shoot_ticker -= 1

        pygame.display.update()
        fpsClock.tick(FPS)


main()

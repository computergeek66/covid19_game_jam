import pygame, sys, random
from pygame.locals import *
from drawable import Drawable
from player import Player
from enemy import Enemy
from levels import *
from sound import Sound

#initialization of pygame
pygame.init()

#constants
FPS=60
DISPLAYFONT = pygame.font.Font("fonts/arial.ttf", 15)
BG_SPRITES = [pygame.image.load("sprites/background/bg1.png"),
              pygame.image.load("sprites/background/bg2.png"),
              pygame.image.load("sprites/background/bg3.png"),
              pygame.image.load("sprites/background/bg4.png")]
DISPLAYSURF = pygame.display.set_mode((550, 600))
DISPLAYHEIGHT = DISPLAYSURF.get_height()
DISPLAYWIDTH = DISPLAYSURF.get_width()
GUIWIDTH = 150
PLAYWIDTH = DISPLAYWIDTH - GUIWIDTH
BG_COLOR = (140, 0, 21)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BULLET_SPRITE = pygame.image.load("sprites/bullet.png")
BULLET_SPEED = 12
SHOOT_TICKER_MAX = 8
TICK_COUNTER_MAX = 30


bg_tiles = []
player = Player(PLAYWIDTH, DISPLAYHEIGHT)
bullets = []
drawables = []
enemies = []
points = 0
scoreLabelDisplay = None
scoreLabelDisplayRect = None
scoreDisplay = None
scoreDisplayRect = None


pygame.display.set_caption("COVID-19 Game")

def create_GUI():
    global scoreLabelDisplay
    global scoreLabelDisplayRect
    global scoreDisplay
    global scoreDisplayRect
    
    scoreLabelDisplay = DISPLAYFONT.render("SCORE", True, WHITE, BLACK)
    scoreLabelDisplayRect = scoreLabelDisplay.get_rect()
    scoreLabelDisplayRect.centerx = (int)(PLAYWIDTH + GUIWIDTH * 0.2)
    scoreLabelDisplayRect.y = 0
    
    scoreDisplay = DISPLAYFONT.render(str(points), True, WHITE, BLACK)
    scoreDisplayRect = scoreDisplay.get_rect()
    scoreDisplayRect.centerx =  scoreLabelDisplayRect.centerx
    scoreDisplayRect.y = scoreLabelDisplayRect.height
    
def update_GUI():
    global scoreLabelDisplay
    global scoreLabelDisplayRect
    global scoreDisplay
    global scoreDisplayRect
    global points
    

    scoreDisplay = DISPLAYFONT.render(str(points), True, WHITE, BLACK)
    DISPLAYSURF.blit(scoreLabelDisplay, scoreLabelDisplayRect)
    DISPLAYSURF.blit(scoreDisplay, scoreDisplayRect)

def game_over():
    print("Game over")
    pygame.quit()
    sys.exit()

def main():
    fpsClock = pygame.time.Clock()
    shoot_ticker = 0
    pause_counter = 0
    tick_counter = 0
    current_level_line = 0
    current_level = LEVEL1

    global points
    
    create_GUI()

    for i in range(40):
        bg_tile_sprite = random.choice(BG_SPRITES)
        bg_tile = Drawable(bg_tile_sprite, random.randrange(PLAYWIDTH), random.randrange(DISPLAYHEIGHT))
        bg_tiles.append(bg_tile)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        ##Fill the frame with background color
        DISPLAYSURF.fill(BG_COLOR)

        pygame.draw.rect(DISPLAYSURF, BLACK, ((PLAYWIDTH, 0), (GUIWIDTH, DISPLAYHEIGHT)))

        #draw background tiles
        for bg_tile in bg_tiles:
            bg_tile.rect.y += 7
            if(bg_tile.rect.y > DISPLAYHEIGHT):
                bg_tile.rect.y = -bg_tile.sprite.get_height()
                bg_tile.rect.x = random.randrange(PLAYWIDTH)
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
            Sound.play_sound("shoot")
        
        for bullet in bullets:
            bullet.rect.y -= BULLET_SPEED
            if(bullet.rect.y < 0 - bullet.sprite.get_height()):
                bullets.remove(bullet)
            else:
                for enemy in enemies:
                    if(bullet.rect.colliderect(enemy.drawable.rect)):
                        bullets.remove(bullet)
                        if(enemy.take_damage(1)):
                            if(enemy.e_type == "cb" or enemy.e_type == "vb"):
                                points += 100
                            else:
                                points -= 100
                            drawables.remove(enemy.drawable)
                            enemies.remove(enemy)
                            
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
                        enemy_type = ""
                        if(line[i] == 'R'):
                            enemy_type = "rb"
                        if(line[i] == 'W'):
                            enemy_type = "wb"
                        if(line[i] == 'C'):
                            enemy_type = "cb"
                        if(line[i] == 'V'):
                            enemy_type = "vb"
                        if(enemy_type != ""):
                            enemy = Enemy(enemy_type, (int)(PLAYWIDTH / (len(line) + 1)) * (i + 1), 0, PLAYWIDTH)
                            enemy.drawable.rect.x -= (int)(enemy.drawable.sprite.get_width() / 2)
                            drawables.append(enemy.drawable)
                            enemies.append(enemy)
                current_level_line += 1
            else:
                pause_counter -= 1
        else:
            tick_counter += 1

        for enemy in enemies:
            enemy.update()
            if(player.drawable.rect.colliderect(enemy.drawable.rect)):
                if(player.take_damage(1)):
                    game_over()
                if(enemy.e_type == "cb" or enemy.e_type == "vb"):
                    points += 100
                else:
                    points -= 100
                drawables.remove(enemy.drawable)
                enemies.remove(enemy)

        for drawable in drawables:
            DISPLAYSURF.blit(drawable.sprite, drawable.rect)

        if shoot_ticker > 0:
            shoot_ticker -= 1

        update_GUI()
        pygame.display.update()
        fpsClock.tick(FPS)


main()

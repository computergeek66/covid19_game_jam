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
DISPLAYFONT = pygame.font.Font("fonts/slkscr.ttf", 15)
GAMEOVERFONT = pygame.font.Font("fonts/slkscr.ttf", 20)
BG_SPRITES = [[pygame.image.load("sprites/background/bg1.png")],
              [pygame.image.load("sprites/background/bg2.png")],
              [pygame.image.load("sprites/background/bg3.png")],
              [pygame.image.load("sprites/background/bg4.png")]]
DISPLAYSURF = pygame.display.set_mode((550, 600))
DISPLAYHEIGHT = DISPLAYSURF.get_height()
DISPLAYWIDTH = DISPLAYSURF.get_width()
GUIWIDTH = 150
PLAYWIDTH = DISPLAYWIDTH - GUIWIDTH
BG_COLOR = (140, 0, 21)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BULLET_SPRITE = [pygame.image.load("sprites/bullet.png")]
BULLET_SPEED = 12
SHOOT_TICKER_MAX = 30
TICK_COUNTER_MAX = 30


bg_tiles = []
player = Player(PLAYWIDTH, DISPLAYHEIGHT)
bullets = []
drawables = []
enemies = []
game_over = False
you_win = False
points = 0
level = 1
scoreLabelDisplay = None
scoreLabelDisplayRect = None
scoreDisplay = None
scoreDisplayRect = None
healthLabelDisplay = None
healthLabelDisplayRect = None
healthDisplay = None
healthDisplayRect = None
levelLabelDisplay = None
levelLabelDisplayRect = None
levelDisplay = None
levelDisplayRect = None
gameOverDisplay = None
gameOverDisplayRect = None
youWinDisplay = None
youWinDisplayRect = None
scoringGoodDisplay = None
scoringGoodDisplayRect = None
scoringBadDisplay = None
scoringBadDisplayRect = None
scoringVirusDisplay = None
scoringVirusDisplayRect = None

RB_GUI = pygame.image.load("sprites/rb_gui.png")
WB_GUI = pygame.image.load("sprites/wb_gui.png")
CB_GUI = pygame.image.load("sprites/cb_gui.png")
VB_GUI =pygame.image.load("sprites/covid1.png")



#pygame.display.set_caption("Antibody Blast!")

def create_GUI():
    global scoreLabelDisplay
    global scoreLabelDisplayRect
    global scoreDisplay
    global scoreDisplayRect
    global healthLabelDisplay
    global healthLabelDisplayRect
    global healthDisplay
    global healthDisplayRect
    global levelLabelDisplay
    global levelLabelDisplayRect
    global levelDisplay
    global levelDisplayRect
    global gameOverDisplay
    global gameOverDisplayRect
    global youWinDisplay
    global youWinDisplayRect
    global scoringGoodDisplay
    global scoringGoodDisplayRect
    global scoringBadDisplay
    global scoringBadDisplayRect
    global scoringVirusDisplay
    global scoringVirusDisplayRect
    
    scoreLabelDisplay = DISPLAYFONT.render("SCORE", True, WHITE, BLACK)
    scoreLabelDisplayRect = scoreLabelDisplay.get_rect()
    scoreLabelDisplayRect.centerx = (int)(PLAYWIDTH + GUIWIDTH/2)
    scoreLabelDisplayRect.y = 25
    
    scoreDisplay = DISPLAYFONT.render(str(points), True, WHITE, BLACK)
    scoreDisplayRect = scoreDisplay.get_rect()
    scoreDisplayRect.centerx =  scoreLabelDisplayRect.centerx
    scoreDisplayRect.y = scoreLabelDisplayRect.y+scoreLabelDisplayRect.height

    healthLabelDisplay = DISPLAYFONT.render("HEALTH", True, WHITE, BLACK)
    healthLabelDisplayRect = healthLabelDisplay.get_rect()
    healthLabelDisplayRect.centerx = (int)(PLAYWIDTH + GUIWIDTH/2)
    healthLabelDisplayRect.y = 75

    healthDisplay = DISPLAYFONT.render(str(player.health), True, WHITE, BLACK)
    healthDisplayRect = healthDisplay.get_rect()
    healthDisplayRect.centerx = healthLabelDisplayRect.centerx
    healthDisplayRect.y = healthLabelDisplayRect.y+healthLabelDisplayRect.height

    levelLabelDisplay = DISPLAYFONT.render("LEVEL", True, WHITE, BLACK)
    levelLabelDisplayRect = levelLabelDisplay.get_rect()
    levelLabelDisplayRect.centerx = (int)(PLAYWIDTH + GUIWIDTH/2)
    levelLabelDisplayRect.y = 125

    levelDisplay = DISPLAYFONT.render(str(player.health), True, WHITE, BLACK)
    levelDisplayRect = levelDisplay.get_rect()
    levelDisplayRect.centerx = levelLabelDisplayRect.centerx
    levelDisplayRect.y = levelLabelDisplayRect.y+levelLabelDisplayRect.height

    gameOverDisplay = GAMEOVERFONT.render("GAME OVER", True, WHITE, BLACK)
    gameOverDisplayRect = gameOverDisplay.get_rect()
    gameOverDisplayRect.centerx = (int)(PLAYWIDTH * 0.5)
    gameOverDisplayRect.y = (int)(DISPLAYHEIGHT * 0.5)

    youWinDisplay = GAMEOVERFONT.render("YOU WIN", True, WHITE, BLACK)
    youWinDisplayRect = youWinDisplay.get_rect()
    youWinDisplayRect.centerx = (int)(PLAYWIDTH * 0.5)
    youWinDisplayRect.y = (int)(DISPLAYHEIGHT * 0.5)

    scoringGoodDisplay = DISPLAYFONT.render("+50pts", True, WHITE, BLACK)
    scoringGoodDisplayRect = scoringGoodDisplay.get_rect()
    scoringGoodDisplayRect.centerx = PLAYWIDTH+GUIWIDTH/2
    scoringGoodDisplayRect.y = DISPLAYHEIGHT/2 + 50

    scoringBadDisplay = DISPLAYFONT.render("-100pts", True, WHITE, BLACK)
    scoringBadDisplayRect = scoringBadDisplay.get_rect()
    scoringBadDisplayRect.centerx = scoringGoodDisplayRect.centerx
    scoringBadDisplayRect.y = scoringGoodDisplayRect.y + scoringGoodDisplayRect.height + CB_GUI.get_height()+ 16

    scoringVirusDisplay = DISPLAYFONT.render("Avoid!", True, WHITE, BLACK)
    scoringVirusDisplayRect = scoringVirusDisplay.get_rect()
    scoringVirusDisplayRect.centerx = scoringBadDisplayRect.centerx
    scoringVirusDisplayRect.y = scoringBadDisplayRect.y + scoringBadDisplayRect.height + WB_GUI.get_height() +16
    
def update_GUI():
    global scoreLabelDisplay
    global scoreLabelDisplayRect
    global scoreDisplay
    global scoreDisplayRect
    global healthLabelDisplay
    global healthLabelDisplayRect
    global healthDisplay
    global healthDisplayRect
    global levelLabelDisplay
    global levelLabelDisplayRect
    global levelDisplay
    global levelDisplayRect
    global gameOverDisplay
    global gameOverDisplayRect
    global youWinDisplay
    global youWinDisplayRect
    global scoringGoodDisplay
    global scoringGoodDisplayRect
    global scoringBadDisplay
    global scoringBadDisplayRect
    global scoringVirusDisplay
    global scoringVirusDisplayRect
    global points
    global level
    global game_over
    global you_win

    scoreDisplay = DISPLAYFONT.render(str(points), True, WHITE, BLACK)
    healthDisplay = DISPLAYFONT.render(str(player.health), True, WHITE, BLACK)
    levelDisplay = DISPLAYFONT.render(str(level), True, WHITE, BLACK)
    DISPLAYSURF.blit(scoreLabelDisplay, scoreLabelDisplayRect)
    DISPLAYSURF.blit(scoreDisplay, scoreDisplayRect)
    DISPLAYSURF.blit(healthLabelDisplay, healthLabelDisplayRect)
    DISPLAYSURF.blit(healthDisplay, healthDisplayRect)
    DISPLAYSURF.blit(levelLabelDisplay, levelLabelDisplayRect)
    DISPLAYSURF.blit(levelDisplay, levelDisplayRect)

    DISPLAYSURF.blit(scoringGoodDisplay, scoringGoodDisplayRect)
    DISPLAYSURF.blit(CB_GUI, (scoringGoodDisplayRect.centerx-(CB_GUI.get_width()/2), scoringGoodDisplayRect.y + scoringGoodDisplayRect.height))
    DISPLAYSURF.blit(scoringBadDisplay, scoringBadDisplayRect)
    DISPLAYSURF.blit(WB_GUI, (scoringBadDisplayRect.centerx-(WB_GUI.get_width()), scoringBadDisplayRect.y + scoringBadDisplayRect.height))
    DISPLAYSURF.blit(RB_GUI, (scoringBadDisplayRect.centerx+(RB_GUI.get_width()), scoringBadDisplayRect.y + scoringBadDisplayRect.height))
    DISPLAYSURF.blit(scoringVirusDisplay, scoringVirusDisplayRect)
    DISPLAYSURF.blit(VB_GUI, (scoringVirusDisplayRect.centerx-(VB_GUI.get_width()/2), scoringVirusDisplayRect.y + scoringVirusDisplayRect.height))

    if(game_over):
        DISPLAYSURF.blit(gameOverDisplay, gameOverDisplayRect)
    if(you_win):
        DISPLAYSURF.blit(youWinDisplay, youWinDisplayRect)

def main():
    global points
    global level
    global game_over
    global you_win
    global enemies
    global drawables
    fpsClock = pygame.time.Clock()
    shoot_ticker = 0
    pause_counter = 0
    tick_counter = 0
    current_level_line = 0
    current_level = LEVELS[level-1]

    

    Sound.play_loop("level")
    
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
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    shoot_ticker = 0

        ##Fill the frame with background color
        DISPLAYSURF.fill(BG_COLOR)

        pygame.draw.rect(DISPLAYSURF, BLACK, ((PLAYWIDTH, 0), (GUIWIDTH, DISPLAYHEIGHT)))

        #draw background tiles
        for bg_tile in bg_tiles:
            bg_tile.rect.y += 15
            if(bg_tile.rect.y > DISPLAYHEIGHT):
                bg_tile.rect.y = -bg_tile.sprite.get_height()
                bg_tile.rect.x = random.randrange(PLAYWIDTH)
            DISPLAYSURF.blit(bg_tile.sprite, bg_tile.rect)

        #detect player movement
        if(not game_over and not you_win):
            keys = pygame.key.get_pressed()
            player.move_player(keys)

            #bullet generation logic
            if(keys[K_SPACE] and shoot_ticker == 0):
                Sound.play_sound("shoot")
                shoot_ticker = SHOOT_TICKER_MAX
                bullet_x = (int)(((player.drawable.rect.x * 2) + player.drawable.sprite.get_width() - BULLET_SPRITE[0].get_width()) / 2)
                bullet_y = player.drawable.rect.y - (int)(BULLET_SPRITE[0].get_height() / 2)
                bullet = Drawable(BULLET_SPRITE, bullet_x, bullet_y)
                bullets.append(bullet)
                
            
            for bullet in bullets:
                bullet.rect.y -= BULLET_SPEED
                if(bullet.rect.y < 0 - bullet.sprite.get_height()):
                    bullets.remove(bullet)
                else:
                    for enemy in enemies:
                        if(bullet.rect.colliderect(enemy.drawable.rect)):
                            if(bullet in bullets):
                                bullets.remove(bullet)
                            if(enemy.take_damage(1)):
                                if(enemy.e_type == "cb" or enemy.e_type == "vb"):
                                    Sound.play_sound("smallexplode")
                                    points += 100
                                else:
                                    Sound.play_sound("allydamage")
                                    points -= 100
                                    if(points < 0): points = 0
                DISPLAYSURF.blit(bullet.sprite, bullet.rect)

            #level generation logic
            #level increment logic
            if(current_level_line >= len(current_level) and not drawables):
                tick_counter = -30
                current_level_line = 0
                level += 1
                if(level <= len(LEVELS)):
                    current_level = LEVELS[level-1]
                    player.heal_player()
                else:
                    current_level = ['']
                    Sound.stop_sound("level")
                    Sound.play_sound("win")
                    you_win = True
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
                                enemy = Enemy(enemy_type, (int)(PLAYWIDTH / (len(line) + 1)) * (i + 1), -64, PLAYWIDTH)
                                enemy.drawable.rect.x -= (int)(enemy.drawable.sprite.get_width() / 2)
                                drawables.append(enemy.drawable)
                                enemies.append(enemy)
                    current_level_line += 1
                else:
                    pause_counter -= 1
            else:
                tick_counter += 1
            
            #enemy collision
            for enemy in enemies:
                enemy.update()
                if(player.drawable.rect.colliderect(enemy.drawable.rect) and not enemy.dying):
                    if(enemy.e_type == "cb"):
                        if(player.damage_counter <= 0):
                            enemy.take_damage(enemy.health)
                            points += 50
                        if(player.take_damage(1)):
                            game_over = True
                    elif(enemy.e_type == "vb"):
                        enemy.take_damage(enemy.health)
                        if(player.take_damage(1)):
                            game_over = True
                    elif(player.damage_counter <= 0):
                        points -= 100
                        if(points < 0): points = 0
                        player.take_damage(0)
                        enemy.take_damage(enemy.health)
                if(enemy.health < 0):
                    drawables.remove(enemy.drawable)
                    enemies.remove(enemy)
                if(enemy.drawable.rect.y > DISPLAYHEIGHT and enemy in enemies):
                    enemies.remove(enemy)
        else:
            keys = pygame.key.get_pressed()
            if(keys[K_SPACE] or keys[K_RETURN] or keys[K_ESCAPE]):
                player.reset_position()
                game_over = False
                you_win = False
                level = 1
                score = 0
                drawables = []
                enemies = []
                main()

        for drawable in drawables:
            if(drawable.rect.y > DISPLAYHEIGHT):
                drawables.remove(drawable)
            else:
                DISPLAYSURF.blit(drawable.sprite, drawable.rect)
        
        if(player.damage_counter % 2 == 0):
            DISPLAYSURF.blit(player.drawable.sprite, player.drawable.rect)

        if shoot_ticker > 0:
            shoot_ticker -= 1

        update_GUI()
        pygame.display.update()
        fpsClock.tick(FPS)



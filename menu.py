import pygame, sys, random
from pygame.locals import *
from main import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((550, 600))
DISPLAYHEIGHT = DISPLAYSURF.get_height()
DISPLAYWIDTH = DISPLAYSURF.get_width()
pygame.display.set_caption("Antibody Blast!")


BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255, 255, 0)

TITLEFONT = pygame.font.Font("fonts/slkscrb.ttf", 36)
OPTIONFONT = pygame.font.Font("fonts/slkscr.ttf", 20)

FPS = 60

def credits():
    creditsDisplay = TITLEFONT.render("Developed by:", True, WHITE, BLACK)
    creditsDisplayRect = creditsDisplay.get_rect()
    creditsDisplayRect.centerx = DISPLAYWIDTH/2
    creditsDisplayRect.y = 50


    creditsNoah = TITLEFONT.render("Noah Kelley", True, WHITE, BLACK)
    creditsNoahRect = creditsNoah.get_rect()
    creditsNoahRect.centerx = DISPLAYWIDTH/2
    creditsNoahRect.y = creditsDisplayRect.y + 2*creditsDisplayRect.height

    creditsAnd = TITLEFONT.render("&", True, WHITE, BLACK)
    creditsAndRect = creditsAnd.get_rect()
    creditsAndRect.centerx = DISPLAYWIDTH/2
    creditsAndRect.y = creditsNoahRect.y + 2*creditsNoahRect.height

    creditsTrey = TITLEFONT.render("Trey McGinnis", True, WHITE, BLACK)
    creditsTreyRect = creditsTrey.get_rect()
    creditsTreyRect.centerx = DISPLAYWIDTH/2
    creditsTreyRect.y = creditsAndRect.y + 2*creditsAndRect.height


    creditsExit = OPTIONFONT.render("Press ESC to return to menu", True, WHITE, BLACK)
    creditsExitRect = creditsExit.get_rect()
    creditsExitRect.x = 0
    creditsExitRect.y = DISPLAYHEIGHT-creditsExitRect.height


    return_menu = False
    while return_menu == False:

        DISPLAYSURF.fill(BLACK)
        
        DISPLAYSURF.blit(creditsDisplay, creditsDisplayRect)
        DISPLAYSURF.blit(creditsNoah, creditsNoahRect)
        DISPLAYSURF.blit(creditsAnd, creditsAndRect)
        DISPLAYSURF.blit(creditsTrey, creditsTreyRect)
        DISPLAYSURF.blit(creditsExit, creditsExitRect)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[K_ESCAPE]:
            return_menu = True

        pygame.display.update()

    menu()


def menu():

    fpsClock = pygame.time.Clock()
    titleDisplay = TITLEFONT.render("antibody blast!", True, WHITE, BLACK)
    titleDisplayRect = titleDisplay.get_rect()
    titleDisplayRect.centerx = DISPLAYWIDTH / 2
    titleDisplayRect.y = 50

    playDisplay = OPTIONFONT.render("Play", True, WHITE, BLACK)
    playDisplayRect = playDisplay.get_rect()
    playDisplayRect.centerx = DISPLAYWIDTH/2
    playDisplayRect.y = DISPLAYHEIGHT*0.6

    creditsDisplay = OPTIONFONT.render("Credits", True, WHITE, BLACK)
    creditsDisplayRect = creditsDisplay.get_rect()
    creditsDisplayRect.centerx = DISPLAYWIDTH/2
    creditsDisplayRect.y = playDisplayRect.y+playDisplayRect.height

    quitDisplay = OPTIONFONT.render("Quit", True, WHITE, BLACK)
    quitDisplayRect = quitDisplay.get_rect()
    quitDisplayRect.centerx = DISPLAYWIDTH/2
    quitDisplayRect.y = creditsDisplayRect.y+creditsDisplayRect.height

    optionsColorList = [YELLOW, WHITE, WHITE]
    selected = 0

    MOVETICKERMAX = 15
    moveTicker = 0

    play = False

    selection = ''

    while play == False:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[K_UP] and moveTicker < 0:
            if selected > 0:
                selected -= 1
            else:
                selected = len(optionsColorList)-1
            moveTicker = MOVETICKERMAX

        if keys[K_DOWN] and moveTicker < 0:
            if selected < len(optionsColorList)-1:
                selected += 1
            else:
                selected = 0
            moveTicker = MOVETICKERMAX

        if keys[K_RETURN] and moveTicker < 0:
            if selected == 0:
                print("Play game")
                selection = "play"
                play = True
            if selected == 1:
                print("credits")
                selection = "credits"
                play = True
            if selected == 2:
                print("quit")
                pygame.quit()
                sys.exit()
            moveTicker = MOVETICKERMAX

        if moveTicker >= 0:
            moveTicker-=1

        for i in range(len(optionsColorList)):
            if i == selected:
                optionsColorList[i] = YELLOW
            else:
                optionsColorList[i] = WHITE
        DISPLAYSURF.fill(BLACK)

        playDisplay = OPTIONFONT.render("Play", True, optionsColorList[0], BLACK)
        creditsDisplay = OPTIONFONT.render("Credits", True, optionsColorList[1], BLACK)
        quitDisplay = OPTIONFONT.render("Quit", True, optionsColorList[2], BLACK)


        DISPLAYSURF.blit(titleDisplay, titleDisplayRect)
        DISPLAYSURF.blit(playDisplay, playDisplayRect)
        DISPLAYSURF.blit(creditsDisplay, creditsDisplayRect)
        DISPLAYSURF.blit(quitDisplay, quitDisplayRect)
        
        fpsClock.tick(FPS)
        pygame.display.update()

    if selection == "play":
        main()
    if selection == "credits":
        credits()
    
menu()


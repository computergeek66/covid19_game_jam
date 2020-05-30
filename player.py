import pygame
from pygame.locals import *
from drawable import Drawable

#constants
PLAYER_SPRITE = "sprites/block.png"
PLAYER_SPEED = 5

class Player:
    def __init__(self, displayWidth, displayHeight):
        self.drawable = Drawable(pygame.image.load(PLAYER_SPRITE), (int)(0.5 * displayWidth), (int)(0.8 * displayHeight))
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight
    
    def move_player(self, keys):
        if keys[K_a] and self.drawable.rect.x > (0):
            self.drawable.rect.x -= PLAYER_SPEED
        if keys[K_d] and self.drawable.rect.x <= (self.displayWidth - self.drawable.sprite.get_width()):
            self.drawable.rect.x += PLAYER_SPEED
        if keys[K_w] and self.drawable.rect.y > self.displayHeight / 2:
            self.drawable.rect.y -= PLAYER_SPEED
        if keys[K_s] and self.drawable.rect.y <= (self.displayHeight - self.drawable.sprite.get_height()):
            self.drawable.rect.y += PLAYER_SPEED
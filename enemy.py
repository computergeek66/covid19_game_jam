import pygame
from pygame.locals import *
from drawable import Drawable

RB_SPRITE = "sprites/rb.png"
WB_SPRITE = "sprites/wb.png"

class Enemy:
    def __init__(self, e_type, x, y):
        self.x = x
        self.y = y
        self.e_type = e_type
        if(self.e_type == "rb"):
            self.sprite = pygame.image.load(RB_SPRITE)
            self.speed = 3

        if(self.e_type == "wb"):
            self.sprite = pygame.image.load(WB_SPRITE)
            self.speed = 4

        self.drawable = Drawable(self.sprite, x, y)
    

    def update(self): 
        self.drawable.rect.y += self.speed

            
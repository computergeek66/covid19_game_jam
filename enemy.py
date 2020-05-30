import pygame
from pygame.locals import *
from drawable import Drawable

RB_SPRITE = "sprites/rb.png"

class Enemy:
    def __init__(self, e_type, x, y):
        self.x = x
        self.y = y
        self.e_type = e_type
        if(self.e_type == "rb"):
            self.sprite = pygame.image.load(RB_SPRITE)
            self.speed = 3

        self.drawable = Drawable(self.sprite, x, y)
    

    def update(self): 
        if(self.e_type == "rb"):
            self.drawable.rect.y += self.speed

            
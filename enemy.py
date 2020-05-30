import pygame
from pygame.locals import *
from drawable import Drawable

RB_SPRITE = "sprites/rb.png"
WB_SPRITE = "sprites/wb.png"
CB_SPRITE = "sprites/cb.png"
VB_SPRITES = ["sprites/covid1.png",
              "sprites/covid2.png",
              "sprites/covid3.png",
              "sprites/covid4.png"]

class Enemy:
    def __init__(self, e_type, x, y):
        self.x = x
        self.y = y
        self.e_type = e_type
        if(self.e_type == "rb"):
            self.sprite = pygame.image.load(RB_SPRITE)
            self.speed = 3
            self.drawable = Drawable(self.sprite, x-self.sprite.get_width()/2, y-self.sprite.get_height()/2)
            self.health = 2

        if(self.e_type == "wb"):
            self.sprite = pygame.image.load(WB_SPRITE)
            self.speed = 4
            self.drawable = Drawable(self.sprite, x-self.sprite.get_width()/2, y-self.sprite.get_height()/2)
            self.health = 5

        if(self.e_type == "cb"):
            self.sprite = pygame.image.load(CB_SPRITE)
            self.speed = 2
            self.drawable = Drawable(self.sprite, x-self.sprite.get_width()/2, y-self.sprite.get_height()/2)
            self.health = 1

        if(self.e_type == "vb"):
            self.sprite = pygame.image.load(VB_SPRITES[0])
            self.speed = 2
            self.drawable = Drawable(self.sprite, x-self.sprite.get_width()/2, y-self.sprite.get_height()/2)
            self.health = 99

        
    

    def update(self): 
        self.drawable.rect.y += self.speed

    def take_damage(self, damage):
        dead = False
        self.health -= damage
        if(self.health <= 0):
            dead = True
        return dead
            

            
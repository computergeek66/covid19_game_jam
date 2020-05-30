import pygame, random
from pygame.locals import *
from drawable import Drawable

RB_SPRITE = "sprites/rb.png"
WB_SPRITE = "sprites/wb.png"
CB_SPRITE = "sprites/cb.png"
WB_DEATH = ["sprites/wb_death1.png",
            "sprites/wb_death2.png",
            "sprites/wb_death3.png",
            "sprites/wb_death4.png",
            "sprites/wb_death5.png"]
VB_SPRITES = ["sprites/covid1.png",
              "sprites/covid2.png",
              "sprites/covid3.png",
              "sprites/covid4.png",
              "sprites/covid3.png",
              "sprites/covid2.png"]

class Enemy:
    def __init__(self, e_type, x, y, playWidth):
        self.x = x
        self.y = y
        self.velocity = random.randrange(-3, 3)
        self.playWidth = playWidth
        self.e_type = e_type
        self.dying = False
        if(self.e_type == "rb"):
            self.sprite = pygame.image.load(RB_SPRITE)
            self.speed = 5
            self.drawable = Drawable(self.sprite, x, y)
            self.health = 2

        if(self.e_type == "wb"):
            sprites= []
            for sprite in WB_DEATH:
                sprites.append(pygame.image.load(sprite))
            self.sprite = sprites[0]
            self.speed = 6
            self.drawable = Drawable.animated_drawable(sprites[0], sprites, x, y)
            
            self.health = 1

        if(self.e_type == "cb"):
            self.sprite = pygame.image.load(CB_SPRITE)
            self.speed = 4
            self.drawable = Drawable(self.sprite, x, y)
            self.health = 1

        if(self.e_type == "vb"):
            sprites= []
            for sprite in VB_SPRITES:
                sprites.append(pygame.image.load(sprite))
            self.sprite = sprites[0]
            self.speed = 4+random.uniform(-1.5, 2)
            self.drawable = Drawable.animated_drawable(sprites[0], sprites, x, y)
            self.drawable.initialize_animation(5,0)
            self.health = 99

        
    

    def update(self):
        if(self.drawable.rect.x < 0 or self.drawable.rect.x > (self.playWidth - self.sprite.get_width())):
            self.velocity *= -1
        self.drawable.rect.x += self.velocity
        self.drawable.rect.y += self.speed

        if(self.e_type == "vb"):
            self.drawable.animate()
        else:
            if(self.dying):
                if(self.drawable.animate()):
                    self.health = -99

    def take_damage(self, damage):
        dead = False
        
        if(self.health <= 0):
            dead = True
            if(self.e_type == "wb"):
                self.dying = True
                self.drawable.initialize_animation(5,0)
        else:
            self.health -= damage
        return dead
            

            
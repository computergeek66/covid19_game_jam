import pygame, random
from pygame.locals import *
from drawable import Drawable

WB_DEATH = [pygame.image.load("sprites/wb_death1.png"),
            pygame.image.load("sprites/wb_death2.png"),
            pygame.image.load("sprites/wb_death3.png"),
            pygame.image.load("sprites/wb_death4.png"),
            pygame.image.load("sprites/wb_death5.png")]

RB_SPRITES = [pygame.image.load("sprites/rb_death1.png"),
              pygame.image.load("sprites/rb_death2.png"),
              pygame.image.load("sprites/rb_death3.png"),
              pygame.image.load("sprites/rb_death4.png"),
              pygame.image.load("sprites/rb_death5.png"),
              pygame.image.load("sprites/rb_death6.png")]

CB_SPRITES = [pygame.image.load("sprites/cb_death1.png"),
              pygame.image.load("sprites/cb_death2.png"),
              pygame.image.load("sprites/cb_death3.png"),
              pygame.image.load("sprites/cb_death4.png"),
              pygame.image.load("sprites/cb_death5.png"),
              pygame.image.load("sprites/cb_death6.png")]

VB_SPRITES = [pygame.image.load("sprites/covid1.png"),
              pygame.image.load("sprites/covid2.png"),
              pygame.image.load("sprites/covid3.png"),
              pygame.image.load("sprites/covid4.png"),
              pygame.image.load("sprites/covid3.png"),
              pygame.image.load("sprites/covid2.png")]

class Enemy:
    def __init__(self, e_type, x, y, playWidth):
        self.x = x
        self.y = y
        self.velocity = random.randrange(-3, 3)
        self.playWidth = playWidth
        self.e_type = e_type
        self.dying = False
        if(self.e_type == "rb"):
            self.sprites = RB_SPRITES
            self.sprite = self.sprites[0]
            self.speed = 5
            self.drawable = Drawable( self.sprites, x, y)
            self.health = 2

        if(self.e_type == "wb"):
            self.sprites = WB_DEATH
            self.sprite = self.sprites[0]
            self.speed = 6
            self.drawable = Drawable(self.sprites, x, y)
            
            self.health = 1

        if(self.e_type == "cb"):
            self.sprites = CB_SPRITES
            self.sprite = self.sprites[0]
            self.speed = 4
            self.drawable = Drawable(self.sprites, x, y)
            self.health = 1

        if(self.e_type == "vb"):
            self.sprites = VB_SPRITES
            self.sprite = self.sprites[0]
            self.speed = 4+random.uniform(-1.5, 2)
            self.drawable = Drawable(self.sprites, x, y)
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
        self.dead = False
        
        if(self.health <= 0):
            self.dead = True
            if(self.e_type != "vb"):
                self.dying = True
                self.drawable.initialize_animation(5,0)
        else:
            self.health -= damage
        return self.dead
            

            
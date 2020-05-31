import pygame
from pygame.locals import *
from drawable import Drawable
from sound import Sound

#constants
PLAYER_SPRITE = [pygame.image.load("sprites/player.png"),
                 pygame.image.load("sprites/player.png")]
PLAYER_SPEED = 7
MAX_HEALTH = 10
DAMAGE_COUNTER_MAX = 60

class Player:
    def __init__(self, displayWidth, displayHeight):
        self.drawable = Drawable(PLAYER_SPRITE, (int)(0.5 * displayWidth), (int)(0.8 * displayHeight))
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight
        self.health = MAX_HEALTH
        self.damage_counter = 0
    
    def move_player(self, keys):
        if keys[K_a] and self.drawable.rect.x > (0):
            self.drawable.rect.x -= PLAYER_SPEED
        if keys[K_d] and self.drawable.rect.x <= (self.displayWidth - self.drawable.sprite.get_width()):
            self.drawable.rect.x += PLAYER_SPEED
        if keys[K_w] and self.drawable.rect.y > self.displayHeight * 0.35:
            self.drawable.rect.y -= PLAYER_SPEED
        if keys[K_s] and self.drawable.rect.y <= (self.displayHeight - self.drawable.sprite.get_height()):
            self.drawable.rect.y += PLAYER_SPEED
        if(self.damage_counter > 0):
            self.damage_counter -= 1
    
    def take_damage(self, damage):
        dead = False
        if(self.damage_counter <= 0):
            self.damage_counter = DAMAGE_COUNTER_MAX
            self.health -= damage
            self.rstep = (int)((255-32)/MAX_HEALTH)
            self.gstep = (int)((255-205)/MAX_HEALTH)
            self.bstep = (int)((255-32)/MAX_HEALTH)
            self.drawable.sprite.fill((self.rstep,self.gstep,self.bstep), special_flags=pygame.BLEND_SUB)
            if(self.health <= 0):
                Sound.play_sound("death")
                dead = True
            elif(self.health == 0.2 * MAX_HEALTH):
                Sound.play_sound("lowhealth")
            else:
                Sound.play_sound("playerdamage")
        return dead
    
    def heal_player(self):
        self.health = MAX_HEALTH
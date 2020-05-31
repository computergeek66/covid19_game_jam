import pygame
from pygame.locals import *
from drawable import Drawable
from sound import Sound

#constants
PLAYER_SPRITE = "sprites/player.png"
PLAYER_SPEED = 7
MAX_HEALTH = 10
DAMAGE_COUNTER_MAX = 60

class Player:
    def __init__(self, displayWidth, displayHeight):
        self.drawable = Drawable(pygame.image.load(PLAYER_SPRITE), (int)(0.5 * displayWidth), (int)(0.8 * displayHeight))
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
            if(self.health <= 0):
                Sound.play_sound("death")
                dead = True
            elif(self.health == 0.2 * MAX_HEALTH):
                Sound.play_sound("lowhealth")
            else:
                Sound.play_sound("playerdamage")
        return dead
import pygame

pygame.mixer.init()
sounds = {"shoot": pygame.mixer.Sound("sounds/sfx_wpn_laser8.wav")}

class Sound:
    @staticmethod
    def play_sound(sound):
        global sounds
        sounds[sound].play()
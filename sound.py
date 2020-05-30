import pygame

pygame.mixer.init()
sounds = {"shoot": pygame.mixer.Sound("sounds/sfx_wpn_laser8.wav"),
          "smallexplode": pygame.mixer.Sound("sounds/sfx_exp_shortest_soft2.wav"),
          "playerdamage": pygame.mixer.Sound("sounds/sfx_sounds_impact1.wav"),
          "allydamage": pygame.mixer.Sound("sounds/sfx_sounds_damage1.wav"),
          "lowhealth": pygame.mixer.Sound("sounds/sfx_lowhealth_alarmloop6.wav"),
          "death": pygame.mixer.Sound("sounds/sfx_deathscream_human10.wav") }

class Sound:
    @staticmethod
    def play_sound(sound):
        global sounds
        sounds[sound].play()
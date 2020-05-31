import pygame

pygame.mixer.init()
sounds = {"shoot": pygame.mixer.Sound("sounds/sfx_wpn_laser8.wav"),
          "smallexplode": pygame.mixer.Sound("sounds/sfx_exp_shortest_soft2.wav"),
          "playerdamage": pygame.mixer.Sound("sounds/sfx_sounds_impact1.wav"),
          "allydamage": pygame.mixer.Sound("sounds/sfx_sounds_damage1.wav"),
          "lowhealth": pygame.mixer.Sound("sounds/sfx_lowhealth_alarmloop6.wav"),
          "death": pygame.mixer.Sound("sounds/sfx_deathscream_human10.wav"),
          "menu": pygame.mixer.Sound("sounds/music/Menu.wav"), 
          "level": pygame.mixer.Sound("sounds/music/Mars.wav"),
          "move": pygame.mixer.Sound("sounds/sfx_menu_move2.wav"),
          "select": pygame.mixer.Sound("sounds/sfx_menu_select1.wav"),
          "heal": pygame.mixer.Sound("sounds/sfx_sounds_powerup16.wav")}

class Sound:
    @staticmethod
    def play_sound(sound):
        global sounds
        sounds[sound].play()

    @staticmethod
    def stop_sound(sound):
        global sounds
        pygame.mixer.fadeout(1000)
        sounds[sound].stop()

    @staticmethod
    def play_loop(sound):
        global sounds
        sounds[sound].play(loops=-1)
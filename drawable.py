class Drawable:
    def __init__(self, sprites, x, y):
        self.sprites = sprites
        self.sprite = self.sprites[0]
        self.rect = self.sprite.get_bounding_rect()
        self.rect.x = x
        self.rect.y = y
        self.sprite_index = 0
        self.duration = 0
        self.countdown = 0        


    def initialize_animation(self, duration, start_time):
        self.duration = duration
        self.countdown = start_time

    def animate(self):
        atEnd = False
        if(self.countdown>0):
            self.countdown -=1
        else:
            if(self.sprite_index < len(self.sprites)-1):
                self.sprite_index += 1
                
            else:
                self.sprite_index = 0
                atEnd = True
            self.sprite = self.sprites[self.sprite_index]
            self.countdown = self.duration
            
        return atEnd
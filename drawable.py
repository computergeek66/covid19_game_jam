class Drawable:
    def __init__(self, sprite, x, y):
        self.sprite = sprite
        self.rect = sprite.get_bounding_rect()
        self.rect.x = x
        self.rect.y = y
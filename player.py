import os
import pygame as pg

# Create a Player class that is a subclass of pygame.sprite.Sprite
# Load an image as such:
#        self.image = pg.image.load(os.path.join('assets', 'Ship6.png')).convert_alpha()
# The position is controlled by the rectangle surrounding the image.
# Set self.rect = self.image.get_rect().  Then make changes to the 
# rectangle x, y or centerx and centery to move the object.

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        pg.sprite.Sprite.__init__(self)
        self.images = []
        img = pg.image.load(os.path.join('assets', 'Ship2.png')).convert_alpha()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.lives = 3
        self.speed = 10


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        pass

    def up(self, delta):
        self.rect.y -= 1 * self.speed

    def down(self, delta):
        self.rect.y += 1 * self.speed

import os
import pygame as pg

class Enemy(pg.sprite.Sprite):
    def __init__(self, x):
        super(Enemy, self).__init__()
        pg.sprite.Sprite.__init__(self)
        self.images = []
        img = pg.image.load(os.path.join('assets', 'Ship1.png')).convert_alpha()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        #self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        pass

    def up(self, delta):
        self.rect.y -= 1

    def down(self, delta):
        self.rect.y += 1

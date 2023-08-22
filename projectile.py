import os
import pygame as pg

class Projectile(pg.sprite.Sprite):
    def __init__(self, shipLocation, enemies):
        super(Projectile, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'shot.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = shipLocation.x + 100
        self.rect.centery = shipLocation.y + 37
        self.enemies = enemies
        self.event = pg.USEREVENT + 1
        self.fireSound = pg.mixer.Sound(os.path.join('assets', 'fire.wav'))
        self.fireSound.play()
        self.explosionSound = pg.mixer.Sound(os.path.join('assets', 'explosion.wav'))
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        self.rect.x += 1000 * delta
        if self.rect.x > 1024:
            self.kill()
        collision = pg.sprite.spritecollideany(self, self.enemies)
        if collision:
            collision.kill()
            pg.event.post(pg.event.Event(self.event))
            self.explosionSound.play()
            self.kill()


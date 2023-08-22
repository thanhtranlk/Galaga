import os
import pygame as pg

class EnemyProjectile(pg.sprite.Sprite):
    def __init__(self, shipLocation, player):
        super(EnemyProjectile, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'shot.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = shipLocation.x + 10
        self.rect.centery = shipLocation.y + 10
        self.enemies = player
        self.event = pg.USEREVENT + 2
        self.fireSound = pg.mixer.Sound(os.path.join('assets', 'fire.wav'))
        self.fireSound.play()
        self.explosionSound = pg.mixer.Sound(os.path.join('assets', 'explosion.wav'))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        self.rect.x -= 1000 * delta
        if self.rect.x < 0:
            self.kill()
        playerCollision = pg.sprite.collide_rect(self, self.enemies)
        if playerCollision:
            pg.event.post(pg.event.Event(self.event))
            self.explosionSound.play()
            self.kill()
    
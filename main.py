#!/usr/bin/env python3

import pygame as pg
import pygame.freetype
import os
import random
from enemy import Enemy
from player import Player
from projectile import Projectile
from pygame.locals import *
from enemyProjectile import EnemyProjectile

def main():
    # Startup pygame
    pg.init()

    # Get a screen object
    screen = pg.display.set_mode([1024, 768])
    
    # Create a player
    player = Player()
    player.rect.x=0
    player.rect.y=100
    player_list = pg.sprite.Group()

    # Create enemy and projectile Groups
    projectiles = pg.sprite.Group()
    enemyProjectiles = pg.sprite.Group()

    enemies = pg.sprite.Group()
    enemylist = []
    for i in range(500, 1000, 75):
        for j in range(100, 600, 50):
            enemy = Enemy((i))
            enemy.rect.x=i
            enemy.rect.y=j
            enemies.add(enemy)
            enemylist.append(enemy)
    
    bg = pg.image.load('assets/galaxy.png').convert()
    bg = pg.transform.scale(bg, (1024, 780))
    

    # Start sound - Load background music and start it
    # playing on a loop
    pg.mixer.init()
    music = pg.mixer.music.load(os.path.join('assets', 'POL-star-way-short.wav'))
    pg.mixer.music.set_volume(0.05)
    pg.mixer.music.play(-1)

    # Get font setup
    pg.freetype.init()
    font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./assets", "PermanentMarker-Regular.ttf")
    font_size = 64
    font = pg.freetype.Font(font_path, font_size)
    # Make a tuple for FONTCOLOR
    FONTCOLOR = (109, 72, 156)
    # Startup the main game loop
    running = True
    # Keep track of time
    delta = 0
    # can't fire more than once every 250ms
    shotDelta = 250
    enemyShotDelta = 1000
    # Frame limiting
    fps = 60
    clock = pg.time.Clock()
    clock.tick(fps)
    # Setup score variable
    score = 0

    while running:

        # First thing need to clear the events.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.USEREVENT + 1:
                score += 100
            if event.type == pg.USEREVENT + 2:
                player.lives -= 1

        keys = pg.key.get_pressed()

        if keys[K_s]:
            player.down(delta)
        if keys[K_w]:
            player.up(delta)
        if keys[K_SPACE]:
            if shotDelta >= .25:
                projectile = Projectile(player.rect, enemies)
                projectiles.add(projectile)
                shotDelta = 0

        if enemyShotDelta >= 1 :
            shooting = random.choice(enemylist)
            enemyProjectile = EnemyProjectile(shooting.rect, player)
            enemyProjectiles.add(enemyProjectile)
            enemyShotDelta = 0
        
        # update objects!
        player.update(delta)
        for enemy in enemies:
            enemy.update(delta)
        for projectile in projectiles:
            projectile.update(delta)
        for enemyProjectile in enemyProjectiles:
          enemyProjectile.update(delta)

        # Objects are updated, now  draw!
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        player.draw(screen)
        enemies.draw(screen)
        projectiles.draw(screen)
        enemyProjectiles.draw(screen)
        font.render_to(screen, (10, 10), "Score: " + str(score) + " Lives: " + str(player.lives), FONTCOLOR, None, size=64)

        # When drawing is done, flip the buffer.
        pg.display.flip()

        
        delta = clock.tick(fps) / 1000.0
        shotDelta += delta
        enemyShotDelta += delta

        #game exits 
        if(score == 7000 or player.lives == 0) :
           running = False  

# Startup the main method to get things going.
if __name__ == "__main__":
    main()
    pg.quit()

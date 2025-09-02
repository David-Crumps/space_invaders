import pygame
import os
from player import Player
from invader import Invader
from sprite_pool import SpritePool
from InvaderSpawnManager import InvaderSpawnManager
from bullet import Bullet
from utils import bullet_spawn_strat, barrier_spawn_strat, barrier_spawn_loc
from barrier import Barrier
import sys
import json
import random
from configs import INVADER_SIZE, BULLET_SIZE, PLAYER_SIZE

#ADD TO CONFIGS, ALSO CREATE A CONFIG.PY WHICH HAS ALL THESE VALUES LOADED TO MAKE MAIN READABLE
bullet_cooldown = 250
last_shot_time = 0

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.join(BASE_DIR, '..')
DATA = os.path.join(PROJECT_ROOT, 'Data')

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1920, 1080))

    player_img = pygame.transform.scale(pygame.image.load(os.path.join(DATA, "player.png")), PLAYER_SIZE)
    player_speed = 450

    player = Player([960, 1030], player_img, player_speed)

    invader_img = pygame.transform.scale(pygame.image.load(os.path.join("Data", "invader.png")), INVADER_SIZE)

    invader_group = SpritePool(cls=Invader, size = 12, spawn_strategy=InvaderSpawnManager(), image=invader_img, speed=150)
    for _ in range(len(invader_group)):
        invader_group.spawn(invader_group.get_all_active_sprites())

    bullet_img = pygame.transform.scale(pygame.image.load(os.path.join("Data", "bullet.png")), BULLET_SIZE)
    bullet_group = SpritePool(cls=Bullet, size=10, spawn_strategy=bullet_spawn_strat ,image=bullet_img, speed=600)

    barrier_img = pygame.transform.scale(pygame.image.load(os.path.join("Data", "barrier.png")), (80, 80))
    
    num_barriers = len(barrier_spawn_loc)
    barrier_group = SpritePool(cls=Barrier, size = num_barriers, spawn_strategy=barrier_spawn_strat, image = barrier_img)
    for _ in range(num_barriers):
        barrier_group.spawn()

    del player_img, player_speed, num_barriers


    bullet_cooldown = 250
    last_shot_time = 0
    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        if keys[pygame.K_SPACE] and current_time - last_shot_time > bullet_cooldown:
            bullet_group.spawn(player)
            last_shot_time = current_time

        for invader in invader_group:
            if not invader.active:
                invader_group.spawn(invader_group.get_all_active_sprites())
        
        bullet_group.check_collision(invader_group)
        barrier_group.check_collision(invader_group)

        invader_group.update(dt, 1080)
        player.update(dt, keys, 1920)
        bullet_group.update(dt)
        barrier_group.update()

        screen.fill("black")
        invader_group.draw(screen)
        screen.blit(player.image, player.rect)
        barrier_group.draw(screen)
        bullet_group.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()

    #need to finish configs.json and create configs.py otherwise barrier working, invader working, bullet working, pierce works better as a flag not as health
    #can' think of much else, tbh, other than if an invader hits the end of the screen you get game over, maybe track kills
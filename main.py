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



def open_configs():
    try:
        with open("configs.json") as f:
            return json.load(f)
    except FileNotFoundError:
        print ("File not found, closing program")
        sys.exit()

#ADD TO CONFIGS, ALSO CREATE A CONFIG.PY WHICH HAS ALL THESE VALUES LOADED TO MAKE MAIN READABLE
bullet_cooldown = 250
last_shot_time = 0


def main():
    pygame.init()
    clock = pygame.time.Clock()
    config = open_configs()
    screen_width, screen_height = config["screen"]["screen_width"], config["screen"]["screen_height"]
    screen = pygame.display.set_mode((screen_width, screen_height))

    player_img = pygame.transform.scale(pygame.image.load(os.path.join("Data", config["player"]["player_image"])), (80,80))
    player_speed = config["player"]["player_speed"]
    player_start_pos = config["player"]["player_start_pos"]

    player = Player(player_start_pos, player_img, player_speed)

    invader_img = pygame.transform.scale(pygame.image.load(os.path.join("Data", "invader.png")), (80,80))

    invader_group = SpritePool(cls=Invader, size = 12, spawn_strategy=InvaderSpawnManager(), image=invader_img, speed=150)
    for _ in range(len(invader_group)):
        invader_group.spawn(invader_group.get_all_active_sprites())

    bullet_img = pygame.transform.scale(pygame.image.load(os.path.join("Data", "bullet.png")), (30,30))
    bullet_group = SpritePool(cls=Bullet, size=10, spawn_strategy=bullet_spawn_strat ,image=bullet_img, speed=600)

    barrier_img = pygame.transform.scale(pygame.image.load(os.path.join("Data", "barrier.png")), (80, 80))
    
    num_barriers = len(barrier_spawn_loc)
    barrier_group = SpritePool(cls=Barrier, size = num_barriers, spawn_strategy=barrier_spawn_strat, image = barrier_img)
    for _ in range(num_barriers):
        barrier_group.spawn()

    del player_img, player_speed, player_start_pos, num_barriers


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

        invader_group.update(dt, screen_height)
        player.update(dt, keys, screen_width)
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
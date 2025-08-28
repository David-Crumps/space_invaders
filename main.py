import pygame
import os
from player import Player
from invader import Invader
from sprite_pool import SpritePool
from InvaderSpawnManager import InvaderSpawnManager
from bullet import *
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

    invader_group = SpritePool(cls=Invader, size = 10, spawn_strategy=InvaderSpawnManager(), image=invader_img, speed=150)
    for _ in range(10):
        invader_group.spawn()

    bullet_img = pygame.transform.scale(pygame.image.load(os.path.join("Data", "bullet.png")), (30,30))
    bullet_group = SpritePool(cls=Bullet, size=10, spawn_strategy=bullet_spawn_strat ,image=bullet_img, speed=600)

    del player_img, player_speed, player_start_pos


    bullet_cooldown = 250
    last_shot_time = 0

    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        keys = pygame.key.get_pressed()
        for invader in invader_group:
            if not invader.active:
                invader_group.spawn()

        invader_group.update(dt, screen_height)

        screen.fill("black")
        invader_group.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
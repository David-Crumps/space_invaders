import pygame
import os
from player import Player
from invader import Invader
from sprite_pool import SpritePool
from InvaderSpawnManager import InvaderSpawnManager
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

    width, height = config["screen_size"][0], config["screen_size"][1]
    screen = pygame.display.set_mode((width, height))

    player_img = pygame.transform.scale(pygame.image.load(os.path.join("Data", config["player"]["player_image"])), (80,80))
    player_speed = config["player"]["player_speed"]
    player_start_pos = config["player"]["player_start_pos"]

    player = Player(player_start_pos, player_img, player_speed)

    invader_img = pygame.transform.scale(pygame.image.load(os.path.join("Data", "invader.png")), (80,80))

    invader_group = SpritePool(cls=Invader, size = 12, spawn_strategy=InvaderSpawnManager(), image=invader_img, speed=100)
    invader_group.spawn_all()   

    del player_img, player_speed, player_start_pos
    while True:
        dt = clock.tick(60) / 1000 #Delta time

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        keys = pygame.key.get_pressed() 
        player.update(dt, keys, width)
        invader_group.update(dt, height)
        
        screen.fill('black')
        screen.blit(player.image, player.rect)
        invader_group.draw(screen)
        
        
        pygame.display.flip()


         

    


if __name__ == "__main__":
    main()
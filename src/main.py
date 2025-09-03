import pygame
import os
from player import Player
from invader import Invader
from sprite_pool import SpritePool
from InvaderSpawnManager import InvaderSpawnManager
from bullet import Bullet
from utils import bullet_spawn_strat, barrier_spawn_strat, BARRIER_SPAWN_LOC
import game_flags
from barrier import Barrier
import sys
from configs import *

#REMOVE ALL HARDCODED VALUES AND REPLACE WITH CONFIGS VALUES, AND THATS ABOUT IT.
bullet_cooldown = 250
last_shot_time = 0

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.join(BASE_DIR, '..')
DATA = os.path.join(PROJECT_ROOT, 'Data')

def main():
    pygame.init()
    clock = pygame.time.Clock()

    screen_img = pygame.transform.scale(pygame.image.load(os.path.join(DATA, SCREEN_IMAGE)), (SCREEN_WIDTH, SCREEN_HEIGHT))

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Space Invaders')

    player_img = pygame.transform.scale(pygame.image.load(os.path.join(DATA, PLAYER_IMAGE)), PLAYER_SIZE)
    player = Player(PLAYER_START_POS, player_img, PLAYER_SPEED)

    invader_imgs = [pygame.transform.scale(pygame.image.load(os.path.join("Data", img)), INVADER_SIZE) for img in INVADER_IMAGES]
    invader_group = SpritePool(cls=Invader, size = INVADER_SPAWN_LIMIT, spawn_strategy=InvaderSpawnManager(), images=invader_imgs, speed=INVADER_SPEED)
    for _ in range(len(invader_group)):
        invader_group.spawn(invader_group.get_all_active_sprites())

    bullet_img = pygame.transform.scale(pygame.image.load(os.path.join(DATA, BULLET_IMAGE)), BULLET_SIZE)
    bullet_group = SpritePool(cls=Bullet, size=BULLET_MAGAZINE_SIZE, spawn_strategy=bullet_spawn_strat ,image=bullet_img, speed=BULLET_SPEED)

    barrier_img = pygame.transform.scale(pygame.image.load(os.path.join(DATA, BARRIER_IMAGE)), BARRIER_SIZE)
    
    num_barriers = len(BARRIER_SPAWN_LOC)
    barrier_group = SpritePool(cls=Barrier, size = num_barriers, spawn_strategy=barrier_spawn_strat, image = barrier_img)
    for _ in range(num_barriers):
        barrier_group.spawn()

    del num_barriers

    last_shot_time = 0
    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        #GAME OVER SCREEN
        if game_flags.GAME_OVER:
            game_over_font = pygame.font.Font(None, 128)

            game_over_text = game_over_font.render("GAME OVER", True, "red")
            click_text = game_over_font.render("CLICK ANYWHERE ON SCREEN TO EXIT", True, "red")

            game_over_text_rect = game_over_text.get_rect()
            click_text_rect = click_text.get_rect()

            game_over_text_rect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
            click_text_rect.midtop = (game_over_text_rect.midbottom)
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or pygame.MOUSEBUTTONDOWN:
                        pygame.quit()
                        sys.exit()

                screen.fill("black")
                screen.blit(game_over_text, game_over_text_rect)
                screen.blit(click_text, click_text_rect)
                pygame.display.flip()


        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        if keys[pygame.K_SPACE] and current_time - last_shot_time > BULLET_COOLDOWN:
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

        screen.blit(screen_img, (0,0))
        invader_group.draw(screen)
        screen.blit(player.image, player.rect)
        barrier_group.draw(screen)
        bullet_group.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()

import pygame
import os
from player import Player
import sys

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'Data')

player_img = pygame.transform.scale(pygame.image.load(os.path.join(data_dir, 'player.png')), (80,80))
player_speed = 450
player_start_pos = x_pos, y_pos = 960, 1030

def main():
    pygame.init()
    clock = pygame.time.Clock()

    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)

    player = Player(x_pos, y_pos, player_img, player_speed)

    while True:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        keys = pygame.key.get_pressed() 
        player.update(dt, keys, width)

        screen.fill('black')
        screen.blit(player.image, player.rect)
        
        pygame.display.flip()


         

    


if __name__ == "__main__":
    main()
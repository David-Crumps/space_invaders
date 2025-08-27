import pygame
import os


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
speed = [0, 1]
playerSpeed = [4, 0]

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'Data')

invader = pygame.transform.scale(pygame.image.load(os.path.join(data_dir, 'invader.png')), (80, 80))
invaderPos = invader.get_rect(center=(100, 360))

player = pygame.transform.scale(pygame.image.load(os.path.join(data_dir, 'player.png')), (80,80))
playerPos = player.get_rect(center=(640, 670))



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    invaderPos = invaderPos.move(speed)


    screen.fill('black')
    screen.blit(invader, invaderPos)
    screen.blit(player, playerPos)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


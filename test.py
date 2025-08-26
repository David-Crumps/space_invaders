import pygame
import os

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'Data')

invader = pygame.transform.scale(pygame.image.load(os.path.join(data_dir, 'invader.png')), (80, 80))
invaderRect = invader.get_rect(center=(400, 400))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill('black')
    screen.blit(invader, invaderRect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
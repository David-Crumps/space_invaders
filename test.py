import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

invader = pygame.transform.scale(pygame.image.load('invader_5.png'), (80, 80))
invader2 = pygame.transform.scale(pygame.image.load('invader_2.png'), (80, 80))
invader3 = pygame.transform.scale(pygame.image.load('invader_3.png'), (80, 80))
invaderRect = invader.get_rect(center=(400, 400))
invaderRect2 = invader.get_rect(center=(500, 100))
invaderRect3 = invader.get_rect(center=(640, 360))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill('black')
    screen.blit(invader, invaderRect)
    screen.blit(invader2, invaderRect2)
    screen.blit(invader3, invaderRect3)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
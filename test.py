import pygame
import os


pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
invader_speed = 80
player_speed = 450
bullet_speed = 600

dt = 0

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'Data')

invader = pygame.transform.scale(pygame.image.load(os.path.join(data_dir, 'invader.png')), (80, 80))
invaderPos = invader.get_rect(center=(100, 360))

player = pygame.transform.scale(pygame.image.load(os.path.join(data_dir, 'player.png')), (80,80))
playerPos = player.get_rect(center=(640, 670))


bullets = []

bullet_img = pygame.transform.scale(pygame.image.load(os.path.join(data_dir, 'bullet.png')), (30,30))

bullet_cooldown = 250 #milliseconds
last_shot_time = 0



while running:
    dt = clock.tick(60)/ 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  
    #Limit bullets shot:
    current_time = pygame.time.get_ticks()
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_SPACE] and current_time - last_shot_time > bullet_cooldown:
        bullet_rect = bullet_img.get_rect()
        bullet_rect.midbottom = playerPos.midtop
        bullets.append((bullet_img, bullet_rect))
        last_shot_time = current_time



    player_x = 0    #moving left and right
    if keys[pygame.K_LEFT]:
        player_x = -player_speed
    if keys[pygame.K_RIGHT]:
        player_x = player_speed
    playerPos = playerPos.move(player_x*dt, 0)

    if playerPos.left < 0: #checking collision with screen
        playerPos.left = 0
    if playerPos.right > width:
        playerPos.right = width



    invaderPos = invaderPos.move(0, invader_speed*dt)

    screen.fill('black')
    screen.blit(invader, invaderPos)
    screen.blit(player, playerPos)

    for bullet_img, bullet_rect in bullets:
        bullet_rect.move_ip(0, -bullet_speed * dt)
        screen.blit(bullet_img, bullet_rect)

    pygame.display.flip()

pygame.quit()


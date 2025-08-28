import pygame

def collision_detection(sprite, group):
    collisions = pygame.sprite.spritecollide(sprite, group, False) #returns a list of sprites in group that are colliding with sprite
    if collisions:
        sprite.active = False
        for collide in collisions:
            collide.active = False

def bullet_spawn_strat(bullet, player):
    bullet.rect.midbottom = player.rect.midtop

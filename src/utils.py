import pygame
from invader import Invader
from configs import LANES_WIDTH, LANES_BOTTOM_Y_POS, LANES_LAST_X_POS, LANES_START_X_POS


BARRIER_SPAWN_LOC = [(x,LANES_BOTTOM_Y_POS) for x in range(LANES_START_X_POS, LANES_LAST_X_POS, LANES_WIDTH)]


def collision_detection(sprite, group):
    collisions = pygame.sprite.spritecollide(sprite, group, False) #returns a list of the sprite conatined in the group that are colliding with sprite
    if collisions:
        sprite.collision(damage_taken = Invader.damage)
        for collide in collisions:
            if collide.active == True:
                collide.collision(damage_taken = sprite.damage)


def bullet_spawn_strat(bullet, player):
    bullet.rect.midbottom = player.rect.midtop
    spawnedBullet = True
    return spawnedBullet


def barrier_spawn_strat(barrier):
    barrier.rect.center = BARRIER_SPAWN_LOC[-1]
    spawned_barrier = True
    BARRIER_SPAWN_LOC.pop()
    return spawned_barrier
    


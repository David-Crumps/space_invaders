import pygame
from invader import Invader

#move to configs
slot_width=95 
x_min=50
x_max = 1870
y = 950
barrier_spawn_loc = [(x,y) for x in range(x_min, x_max, slot_width)]

#when the sprite is invader and the group is bullet/barrier it creates a number of anomalies
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
    barrier.rect.center = barrier_spawn_loc[-1]
    spawned_barrier = True
    barrier_spawn_loc.pop()
    return spawned_barrier
    


import pygame

slot_width=95 
x_min=50
x_max = 1870
y = 950
barrier_spawn_loc = [(x,y) for x in range(x_min, x_max, slot_width)]

def collision_detection(sprite, group):
    collisions = pygame.sprite.spritecollide(sprite, group, False) #returns a list of the sprite conatined in the group that are colliding with sprite
    if collisions:
        print(group)
        for collide in collisions:
            collide.collision()
            print("Collision occured!")
#might need to make different collision functions for invader to bullet, and invader to barrier, if an invader hits a barrier it dies and the barrier loses one hp
#KEEP THIS FUNCTION, ADD IN COLLIDED FUNCTIONS FOR ALL SPRITE CLASSES, THEN IF THERE IS A COLLISION CALL THE COLLIDE FUNCTION FOR THE SPRITE AND THEN FOR EACH MEMEBER OF THE GROUP WHERE IT CAN UPDATE ITSELF ACCORDINGLY
#HAVE BARRIER AND BULLET, PASS A DAMAGE STAT, THAT IS THE DAMAGE OF A BARRIER IS EQUAL TO THE HP OF AN INVADER WHICH WILL THEN DISABLE IT ON THE UPDATE CALLS.
#CAN HAVE EACH MEMBER OF THE GROUP THAT IS COLLIDING WITH THE SPRITE PASS ITS DAMAGE TO THE SPRITE, AND THEN THE SPRITE PASSES IT'S DAMAGE TO EACH MEMBER (SENDING DAMAGE TO A BULLET WOULD BE POINTLESS (UNLESS WE ADD IN PIERCING SHOTS????))
#Anything other than invader, would just decrease health by one..., except bullet technically but if we give bullet piercing it would work perhaps

def bullet_spawn_strat(bullet, player):
    bullet.rect.midbottom = player.rect.midtop
    bullet.health = 1
    spawnedBullet = True
    return spawnedBullet

def barrier_spawn_strat(barrier):
    barrier.rect.center = barrier_spawn_loc[-1]
    spawned_barrier = True
    barrier_spawn_loc.pop()
    return spawned_barrier
    


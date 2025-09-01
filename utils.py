import pygame

def collision_detection(sprite, group):
    collisions = pygame.sprite.spritecollide(sprite, group, False) #returns a list of the sprite conatined in the group that are colliding with sprite
    if collisions:
        sprite.active = False
        for collide in collisions:
            collide.active = False
#might need to make different collision functions for invader to bullet, and invader to barrier, if an invader hits a barrier it dies and the barrier loses one hp
#KEEP THIS FUNCTION, ADD IN COLLIDED FUNCTIONS FOR ALL SPRITE CLASSES, THEN IF THERE IS A COLLISION CALL THE COLLIDE FUNCTION FOR THE SPRITE AND THEN FOR EACH MEMEBER OF THE GROUP WHERE IT CAN UPDATE ITSELF ACCORDINGLY
#HAVE BARRIER AND BULLET, PASS A DAMAGE STAT, THAT IS THE DAMAGE OF A BARRIER IS EQUAL TO THE HP OF AN INVADER WHICH WILL THEN DISABLE IT ON THE UPDATE CALLS.
#CAN HAVE EACH MEMBER OF THE GROUP THAT IS COLLIDING WITH THE SPRITE PASS ITS DAMAGE TO THE SPRITE, AND THEN THE SPRITE PASSES IT'S DAMAGE TO EACH MEMBER (SENDING DAMAGE TO A BULLET WOULD BE POINTLESS (UNLESS WE ADD IN PIERCING SHOTS????))

def bullet_spawn_strat(bullet, player):
    bullet.rect.midbottom = player.rect.midtop
    spawnedBullet = True
    return spawnedBullet

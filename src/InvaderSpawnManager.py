import random
from configs import LANES_WIDTH, LANES_START_X_POS, LANES_LAST_X_POS, LANES_TOP_Y_POS

class InvaderSpawnManager:
    def __init__(self):
        self.spawn_loc = [(x,LANES_TOP_Y_POS) for x in range (LANES_START_X_POS, LANES_LAST_X_POS, LANES_WIDTH)]
        random.shuffle(self.spawn_loc)
    
    def __call__(self, sprite, activeSprites):
        spawnedInvader = False
        if activeSprites:
            for x,y in self.spawn_loc:
                collision = False
                for activeSprite in activeSprites:
                    if activeSprite.rect.collidepoint(x,y):
                        collision = True
                        break
                if not collision:
                    sprite.rect.center = (x,y)
                    sprite.health = 2
                    spawnedInvader = True
                    break
        else:
            sprite.rect.center = self.spawn_loc[0] #If there are no active sprites, add a sprite at the first spawn location
            sprite.health = 2
            spawnedInvader = True
        random.shuffle(self.spawn_loc)
        return spawnedInvader

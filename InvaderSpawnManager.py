import pygame
import random


class InvaderSpawnManager:
    def __init__(self, slot_width=95, x_min=50, x_max = 1870, y = 50):
        self.spawn_loc = [(x,y) for x in range (x_min, x_max, slot_width)]
        random.shuffle(self.spawn_loc)
    
    def __call__(self, sprite, activeSprites):
        if activeSprites:
            for x,y in self.spawn_loc:
                collision = False
                for activeSprite in activeSprites:
                    if activeSprite.rect.collidepoint(x,y):
                        collision = True
                        break
                if not collision:
                    sprite.rect.center = (x,y)
                    break
        else:
            sprite.rect.center = self.spawn_loc[0]
        random.shuffle(self.spawn_loc)

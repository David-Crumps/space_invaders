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



"""
class InvaderSpawnManager:
    def __init__ (self, slot_width = 95, x_min=50, x_max=1870, y=50):
        self.x_min = x_min
        self.x_max = x_max
        self.y = y
        self.slot_width = slot_width

        self.slots = [(x,y) for x in range(x_min, x_max, slot_width)]
        self.shuffle()

    def __call__(self, sprite, activeSprites):
        if self.slots:
            x,y = self.slots.pop()
            sprite.rect.center = (x,y)
        else:
            sprite.active = False

    def shuffle(self):
        random.shuffle(self.slots)
    
    def reset_slots(self):
        self.slots = [(x,self.y) for x in range(self.x_min, self.x_max, self.slot_width)]
        self.shuffle()
    
    def is_slot_clear(self, sprite):
        print("Help")
"""

#We want to check if the current slot is clear, that is check, .collidepoint(x,y) determines if the points x and y are inside a rect object, use this, determine if any invaders are inside a point if true, do NOT spawn there, otherwise spawn
#want the spawning to be at random locations so, rather than pop slots, everytime we look to add a value to one of the slots, randomise the slots, that is shuffle, it not move to next slot etc.
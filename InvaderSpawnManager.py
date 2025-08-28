import pygame
import random

class InvaderSpawnManager:
    def __init__ (self, slot_width = 95, x_min=50, x_max=1870, y=50):
        self.slots = [(x,y) for x in range(x_min, x_max, slot_width)]

    def __call__(self, sprite):
        if self.slots:
            x,y = self.slots.pop(0)
            sprite.rect.center = (x,y)
            self.slots.append((x,y))
        else:
            sprite.active = False

    def shuffle(self):
        random.shuffle(self.slots)
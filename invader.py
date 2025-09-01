import pygame
import os
import random
from typing import cast
from bullet import Bullet


class Invader(pygame.sprite.Sprite):
    def __init__(self, image, speed):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()

        self.speed = speed
        self.active = False

        self.health = 0
    
    def update(self, dt, height):
        if self.rect.bottom > height or self.health <= 0:
            self.active = False
        else:
            self.rect = self.rect.move(0, self.speed * dt)
    
    def collision(self):
        print(f"Prior to collision: {self.health}")
        self.health -= 1
        print(f"After collision: {self.health}")





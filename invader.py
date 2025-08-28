import pygame
import os
import random

class Invader(pygame.sprite.Sprite):
    def __init__(self, image, speed):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()

        self.speed = speed
        self.active = True
        self.health = 1
    
    def update(self, dt, height):
        self.rect = self.rect.move(0, self.speed * dt)

        if self.rect.bottom > height:
            self.active = False

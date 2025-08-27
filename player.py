import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image, speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x,y))
        self.speed = speed
    
    def update(self, dt, keys, width):
        movement = 0
        if (keys[pygame.K_LEFT]):
            movement = -self.speed
        if (keys[pygame.K_RIGHT]):
            movement = self.speed
        self.rect = self.rect.move(movement*dt, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width

        

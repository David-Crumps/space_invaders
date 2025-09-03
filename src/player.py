import pygame
import os
from configs import SCREEN_LEFT, SCREEN_RIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self, start_cords, image, speed):
        super().__init__()
        self.image = image

        x = start_cords[0]
        y = start_cords[1]

        self.rect = self.image.get_rect(center=(x,y))
        self.speed = speed
    
    def update(self, dt, keys):
        movement = 0
        if (keys[pygame.K_LEFT]):
            movement = -self.speed
        if (keys[pygame.K_RIGHT]):
            movement = self.speed
        self.rect = self.rect.move(movement*dt, 0)

        if self.rect.left < SCREEN_LEFT:
            self.rect.left = SCREEN_LEFT
        if self.rect.right > SCREEN_RIGHT:
            self.rect.right = SCREEN_RIGHT

        

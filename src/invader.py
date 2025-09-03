import pygame
import random
import game_flags

class Invader(pygame.sprite.Sprite):
    damage = 1
    def __init__(self, images, speed):
        super().__init__()

        self.image = random.choice(images)
        self.rect = self.image.get_rect()

        self.speed = speed
        self.active = False

        self.health = 0

    #if hitting bottom of screen activate flag that ends game.
    def update(self, dt, height):
        if self.health <= 0:
            self.active = False
        else:
            self.rect = self.rect.move(0, self.speed * dt)

        if self.rect.bottom > height:
           game_flags.GAME_OVER = True
    
    def collision(self, **kwargs):
        damage_taken = kwargs.get('damage_taken', 0)
        self.health -= damage_taken





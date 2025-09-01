import pygame

class Barrier(pygame.sprite.Sprite):
    damage = 50
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.active = False
        self.rect = self.image.get_rect()
        self.health = 2
        

    def update(self):
        if self.health <= 0:
            self.active = False
    
    def collision(self, **kwargs):
        self.health -= 1

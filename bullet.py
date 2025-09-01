import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, speed):
        super().__init__()
        self.image = image
        self.rect = image.get_rect()
        self.speed = speed
        self.damage = 1

        self.active = False
    
    def update(self, dt):
        self.rect.move_ip(0, -self.speed*dt)
  
        if self.rect.top < 0:
            self.active = False
    
    def collision(self, **kwargs):
        self.active = False
        

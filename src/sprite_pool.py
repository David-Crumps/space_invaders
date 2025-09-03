import pygame
from utils import collision_detection



class SpritePool(pygame.sprite.Group):
    def __init__(self, cls, size, spawn_strategy = None, *args, **kwargs):
        super().__init__()
        self.cls = cls
        self.spawn_strategy = spawn_strategy

        for _ in range(size):
            self.add(self.cls(*args, **kwargs))

    def get_inactive_sprite(self):
        for sprite in self.sprites():
            if not sprite.active:
                return sprite
    
    def get_all_active_sprites(self):
        return [sprite for sprite in self.sprites() if sprite.active]
    
    def spawn(self, *args, **kwargs):
        sprite = self.get_inactive_sprite()
        if sprite:
            if self.spawn_strategy:
                    spawned = self.spawn_strategy(sprite, *args, **kwargs)
                    if spawned:
                        sprite.active = True
            return sprite
        return None
    def set_all_inactive(self):
        for sprite in self.sprites():
            if sprite.active:
                sprite.active = False

    def check_collision(self, group):
        for sprite in self.sprites():
            if sprite.active:
                collision_detection(sprite, group)
 
    def update(self, *args, **kwargs):
        for sprite in self.sprites():
            if sprite.active:
                sprite.update(*args, **kwargs)
    
    def draw(self, surface, *args, **kwargs):
        for sprite in self.sprites():
            if sprite.active:
                surface.blit(sprite.image, sprite.rect)
        return self.sprites()

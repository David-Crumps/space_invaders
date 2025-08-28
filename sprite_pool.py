import pygame
import os
from InvaderSpawnManager import InvaderSpawnManager

class SpritePool(pygame.sprite.Group):
    def __init__(self, cls, size, spawn_strategy = None, *args, **kwargs):
        super().__init__()
        self.cls = cls
        self.args = args
        self.kwargs = kwargs
        self.spawn_strategy = spawn_strategy
        self.pool = [self._create_sprite() for _ in range(size)]

        for sprite in self.pool:
            self.add(sprite)

    def _create_sprite(self):
        sprite = self.cls(*self.args, **self.kwargs)
        sprite.active = False
        return sprite

    def spawn_one(self):
        for sprite in self.pool:
            if not sprite.active:
                if self.spawn_strategy:
                    self.spawn_strategy.shuffle()
                    self.spawn_strategy(sprite)
                sprite.active = True
                return sprite
        return None
    
    def spawn_all(self):
        spawned = []
        if self.spawn_strategy:
            self.spawn_strategy.shuffle()
            for sprite in self.pool:
                if not sprite.active:
                    self.spawn_strategy(sprite)
                sprite.active = True
                spawned.append(sprite)
        return spawned



    def get(self):
        for sprite in self.pool:
            if not sprite.active:
                sprite.active = True
                return sprite
        return None

    def update(self, *args, **kwargs):
        for sprite in self.sprites():
            if sprite.active:
                sprite.update(*args, **kwargs)
    

    def draw(self, surface, *args, **kwargs):
        for sprite in self.sprites():
            if sprite.active:
                surface.blit(sprite.image, sprite.rect)
        return self.sprites()


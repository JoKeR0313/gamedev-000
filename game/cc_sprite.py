import pygame


class ccSprite:

    def __init__(self, texture, rectangle, hitbox):
        self.rectangle = rectangle
        self.texture = texture
        if hitbox is None:
            self.hitbox = rectangle
        else:
            self.hitbox = hitbox

    def draw(self, renderer, x, y):
        renderer.blit(self.texture.image, (x, y), self.rectangle)

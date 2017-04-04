import pygame


class ccSprite:

    def __init__(self, texture, rectangle):
        self.rectangle = rectangle
        self.texture = texture

    def draw(self, renderer, x, y):
        print(self.texture.image)
        renderer.blit(self.texture.image, (x, y), self.rectangle)


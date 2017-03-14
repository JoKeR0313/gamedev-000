import pygame


class ccSprite:

    def __init__(self, texture, rectangle):
        self.rectangle = rectangle
        self.texture = texture

    def load(self, sprites_reader):
        all_sprites = pygame.sprite.Group()
        all_sprites.add(self.rectangle)

    def draw(self, renderer, x, y):
        renderer.blit(self.texture.image, (x, y), self.rectangle)


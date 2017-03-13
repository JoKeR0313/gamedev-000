import pygame

class ccSprite:

    def __init__(self, texture, rectangle):
        # needs an instance variable what stores the width, height and x,y offset.
        # Probably a pygame.Rect type. Store the texture parameter also in an
        # instance variable
        self.rectangle = rectangle#[width, height, x, y]
        self.texture = texture

        

    def load(self, sprites_reader):
        all_sprites = pygame.sprite.Group()
        all_sprites.add(rectangle)

    def draw(self, renderer, x, y):
        # draw the sprite to screen with pygame. Draw only the sprite from the texture to x,y position
        r = pygame.Rect(self.rectangle[2], self.rectangle[3], 
                        self.rectangle[0], self.rectangle[1])
        renderer.blit(self.texture.image, (x, y), r)


import pygame
from pygame.locals import *


class Block(pygame.sprite.Sprite):
    def __init__(self, colour=(100, 100, 255), width=64, height=64):
        super(Block, self).__init__()

        # Surface - python object for representing images
        # we can blit surfaces onto each others
        self.image = pygame.Surface((width, height))
        self.image.fill(colour)

        # rect - rectangle object (necessary!! a lot of attributes, methods for this)
        # making a rectangle on the image
        self.rect = self.image.get_rect()

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

class InBlock(pygame.sprite.Sprite):
    def __init__(self, colour=(0, 0, 0), width=30, height=30):
        super(InBlock, self).__init__()

        # Surface - python object for representing images
        # we can blit surfaces onto each others
        self.image = pygame.Surface((width, height))
        self.image.fill(colour)

        # rect - rectangle object (necessary!! a lot of attributes, methods for this)
        # making a rectangle on the image
        self.rect = self.image.get_rect()

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y


def main():
    pygame.init()

    screen_size = screen_width, screen_height = 640, 480
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()

    screen.fill((255, 255, 255))

    block_group = pygame.sprite.LayeredUpdates()
    a_block = Block()
    a_block.set_position(screen_width/2, screen_height/2)
    b_block = Block(colour=(255, 160, 122))
    b_block.set_position(100, 100)

    behind_b = InBlock()
    behind_b.set_position(90, 90)

    in_front_of_a = InBlock()
    in_front_of_a.set_position(a_block.rect.x, a_block.rect.y)

    block_group.add(b_block, layer=2)
    block_group.add(behind_b, layer=1)

    block_group.add(a_block, layer=2)
    block_group.add(in_front_of_a, layer=3)

    running = True
    while running:
        clock.tick(60)

        block_group.draw(screen)

        for event in pygame.event.get():
            print(event)
            if event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                a_block_layer = block_group.get_layer_of_sprite(in_front_of_a)
                block_group.change_layer(in_front_of_a, a_block_layer * -1)

            pygame.display.update()

    pygame.quit()

main()
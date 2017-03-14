import sys
import pygame
from cc_object import ccObject
from pygame.locals import *

pygame.init()


class ccBasicObject(ccObject):

    def __init__(self):
        # # call the ancestor's __init__()
        super().__init__()
        self.type = "ccBasicObject"  # probably should use python's type(), so set that up with magic method(?)
        self.position = pygame.math.Vector2(0, 0)  # use Vector2. It should be able to store float values
        self.velocity = pygame.math.Vector2(0, 0)

    def load(self, obj_file_loader):
        # call ancestor's load() method and get the sprite from SpriteManager. If
        # sprite is not found, print error and set active_sprite to None
        super().load(obj_file_loader)
        # later: set position and velocity from test.objects.json

    def draw(self, renderer):
        # draw the active_sprite to the screen, to self.position position
        self.active_sprite.draw(renderer, self.position.x, self.position.y)

    def step(self, time_passed):
        # change Object's position with velocity. Specialized object classes will
        # override this method and do other logic here also
        current_speed = self.velocity
        current_speed.x = self.velocity.x * time_passed
        current_speed.y = self.velocity.y * time_passed
        self.position.x += current_speed.x
        self.position.y += current_speed.y

    def __repr__(self):
        return self.type

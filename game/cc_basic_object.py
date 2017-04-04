import sys
import pygame
from cc_object import ccObject
from pygame.locals import *
from cc_sprite_manager import ccSpriteManager
from copy import deepcopy

pygame.init()


class ccBasicObject(ccObject):

    def __init__(self):
        # # call the ancestor's __init__()
        super().__init__()
        self.type = "ccBasicObject"  # probably should use python's type(), so set that up with magic method(?)
        self.position = pygame.math.Vector2(0, 0)  # use Vector2. It should be able to store float values
        self.velocity = pygame.math.Vector2(0, 0)

    def load(self, obj_section):
        # call ancestor's load() method and get the sprite from SpriteManager. If
        # sprite is not found, print error and set active_sprite to None
        super().load(obj_section)
        if "position_x" in obj_section:
            self.position.x = obj_section["position_x"]
        if "position_y" in obj_section:
            self.position.y = obj_section["position_y"]
        if "velocity_x" in obj_section:
            self.velocity.x = obj_section["velocity_x"]
        if "velocity_y" in obj_section:
            self.velocity.y = obj_section["velocity_y"]
        if "sprite" in obj_section:
            self.active_sprite = ccSpriteManager.get_sprite(obj_section['sprite'])
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

    def copy(self):
        new_object = ccBasicObject()
        self.__fill(new_object)
        return new_object

    def __fill(self, source):
        source.position = deepcopy(self.position)
        source.velocity = deepcopy(self.velocity)
        source.active_sprite = self.active_sprite
        source.type = self.type
        source.id = deepcopy(self.id)
        source.object_props = deepcopy(self.object_props)

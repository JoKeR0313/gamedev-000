import sys
import pygame
from GameData.cc_object import ccObject
from pygame.locals import *
from GameData.cc_sprite_manager import ccSpriteManager
from copy import deepcopy

pygame.init()


class ccBasicObject(ccObject):

    def __init__(self):
        # # call the ancestor's __init__()
        super().__init__()
        self.type = "ccBasicObject"  # probably should use python's type(), so set that up with magic method(?)
        self.position = pygame.math.Vector2(0, 0)  # use Vector2. It should be able to store float values
        self.velocity = pygame.math.Vector2(0, 0)
        self.hitbox = None

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
            self.set_hitbox()

        # later: set position and velocity from test.objects.json

    def draw(self, renderer):
        # draw the active_sprite to the screen, to self.position position
        self.active_sprite.draw(renderer, self.position.x, self.position.y)
        # DRAWING A BIGASS RED RECTANGLE AROUND EVERYTHING
        if self.hitbox != None:
            #rect = pygame.Rect(self.hitbox)
            #rect.x = self.position.x
            #rect.y = self.position.y
            #pygame.draw.rect(renderer, (255, 0, 0), rect, 1)
            pygame.draw.rect(renderer, (255, 0, 0), self.hitbox, 1)

    def step(self, time_passed):
        # change Object's position with velocity. Specialized object classes will
        # override this method and do other logic here also
        current_speed = pygame.math.Vector2(0, 0)
        current_speed.x = self.velocity.x * time_passed
        current_speed.y = self.velocity.y * time_passed
        self.position.x += current_speed.x
        self.position.y += current_speed.y
        self.actualize_hitbox_position()

    def copy(self):
        new_object = ccBasicObject()
        self.fill(new_object)
        return new_object

    def fill(self, target):
        target.position = pygame.math.Vector2(self.position)
        target.velocity = pygame.math.Vector2(self.velocity)
        target.active_sprite = self.active_sprite
        target.type = self.type
        target.id = deepcopy(self.id)
        if self.hitbox != None:
            target.hitbox = pygame.Rect(self.hitbox.x, self.hitbox.y,
                                        self.hitbox.width, self.hitbox.height)
        else:
            target.hitbox = None
        target.object_props = deepcopy(self.object_props)

    def set_hitbox(self):
        if self.active_sprite.hitbox != None:
            self.hitbox = pygame.Rect(self.position.x + self.active_sprite.hitbox.x,
                                      self.position.y + self.active_sprite.hitbox.y,
                                      self.active_sprite.hitbox.width, 
                                      self.active_sprite.hitbox.height)

    def objecthit(self, other_obj):
        pass

    
    def actualize_hitbox_position(self):
        if self.hitbox is not None:
            self.hitbox.x = self.position.x + self.active_sprite.hitbox.x
            self.hitbox.y = self.position.y + self.active_sprite.hitbox.y


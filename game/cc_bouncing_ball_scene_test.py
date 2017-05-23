from cc_object_scene import ccObjectScene
from cc_globals import ccGlobals
import copy
import pygame


class ccBouncingBallScene(ccObjectScene):

    def __init__(self):
        super().__init__()
        self.type = "ccBouncingBallScene"

    def load(self, filename):
        super().load(filename)
        self.load_hitboxes()

    def step(self, time_passed):
        self.update_hitbox()
        self.hitbox_collision_check()
        for obj in self.object_list:
            obj.step(time_passed)
            if obj.position.x + obj.active_sprite.rectangle.width >= ccGlobals.size[0]:
                obj.velocity.x = -obj.velocity.x
            elif obj.position.x <= 0:
                obj.velocity.x = -obj.velocity.x
            elif obj.position.y + obj.active_sprite.rectangle.height >= ccGlobals.size[1]:
                obj.velocity.y = -obj.velocity.y
            elif obj.position.y <= 0:
                obj.velocity.y = -obj.velocity.y

    def load_hitboxes(self):
        for obj in self.object_list:
            obj.hitbox = pygame.Rect(obj.position.x, obj.position.y,
                                     obj.active_sprite.rectangle.width,
                                     obj.active_sprite.rectangle.height)

    def update_hitbox(self):
        for obj in self.object_list:
            if obj.hitbox is not None:
                obj.hitbox.x = obj.position.x
                obj.hitbox.y = obj.position.y

    def hitbox_collision_check(self):
        for obj in self.object_list:
            if obj.hitbox is not None:
                for check_obj in self.object_list:
                    if check_obj.hitbox is not None:
                        if obj != check_obj:
                            if obj.hitbox.colliderect(check_obj.hitbox):
                                obj.velocity.x = -obj.velocity.x
                                obj.velocity.y = -obj.velocity.y

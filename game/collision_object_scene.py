from cc_object_scene import ccObjectScene
from cc_globals import ccGlobals
import pygame
from pprint import pprint
import copy


class ccCollisionObjectScene(ccObjectScene):

    def __init__(self):
        super().__init__()
        self.type = "ccCollisionObjectScene"

    def step(self, time_passed):
        pressed = pygame.key.get_pressed()
        for obj in self.object_list:
            obj.step(time_passed)
            if obj.id == 200:
                player = obj
                if pressed[pygame.K_LEFT]:
                    player.position[0] -= 1
                    self.collision_check(player, "left")
                if pressed[pygame.K_RIGHT]:
                    player.position[0] += 1
                    self.collision_check(player, "right")
                if pressed[pygame.K_UP]:
                    player.position[1] -= 1
                    self.collision_check(player, "up")
                if pressed[pygame.K_DOWN]:
                    obj.position[1] += 1
                    self.collision_check(player, "down")

    def get_positions(self):
        for obj in self.object_list:
            obj.active_sprite.rectangle.y = obj.position.y
            obj.active_sprite.rectangle.x = obj.position.x

    def get_object_position(self, obj):
        obj.active_sprite.rectangle.y = obj.position.y
        obj.active_sprite.rectangle.x = obj.position.x

    def collision_check(self, player, direction):
        x = 0
        for obj in self.object_list:
            self.get_object_position(obj)
            if obj.id != 200:
                if player.active_sprite.rectangle.colliderect(obj.active_sprite.rectangle):
                    print(direction + ":\033[91mcollision true\033[0m")
                    print("-----------------------------------------")
                    print("player object and rectangle coordinates")
                    print("player position: ", player.position)
                    print("player rectangle: ", player.active_sprite.rectangle)
                    print("-----------------------------------------")
                    print("-----------------------------------------")
                    print(x, ". obstacle object and rectangle coordinates")
                    print("obstacle position: ", obj.position)
                    print("obstacle rectangle: ", obj.active_sprite.rectangle)
                    print("-----------------------------------------")
            x += 1

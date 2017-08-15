from GameData.cc_scene import ccScene
from GameData.cc_object_scene_file_loader import ccObjectSceneFileLoader
from GameData.cc_globals import ccGlobals
import pygame
import copy


class ccCollisionObjectScene(ccScene):

    def __init__(self):
        super().__init__()
        self.object_list = []
        self.rect_list = []
        self.player = None
        self.type = "ccCollisionObjectScene"

    def load(self, filename):
        loader = ccObjectSceneFileLoader()
        loader.process_file(filename)
        self.object_list = loader.get_objects()
        self.rect_list = self.get_rects()
        self.player = self.get_player()

    def draw(self):
        for obj in self.object_list:
            obj.draw(ccGlobals.get_renderer())

    def step(self, time_passed):
        pressed = pygame.key.get_pressed()
        for obj in self.object_list:
            obj.step(time_passed)
            if obj.id == 200:
                player = obj
                if pressed[pygame.K_LEFT]:
                    player.position[0] -= 1
                    self.update_player()
                    if self.collision_check():
                        player.position[0] += 1
                if pressed[pygame.K_RIGHT]:
                    player.position[0] += 1
                    self.update_player()
                    if self.collision_check():
                        player.position[0] -= 1
                if pressed[pygame.K_UP]:
                    player.position[1] -= 1
                    self.update_player()
                    if self.collision_check():
                        player.position[1] += 1
                if pressed[pygame.K_DOWN]:
                    obj.position[1] += 1
                    self.update_player()
                    if self.collision_check():
                        player.position[1] -= 1

    def get_rects(self):
        rects = []
        for obj in self.object_list:
            if obj.id != 200:
                rect = copy.deepcopy(obj.active_sprite.rectangle)
                rect.x = obj.position.x
                rect.y = obj.position.y
                rects.append(rect)
        return rects

    def get_player(self):
        for obj in self.object_list:
            if obj.id == 200:
                player = copy.deepcopy(obj.active_sprite.rectangle)
                player.x = obj.position.x
                player.y = obj.position.y
                return player

    def update_player(self):
        for obj in self.object_list:
            if obj.id == 200:
                self.player.x = obj.position.x
                self.player.y = obj.position.y

    def collision_check(self):
        for rect in self.rect_list:
            if self.player.colliderect(rect):
                return True

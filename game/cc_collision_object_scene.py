from cc_object_scene import ccObjectScene
from cc_object_scene_file_loader import ccObjectSceneFileLoader
from cc_globals import ccGlobals
import pygame
from pprint import pprint


class ccCollisionObjectScene(ccObjectScene):
    def __init__(self):
        super().__init__()
        self.object_list = []  # gets objects from load function
        self.type = "ccCollisionObjectScene"

    def load(self, filename):
        loader = ccObjectSceneFileLoader()
        loader.process_file(filename)
        self.object_list = loader.get_objects()

    def draw(self):
        for obj in self.object_list:
            obj.draw(ccGlobals.get_renderer())

    def step(self, time_passed):
        pressed = pygame.key.get_pressed()
        for obj in self.object_list:
            if obj.id == 200:
                if pressed[pygame.K_LEFT]:
                    obj.position[0] -= 1
                if pressed[pygame.K_RIGHT]:
                    obj.position[0] += 1
                if pressed[pygame.K_UP]:
                    obj.position[1] -= 1
                if pressed[pygame.K_DOWN]:
                    obj.position[1] += 1

import pygame
from cc_scene import ccScene
from cc_globals import ccGlobals

from cc_object_scene import ccObjectScene
from cc_tile_scene_file_loader import ccTileSceneFileLoader


class ccTileMapScene(ccScene):

    def __init__(self):
        super().__init__()
        # self.object_list = []
        self.map = []
        self.type = "ccTileMapScene"
        self.offset = []

    def load(self, filename):
        loader = ccTileSceneFileLoader()
        loader.process_file(filename)
        self.map = loader.get_map()
        self.offset = loader.get_offset()

    def draw(self):
        x = self.offset[0]
        y = self.offset[1]
        print("map:", self.map)
        for row in self.map:
            for obj in row:
                x += obj.active_sprite.rectangle.width
                obj.draw(ccGlobals.get_renderer(), x, y)
            y += obj.active_sprite.rectangle.height
            x = 0

    def step(self, time_passed):
        # for obj in self.object_list:
        #     obj.step(time_passed)
        pass

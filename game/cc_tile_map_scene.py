import pygame
from cc_scene import ccScene
from cc_globals import ccGlobals

from cc_object_scene import ccObjectScene
from cc_tile_scene_file_loader import ccTileSceneFileLoader


class ccTileMapScene(ccScene):

    def __init__(self):
        super().__init__()
        self.map = []
        self.type = "ccTileMapScene"
        self.offset = []
        self.velocity = pygame.math.Vector2(0, 0)
        self.tile_width = 1

    def load(self, filename):
        loader = ccTileSceneFileLoader()
        loader.process_file(filename)
        self.map = loader.get_map()
        self.tile_width = self.map[0][0].active_sprite.rectangle.width
        self.offset = loader.get_offset()

    def draw(self):
        for row in self.map:
            for obj in row:
                obj.draw(ccGlobals.get_renderer())

    def step(self, time_passed):
        self.first_tile_pos += self.velocity.x * time_passed
        local_p = int(self.first_tile_pos)

        for row in self.map:
            for x in range(len(row)):
                obj = row[x]
                obj.position.x = local_p + x * self.tile_width

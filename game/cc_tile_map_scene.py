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
        self.actual_velocity = pygame.math.Vector2(0, 0)
        self.tile_width = 1
        self.first_tile_pos = 0  # use offset here
        self.looping = False

    def load(self, filename):
        loader = ccTileSceneFileLoader()
        loader.process_file(filename)
        self.map = loader.get_map()
        self.tile_width = self.map[0][0].active_sprite.rectangle.width
        self.offset = loader.get_offset()
        self.looping = loader.get_looping()
        self.velocity = loader.get_velocity()
        self.actual_velocity = loader.get_velocity()

    def draw(self):
        contained_length = 0
        start_row_index = abs(int(self.first_tile_pos / self.tile_width))
        end_row_index = 2 + int((ccGlobals.size[0] / self.tile_width) + start_row_index)
        if end_row_index > len(self.map[0]):
            contained_length = end_row_index - len(self.map[0])
            end_row_index = len(self.map[0])

        for row in self.map:
            for index in range(start_row_index, end_row_index):
                row[index].draw(ccGlobals.get_renderer())

        if self.looping is True:
            if contained_length != 0:
                for row in self.map:
                    for index in range(0, contained_length):
                        row[index].draw(ccGlobals.get_renderer())

    def step(self, time_passed):
        contained_length = 0
        self.first_tile_pos += self.actual_velocity.x * time_passed
        if self.looping is True:
            if abs(self.first_tile_pos) >= len(self.map[0]) * self.tile_width:
                self.first_tile_pos += len(self.map[0]) * self.tile_width

        local_p = int(self.first_tile_pos)

        start_row_index = abs(int(self.first_tile_pos / self.tile_width))
        end_row_index = 2 + int((ccGlobals.size[0] / self.tile_width) + start_row_index)
        if end_row_index > len(self.map[0]):
            contained_length = end_row_index - len(self.map[0])
            end_row_index = len(self.map[0])

        for row in self.map:
            for index in range(start_row_index, end_row_index):
                row[index].position.x = local_p + index * self.tile_width
                if row[index].hitbox is not None:
                    row[index].hitbox.x = row[index].position.x
                    row[index].hitbox.y = row[index].position.y

        if self.looping is True:
            if contained_length != 0:
                local_p = local_p + (len(self.map[0]) * self.tile_width)
                for row in self.map:
                    for index in range(0, contained_length):
                        row[index].position.x = local_p + index * self.tile_width
                        if row[index].hitbox is not None:
                            row[index].hitbox.x = row[index].position.x
                            row[index].hitbox.y = row[index].position.y

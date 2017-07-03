from GameData.cc_objects_file_loader import ccObjectsFileLoader
from GameData.cc_file_loader import ccFileLoader
from GameData.cc_logger import ccLogger
from GameData.cc_object_manager import ccObjectManager
from GameData.cc_resource_paths import *
from GameData.cc_globals import *
from GameData.cc_resource_paths import ccResourcePaths

import math


class ccTileSceneFileLoader(ccFileLoader):

    def __init__(self):
        super().__init__()
        self.objects_dict = {}
        self.map = []
        self.offset = []
        self.looping = False
        self.velocity_x = 0
        self.tile_width = 1

    def process_file(self, filename):
        try:
            self.load_file(filename)

        except:
            ccLogger.error('{} could not be loaded.'.format(filename))
            raise RuntimeError('{} could not be loaded.'.format(filename))
        self.__process_config()
        self.__process_object_sections()

    def __process_config(self):
        object_files = self.get_field(field_name='filenames', mandatory=True, section_name='Config')
        print("object_files: " + object_files[0])
        contained_looping = self.get_field(field_name = 'looping', mandatory=True, section_name="Config")
        self.velocity_x = self.get_field(field_name = 'velocity_x', mandatory=False, section_name="Config")
        if self.velocity_x == None:
            self.velocity_x = 0
        if contained_looping is True:
            self.looping=True
        self.offset.clear()
        self.offset.append(self.get_field(field_name='offset_x', mandatory=True, section_name='Config'))
        self.offset.append(self.get_field(field_name='offset_y', mandatory=True, section_name='Config'))
        print("offset: " , self.offset)
        for obj_file in object_files:
            loader = ccObjectsFileLoader()

            print("obj_file: " ,obj_file)
            loader.process_file(ccResourcePaths.get_objects() + obj_file)

    def __process_object_sections(self):
        self.set_first_section()
        while self.next_section():
            if self.current_section == self.get_section("Map"):
                raw_map = self.current_section["map"]
                for y in range(len(raw_map)):
                    object_row = []
                    for x in range(len(raw_map[y])):
                        obj = self.objects_dict[raw_map[y][x]].copy()
                        self.tile_width = obj.active_sprite.rectangle.width
                        sprite_height = obj.active_sprite.rectangle.height
                        obj.position.x = x * self.tile_width + self.offset[0]
                        obj.position.y = y * sprite_height + self.offset[1]
                        object_row.append(obj)
                    self.map.append(object_row)
                self.expand_map_for_looping()
            else:
                for name in self.current_section:
                    if name != "map":
                        self.objects_dict[name] = ccObjectManager.create_object(self.current_section[name])
    def get_map(self):
        return self.map

    def get_offset(self):
        return self.offset

    def get_looping(self):
        return self.looping
    
    def get_velocity(self):
        print(self.velocity_x)
        return pygame.math.Vector2(self.velocity_x, 0)
    
    def expand_map_for_looping(self):
        if self.looping is True:
            map_row_offset = len(self.map[0]) * self.tile_width
            screen_width_plus_remaining_part_of_tile = math.ceil(ccGlobals.size[0] / self.tile_width) * self.tile_width
            while screen_width_plus_remaining_part_of_tile >= (self.tile_width * len(self.map[0])):
                for y in range(len(self.map)):
                    for x in range(len(self.map[y])):
                        obj = self.map[y][x].copy()
                        obj.position.x += map_row_offset
                        self.map[y].append(obj)

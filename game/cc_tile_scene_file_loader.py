from cc_objects_file_loader import ccObjectsFileLoader
from cc_file_loader import ccFileLoader
from cc_logger import ccLogger
from cc_object_manager import ccObjectManager
from cc_resource_paths import *

from cc_resource_paths import ccResourcePaths


class ccTileSceneFileLoader(ccFileLoader):

    def __init__(self):
        super().__init__()
        self.objects_dict = {}
        self.map = []
        self.offset = []

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
            print("Current_section: ",self.current_section)
            if self.current_section == self.get_section("Map"):
                for row in self.current_section["map"]:
                    object_row = []
                    for object_name in row:
                        print("Object_name: ", object_name)
                #        set object pos based on where you are in the map
                        object_row.append(self.objects_dict[object_name].copy())
                    print("object_row: ",object_row)
                    self.map.append(object_row)
            else:
                for name in self.current_section:
                    if name != "map":
                        self.objects_dict[name] = ccObjectManager.create_object(self.current_section[name])
                        print("objects_dict: ",self.objects_dict)
    def get_map(self):
        return self.map

    def get_offset(self):
        return self.offset


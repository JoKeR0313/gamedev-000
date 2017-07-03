from GameData.cc_objects_file_loader import ccObjectsFileLoader
from GameData.cc_file_loader import ccFileLoader
from GameData.cc_logger import ccLogger
from GameData.cc_object_manager import ccObjectManager
from GameData.cc_resource_paths import *


class ccObjectSceneFileLoader(ccFileLoader):

    def __init__(self):
        super().__init__()
        self.objects_list = []

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
        for obj_file in object_files:
            loader = ccObjectsFileLoader()
            loader.process_file(ccResourcePaths.get_objects() + obj_file)

    def __process_object_sections(self):
        self.set_first_section()
        while self.next_section():
            obj = ccObjectManager.create_object(self.current_section['object_name'])
            obj.load(self.current_section)
            self.objects_list.append(obj)

    def get_objects(self):
        if len(self.objects_list) == 0:
            ccLogger.warning("ccObjectSceneFileLoader's objects_list attribute is empty.")
        return self.objects_list

    def get_scene_name(self):
        # gets the scene's name
        pass

from cc_objects_file_loader import ccObjectsFileLoader
from cc_fileloader import ccFileLoader
from cc_logger import ccLogger
from cc_object_manager import ccObjectManager

class ccObjectSceneFileLoader(ccFileLoader):
    def __init__(self):
        # call the ancestor's init
        self.objects_list = []
        pass

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
            loader.process_file(obj_file)

    def __process_object_sections(self):
        self.set_first_section()
        while self.next_section():
            obj = ccObjectManager(self.current_section['type'])
            obj.load(self.current_section)
            self.onject_list.append(obj) # stores the updated object clone provided by the ccObjectManager

    def get_objects(self):
        if len(self.objects_list) == 0:
            ccLogger.warning("ccObjectSceneFileLoader's objects_list attribute is empty.")
            return self.objects_list
        else:
            return self.objects_list

    def get_scene_name(self):
        # gets the scene's name
        pass

from cc_file_loader import *
from cc_logger import *
from cc_object_scene import *
from cc_resource_paths import *


class ccActFileLoader(ccFileLoader):

    def __init__(self):
        super().__init__()
        self.name = None
        self.scenes = []

    def process_file(self, filename):
        try:
            self.load_file(ccResourcePaths.get_acts() + filename)

        except:
            ccLogger.error('{} could not be loaded.'.format(filename))
            raise RuntimeError('{} could not be loaded.'.format(filename))
        self.__process_config()
        self.__process_object_sections()

    def __process_config(self):
        curr_act_name = self.get_field(field_name='name', mandatory=True, section_name='Config')
        self.name = curr_act_name

    def __process_object_sections(self):
        self.set_first_section()
        while self.next_section():
            constructor = globals()[self.current_section['scene_type']]
            obj_scene = constructor()
            obj_scene.load(ccResourcePaths.get_object_scenes() + self.current_section['filename'])
            self.scenes.append(obj_scene)

    def get_scenes(self):
        if len(self.scenes) == 0:
            ccLogger.warning("ccActFileLoader's scenes attribute is empty.")
        return self.scenes

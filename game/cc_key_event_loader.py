from cc_file_loader import ccFileLoader
from cc_logger import ccLogger
from cc_resource_paths import *


class ccKeyEventLoader(ccFileLoader):

    def __init__(self):
        super().__init__()
        self.keys = {}
        self.actions = {}

    def process_file(self, filename):
        try:
            self.load_file(ccResourcePaths.get_keys() + filename)
        except:
            ccLogger.error('{} could not be loaded.'.format(filename))
            raise RuntimeError('{} could not be loaded.'.format(filename))
        self.__process_keys()

    def __process_keys(self):
        self.set_section("keys")
        self.keys = self.current_section
        self.set_section("actions")
        self.actions = self.current_section

    def get_keys(self):
        if len(self.keys) == 0:
            ccLogger.warning("ccObjectSceneFileLoader's objects_list attribute is empty.")
        return self.keys

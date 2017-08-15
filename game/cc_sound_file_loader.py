from cc_sound_manager import ccSoundManager
import json
from cc_file_loader import ccFileLoader
from cc_logger import ccLogger
from cc_resource_paths import ccResourcePaths

class ccSoundFileLoader(ccFileLoader):

    def __init__(self):
        pass

    def process_file(self, filename):
        try:
            self.load_file(ccResourcePaths.get_sounds() + filename)

        except:
            ccLogger.error(str(filename) + ' file could not be loaded.')
            raise RuntimeError('File could not be loaded.')
        self.__process_sounds()

    def __process_sounds(self):
        self.set_first_section()
        sounds = self.get_section("sounds")
        for k,v in sounds.items():
            ccSoundManager.add_sound(k,v)
from cc_logger import ccLogger
from cc_scene_props import ccSceneProps


class ccScene:

    def __init__(self):
        self.name = ''
        self.type = 'ccScene'
        self.scene_props = ccSceneProps()

    def load(self, filename):
        ccLogger.error("File not loaded!")
        error_message = ccLogger("File not loaded!")

    def draw(self):
        ccLogger.error("Scene not drawed!")
        error_message = ccLogger("Scene not drawed!")

    def step(self, time_passed):
        time = time_passed
        ccLogger.error("Step currently not working!")
        error_message = ccLogger("Step currently not working!")

    def __process_config(self, config):
        # config is the config section of the JSON dict.
        # fill the variables from it what are present in this class
        pass

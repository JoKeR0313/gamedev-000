from cc_logger import ccLogger
from cc_scene_props import ccSceneProps


class ccScene:

    def __init__(self):
        self.name = ''
        self.type = 'ccScene'
        self.scene_props = ccSceneProps()

    def load(self, filename):
        ccLogger.error("Error: file not loaded.")
        error_message = ccLogger("Error: file not loaded.")

    def draw(self):
        ccLogger.error("Error: could not draw scene.")
        error_message = ccLogger("Error: could not draw scene.")

    def step(self, time_passed):
        time = time_passed
        ccLogger.error("Error: step does not work at the moment.")
        error_message = ccLogger("Error: step does not work at the moment.")

    def __process_config(self, config):
        # config is the config section of the JSON dict.
        # fill the variables from it what are present in this class
        pass

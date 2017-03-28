from cc_logger import *

class ccActManager:
    scenes = []

    def __init__(self):
        ccLogger.error("ActManager is an abstract class, can't call __init__!")
        raise NotImplementedError

    @classmethod
    def load(cls, filename):
        # creates a ccActFileLoader instance and processes the act file, makes the scenes
        # if something was loaded, removes it and initializes before loading
        if len(cls.scenes) > 0:
            cls.scenes = []
        loader = ccActFileLoader(filename)
        cls.scenes = loader.scenes

    @classmethod
    def draw(cls):
    #loops through all the scenes and calls it's draw method
        for scene in cls.scenes:
            scene.draw()

    @classmethod
    def step(cls):
    #loops through all the scenes and calls it's step method
        for scene in cls.scenes:
            scene.step()

    @classmethod
    def push_scene(cls, scene):
    #appends the incoming scene to the end of the scenes list
        cls.scenes.append(scene)

    @classmethod
    def pop_scene(cls):
        cls.scenes.pop()
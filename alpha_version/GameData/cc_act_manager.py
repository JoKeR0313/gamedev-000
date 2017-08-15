from GameData.cc_logger import *
from GameData.cc_act_file_loader import ccActFileLoader
from GameData.cc_collision_detector import ccCollisionDetector
from GameData.cc_globals import ccGlobals


class ccActManager:

    scenes = []

    def __init__(self):
        ccLogger.error("ActManager is an abstract class, can't call __init__!")
        raise NotImplementedError

    @classmethod
    def load(cls, filename):
        if len(cls.scenes) > 0:
            cls.scenes = []
        loader = ccActFileLoader()
        loader.process_file(filename)
        cls.scenes = loader.get_scenes()

    @classmethod
    def draw(cls):
        for scene in cls.scenes:
            scene.draw()

    @classmethod
    def step(cls, time_passed):
        tp = time_passed
        while tp > ccGlobals.frame_rate:
            tp -= ccGlobals.frame_rate
            for scene in cls.scenes:
                scene.step(ccGlobals.frame_rate)
            ccCollisionDetector.update(cls.scenes)
        for scene in cls.scenes:
            scene.step(tp)
        ccCollisionDetector.update(cls.scenes)

    @classmethod
    def push_scene(cls, scene):
        cls.scenes.append(scene)

    @classmethod
    def pop_scene(cls):
        cls.scenes.pop()

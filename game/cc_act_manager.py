from cc_logger import *
from cc_act_file_loader import ccActFileLoader
from cc_bball_coll_detector import BouncingBallCollisionDetector


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
        for scene in cls.scenes:
            # BouncingBallCollisionDetector.check_list_collision(scene.object_list)
            scene.step(time_passed)

    @classmethod
    def push_scene(cls, scene):
        cls.scenes.append(scene)

    @classmethod
    def pop_scene(cls):
        cls.scenes.pop()

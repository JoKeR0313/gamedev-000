import os
import sys
from cc_logger import ccLogger

import inspect
if not hasattr(sys.modules[__name__], '__file__'):
    __file__ = inspect.getfile(inspect.currentframe())


class ccResourcePaths:

    base_path = os.path.dirname(os.path.realpath(__file__))
    dir_name = "/resources/"
    resource_path = base_path + dir_name

    def __init__(self):
        ccLogger.error("ccResourcePath is an abstract class, can't call __init__!")
        raise NotImplementedError

    @classmethod
    def get_resources(cls):
        return cls.resource_path

    @classmethod
    def get_textures(cls):
        return cls.resource_path + "textures/"

    @classmethod
    def get_objects(cls):
        return cls.resource_path + "objects/"

    @classmethod
    def get_sprites(cls):
        return cls.resource_path + "sprites/"

    @classmethod
    def get_anims(cls):
        return cls.resource_path + "anims/"

    @classmethod
    def get_object_scenes(cls):
        return cls.resource_path + "object_scenes/"

    @classmethod
    def get_acts(cls):
        return cls.resource_path + "acts/"

    @classmethod
    def get_keys(cls):
        return cls.resource_path + "keys/"
    
    @classmethod
    def get_tile_scenes(cls):
        return cls.resource_path + "tile_scenes/"




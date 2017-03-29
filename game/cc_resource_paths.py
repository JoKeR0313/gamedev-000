import os
import cc_logger

class ccResourcePaths:

    base_path = os.path.dirname(os.path.realpath(__file__))

    def __init__(self):
        ccLogger.error("ccResourcePath can not be instanted")
        raise NotImplementedError

    @classmethod
    def get_resources(cls):
        return cls.base_path + "/resources/"

    @classmethod
    def get_objects(cls):
        return cls.base_path + "/resources/objects/"

    @classmethod
    def get_sprites(cls):
        return cls.base_path + "/resources/sprites/"

    @classmethod
    def get_anims(cls):
        return cls.base_path + "/resources/anims/"

    @classmethod
    def get_object_scenes(cls):
        return cls.base_path + "/resources/object_scenes/"

    @classmethod
    def get_acts(cls):
        return cls.base_path + "/resources/acts/"



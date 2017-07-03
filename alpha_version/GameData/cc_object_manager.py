from GameData.cc_logger import *
from copy import deepcopy


class ccObjectManager:

    objects = {}

    def __init__(self):
        error = "ccObjectManager is an abstract class, can't call __init__!"
        raise Exception(error)

    @classmethod
    def add_object(cls, object_name, obj):
        if object_name in cls.objects:
            ccLogger.warning(object_name + " is already loaded. It will not be overwritten.")
        else:
            cls.objects[object_name] = obj

    @classmethod
    def create_object(cls, object_name):
        try:
            found_object = cls.objects[object_name]
            return found_object.copy()
        except:
            ccLogger.error(object_name, "cannot be found.")
        return None

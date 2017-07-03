from GameData.cc_object_props import ccObjectProps
from GameData.cc_logger import ccLogger
from copy import deepcopy


class ccObject:

    def __init__(self):
        self.type = 'ccObject'
        self.id = None
        self.active_sprite = None
        self.object_props = ccObjectProps()

    def load(self, obj_section):
        if "visible" in obj_section:
            self.object_props.object_visible = obj_section["visible"]
        if "enabled" in obj_section:
            self.object_props.object_enabled = obj_section["enabled"]
        if "id" in obj_section:
            self.id = obj_section["id"]

    def draw(self, renderer):
        ccLogger.error("ccObject is an abstract class, yon can't call the draw function!")
        raise NotImplementedError

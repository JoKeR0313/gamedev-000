from cc_object_props import ccObjectProps
from cc_logger import ccLogger


class ccObject:

    def __init__(self):
        # initialize instance variables
        self.type = 'ccObject' # not sure this will be needed because python has type() function
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

    def draw(self):
        ccLogger.error("This is an abstract class, yon can't call this function!")
        raise NotImplementedError
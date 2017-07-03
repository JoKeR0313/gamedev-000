from GameData.cc_object_props import ccObjectProps
from GameData.cc_logger import ccLogger
from GameData.cc_sprite_manager import ccSpriteManager
from GameData.cc_basic_object import ccBasicObject
from copy import deepcopy


class ccTileObject(ccBasicObject):

    def __init__(self):
        super().__init__()
        self.type = 'ccTileObject'

    def load(self, obj_section):
        super().load(obj_section)

    def copy(self):
        new_object = ccTileObject()
        self.fill(new_object)
        return new_object

from GameData.cc_anim_object import ccAnimObject
from GameData.cc_key_event_handler import ccKeyEventHandler
from GameData.cc_globals import ccGlobals

class TrashcanObject(ccAnimObject):

    def __init__(self):
        super().__init__()
        self.type = 'TrashcanObject'
        self.id = "trashcan"
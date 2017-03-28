from cc_logger import ccLogger
from cc_anim_frame import *


class ccAnimSprite:

    def __init__(self):
        self.frames = []

    def add_frame(self, frame):
        self.frames.append(frame)

    def get_frame(self, frame_number):
        try:
            return self.frames[frame_number]
        except:
            ccLogger.error(frame_number, "not found with the given index.")
        return None

from cc_logger import ccLogger
from cc_anim_frame import *


class ccAnimSprite:

    def __init__(self):
        self.frames = []
        self.sound = None
        self.counter = -1

    def add_frame(self, frame):
        self.frames.append(frame)

    def add_sound(self, sound):
        self.sound = sound
    
    def get_frame(self, frame_number):
        if self.counter == 0 and self.sound is not None:
            self.sound.play()
        try:
            self.counter+=1
            if self.counter >= len(self.frames):
                self.counter = 0
            return self.frames[frame_number]
        except:
            return None

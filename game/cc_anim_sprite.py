from cc_logger import ccLogger


class ccAnimSprite:

    def __init__(self):
        self.ccAnimFrame = []

    def add_frame(self, frame):
        if frame in self.ccAnimFrame:
            return ccLogger.error("Frame already exists.")
        self.ccAnimFrame.append(frame)

    def get_frame(self, frame_number):
        try:
            return self.ccAnimFrame[frame_number]
        except:
            ccLogger.error("ccAnimFrame not found with the given index.")
            return None

from GameData.cc_logger import ccLogger


class ccSceneProps:

    def _init__(self):
        self.scene_visible = True
        self.scene_enabled = True

    def set_enabled(self, enabled):
        self.scene_enabled = enabled

    def set_visible(self, visible):
        self.scene_visible = visible

    def get_enabled(self):
        return self.scene_enabled

    def get_visible(self):
        return self.scene_visible

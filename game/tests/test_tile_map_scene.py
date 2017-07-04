import import_dir_setter
from cc_tile_map_scene import ccTileMapScene
from cc_globals import ccGlobals


class ccTestTileMapScene(ccTileMapScene):
    # this logic should be in the ccTileMapScene

    def __init__(self):
        super().__init__()

    def step(self, time_passed):
        super().step(time_passed)
        if ccGlobals.get_scene_velocity().x != 0:
            self.actual_velocity.x = self.velocity.x
        else:
            self.actual_velocity.x = 0

        if ccGlobals.get_scene_velocity().y != 0:
            self.actual_velocity.y = self.velocity.y
        else:
            self.actual_velocity.y = 0

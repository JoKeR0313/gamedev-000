import import_dir_setter
from cc_tile_map_scene import ccTileMapScene
from cc_globals import ccGlobals

class ccTestTileMapScene(ccTileMapScene):

    def __init__(self):
        super().__init__()
        self.velocity.x += -0.1

    def step(self, time_passed):
        current_velocity = self.velocity.x * time_passed 
        for row in self.map:
            for obj in row:
                obj.position.x += current_velocity

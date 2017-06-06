import import_dir_setter
from cc_tile_map_scene import ccTileMapScene
from cc_globals import ccGlobals

class ccTestTileMapScene(ccTileMapScene):
# this logic should be in the ccTileMapScene
    def __init__(self):
        super().__init__()
        self.velocity.x = -0.05
        self.first_tile_pos = 0 # use offset here

    def step(self, time_passed):
        self.first_tile_pos += self.velocity.x * time_passed
#        if self.p < -self.map[0][0].active_sprite.rectangle.width:
#            self.p += self.map[0][0].active_sprite.rectangle.width
        local_p = int(self.first_tile_pos)

        for row in self.map:
            for x in range(len(row)):
                obj = row[x]
                obj.position.x = local_p + x * obj.active_sprite.rectangle.width
                obj.position.y -= 0.0

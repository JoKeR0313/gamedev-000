from cc_object_scene import ccObjectScene
from cc_globals import ccGlobals


class ccBouncingBallScene(ccObjectScene):

    def __init__(self):
        super().__init__()
        self.type = "ccBouncingBallScene"

    def step(self, time_passed):
        for obj in self.object_list:
            obj.step(time_passed)
            if obj.position.x + obj.active_sprite.rectangle.width >= ccGlobals.size[0]:
                obj.velocity.x = -obj.velocity.x
            elif obj.position.x <= 0:
                obj.velocity.x = -obj.velocity.x
            elif obj.position.y + obj.active_sprite.rectangle.height >= ccGlobals.size[1]:
                obj.velocity.y = -obj.velocity.y
            elif obj.position.y <= 0:
                obj.velocity.y = -obj.velocity.y

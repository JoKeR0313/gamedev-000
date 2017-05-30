from cc_object_props import ccObjectProps
from cc_logger import ccLogger
from copy import deepcopy


class ccTileObject(ccObject):

    def __init__(self):
        super().__init__()
        self.type = 'ccTileObject'
        self.position = pygame.math.Vector2(0, 0)

    def load(self, obj_section):
        super.load()

    def draw(self, renderer):
        self.active_sprite.draw(renderer, self.position.x, self.position.y)

        # print(self.active_sprite.image.get_rect().size)

        # x = 0
        # y = 0
        # for row in self.map:
        #     for obj in row:
        #         obj.position = pygame.math.Vector2(x, y)
        #         x += 32
        #         obj.draw(ccGlobals.get_renderer())
        #     y += 32
        #     x = 0

        # ccGlobals.get_renderer()

    def set_position(self, new_position):
        self.position = new_position

from cc_object_scene import ccObjectScene
from cc_globals import ccGlobals
import copy


class ccBouncingBallScene(ccObjectScene):

    def __init__(self):
        super().__init__()
        self.rect_list = []
        self.type = "ccBouncingBallScene"

    def load(self, filename):
        super().load(filename)
        self.rect_list = self.get_rects()
        print(self.rect_list)

    def step(self, time_passed):
        self.update_rects()
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

        self.collision_check()

    def get_rects(self):
        rects = []
        for obj in self.object_list:
            if obj.id != 200:
                rect = copy.deepcopy(obj.active_sprite.rectangle)
                rect.x = obj.position.x
                rect.y = obj.position.y
                rects.append(rect)
        return rects

    def update_rects(self):
        for rect, obj in zip(self.rect_list, self.object_list):
            rect.x = obj.position.x
            rect.y = obj.position.y

    def collision_check(self):
        for rect, obj in zip(self.rect_list, self.object_list):
            for check_rect in self.rect_list:
                if rect != check_rect:
                    if rect.colliderect(check_rect):
                        obj.velocity.x = -obj.velocity.x
                        obj.velocity.y = -obj.velocity.y

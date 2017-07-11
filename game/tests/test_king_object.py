from cc_anim_object import ccAnimObject
from cc_globals import ccGlobals
from cc_key_event_handler import ccKeyEventHandler


class KingObject(ccAnimObject):

    def __init__(self):
        super().__init__()
        self.type = 'KingObject'
        self.jumping = False

    def step(self, time_passed):
        if ccKeyEventHandler.get_is_right_pressed():
            self.play()
        else:
            self.pause()
        self.jump()
        super().step(time_passed)

    def copy(self):
        new_object = KingObject()
        self.fill(new_object)
        return new_object

    def objecthit(self, other_obj):
        local_hitbox_y = self.hitbox.y
        self.velocity.y = 0
        self.hitbox.y = other_obj.hitbox.y - self.hitbox.height
        self.position.y -= local_hitbox_y - self.hitbox.y

    def jump(self):
        if self.jumping is False and ccKeyEventHandler.get_is_up_pressed():
            self.velocity.y = -2
            self.jumping = True
        if self.jumping is True:
            self.velocity.y *= 0.5

        if self.jumping is True and self.velocity.y > -0.05:
            self.jumping = False
            self.velocity.y = 0.25
        if self.jumping is False:
            self.velocity.y *= 1.5

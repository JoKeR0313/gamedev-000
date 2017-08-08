from GameData.cc_anim_object import ccAnimObject
from GameData.cc_key_event_handler import ccKeyEventHandler
from GameData.cc_globals import ccGlobals

class PlayerObject(ccAnimObject):

    def __init__(self):
        super().__init__()
        self.type = 'PlayerObject'
        self.jumping = False
        self.colliding = False
        self.desired_position = 100 # TODO get it from the json file in loading time

    def step(self, time_passed):
        if ccKeyEventHandler.get_is_right_pressed():
            self.play()
            if self.current_anim_name != "playerRunAnim":
                self.set_anim("playerRunAnim")
        else:
            self.pause()
            self.set_anim("playerStandAnim")
        self.jump()
        if self.colliding is False and self.velocity.y == 0:
            self.velocity.y = 0.3
        self.colliding = False
        super().step(time_passed)

    def copy(self):
        new_object = PlayerObject()
        self.fill(new_object)
        return new_object

    def objecthit(self, other_obj):
        if self.hitbox.y + self.hitbox.height <= other_obj.hitbox.y + other_obj.hitbox.height and self.velocity.y >= 0:
            self.velocity.y = 0
            local_hitbox_y = self.hitbox.y
            self.hitbox.y = other_obj.hitbox.y - self.hitbox.height
            self.position.y -= local_hitbox_y - self.hitbox.y
            if self.jumping is False and \
              ccKeyEventHandler.get_is_right_pressed() and \
              self.position.x < self.desired_position:
                self.position.x += 1 # to compensate the stuck/jump when it's going backwards a bit
        else:
            outpos_x = 0
            outpos_y = 0
            intersect = self.hitbox.clip(other_obj.hitbox)
            if intersect.width < intersect.height:
                if self.hitbox.x < other_obj.hitbox.x:
                    outpos_x = -intersect.width
                    ccGlobals.blocked = True
                else:
                    outpos_x = intersect.width
            else:
                if self.hitbox.y < other_obj.hitbox.y:
                    outpos_y = -intersect.height
                else:
                    outpos_y = intersect.height
            self.position.x += outpos_x
            self.position.y += outpos_y
            self.hitbox.x += outpos_x
            self.hitbox.y += outpos_y

    def jump(self):
        if self.jumping is False and ccKeyEventHandler.get_is_up_pressed():
            self.velocity.y = -2
            self.jumping = True
        if self.jumping is True:
            if ccKeyEventHandler.get_is_right_pressed():
                ccGlobals.blocked = False
            self.velocity.y *= 0.5

        if self.jumping is True and self.velocity.y > -0.05:
            self.jumping = False
            self.velocity.y = 0.25
        if self.jumping is False:
            self.velocity.y *= 1.5
            if self.velocity.y > 1.1:
                self.velocity.y = 1.1

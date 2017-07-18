from cc_anim_object import ccAnimObject
from cc_globals import ccGlobals
from cc_key_event_handler import ccKeyEventHandler


class KingObject(ccAnimObject):

    def __init__(self):
        super().__init__()
        self.type = 'KingObject'
        self.jumping = False
        self.colliding = False

    def step(self, time_passed):
        if ccKeyEventHandler.get_is_right_pressed():
            self.play()
        else:
            self.pause()
        self.jump()
        if self.colliding is False and self.velocity.y == 0:
            self.velocity.y = 0.3
        self.colliding = False
        super().step(time_passed)

    def copy(self):
        new_object = KingObject()
        self.fill(new_object)
        return new_object

    def objecthit(self, other_obj):
        local_hitbox_x = self.hitbox.x
        local_hitbox_y = self.hitbox.y
        intersect = self.hitbox.clip(other_obj.hitbox)
        if self.hitbox.y + self.hitbox.height <= other_obj.hitbox.y + other_obj.hitbox.height and self.velocity.y >= 0:
        # if intersect.width > intersect.height:
            self.velocity.y = 0
            self.hitbox.y = other_obj.hitbox.y - self.hitbox.height
            self.position.y -= local_hitbox_y - self.hitbox.y
        else:
            self.velocity.y = 0
            if self.hitbox.x < other_obj.hitbox.x:
#                self.hitbox.x = other_obj.hitbox.x - self.hitbox.width
#                self.position.x -= local_hitbox_x - (other_obj.hitbox.x - self.hitbox.width)
                ccGlobals.blocked = True
            else:
                self.hitbox.x = other_obj.hitbox.x + self.hitbox.width
                self.position.x += self.hitbox.x - local_hitbox_x
                
            if self.position.x > 98 or self.position.x < 102:
                self.velocity.x = 0
                self.position.x = 100
        
        # local_hitbox_y = self.hitbox.y
        # local_hitbox_x = self.hitbox.x
        # ccGlobals.blocked = True
        # self.velocity.y = 0
        # self.hitbox.y = other_obj.hitbox.y - self.hitbox.height
        # self.position.y -= local_hitbox_y - self.hitbox.y
        # if ccGlobals.blocked is False:
        #     self.colliding = True

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
            if self.velocity.y > 1.1:
                self.velocity.y = 1.1

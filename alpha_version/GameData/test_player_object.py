from GameData.cc_anim_object import ccAnimObject
from GameData.cc_key_event_handler import ccKeyEventHandler
from GameData.cc_globals import ccGlobals
from enum import Enum
from GameData.cc_logger import ccLogger


class State(Enum):
    standing = 0
    running = 1
    jumping = 2
    falling = 3


class PlayerObject(ccAnimObject):

    def __init__(self):
        super().__init__()
        self.type = 'PlayerObject'
        self.colliding = False
        self.state = State.standing
        self.desired_position = 100  # TODO get it from the json file in loading time

    def step(self, time_passed):
        if self.colliding is False and self.state != State.jumping:
            if self.velocity.y == 0:
                ccLogger.error("zuhan")
                self.velocity.y = 0.3
            elif self.state != State.falling:
                self.velocity.y = 0.025
                self.state = State.falling
                self.set_anim("playerFallAnim")
                self.play()


        if self.state == State.standing:
            ccLogger.error("Standing", self.position.x, self.position.y)
            if ccKeyEventHandler.get_is_up_pressed():
                self.state = State.jumping
                self.velocity.y = -2
                self.set_anim("playerJumpAnim")
                self.play()
            else:
                if ccKeyEventHandler.get_is_right_pressed():
                    ccGlobals.blocked = False
                    self.state = State.running
                    self.set_anim("playerRunAnim")
                    self.play()

        elif self.state == State.running:
            ccLogger.error("Running", self.position.x, self.position.y)            
            if ccKeyEventHandler.get_is_up_pressed():
                self.state = State.jumping
                self.velocity.y = -2
                self.set_anim("playerJumpAnim")
                self.play()
            else:
                if ccKeyEventHandler.get_is_right_pressed() is False:
                    ccLogger.error("Running right key pressed = FALSE")
                    ccGlobals.blocked = True
                    self.state = State.standing
                    self.set_anim("playerStandAnim")
                    self.play()

        elif self.state == State.jumping:
            ccLogger.error("Jumping", self.position.x, self.position.y)           
            if self.velocity.y >= -0.05:
                self.velocity.y = 0.025
                self.state = State.falling
                self.set_anim("playerFallAnim")
                self.play()
            self.velocity.y *= 0.7

        elif self.state == State.falling:
            if self.velocity.y <= 0:
                self.velocity.y = 0.05
            ccLogger.error("Falling", self.position.x, self.position.y)            
            self.velocity.y *= 1.3
            if self.velocity.y > 1.1:
                self.velocity.y = 1.1

        self.colliding = False
        super().step(time_passed)

    def copy(self):
        new_object = PlayerObject()
        self.fill(new_object)
        return new_object

    def objecthit(self, other_obj):
        self.colliding = True

        if self.state == State.falling:
            self.state = State.standing
            self.set_anim("playerStandAnim")
            self.play()

        if self.state == State.jumping:
            self.state = State.falling
            self.set_anim("playerFallAnim")
            self.play()

        intersect = self.hitbox.clip(other_obj.hitbox)
        outpos_x = 0
        outpos_y = 0

        if self.velocity.y > 0:  # falling down
            if other_obj.velocity.x == 0 and other_obj.velocity.y == 0:  # other is standing
                if self.hitbox.height / 2 > intersect.height:
                    if self.hitbox.y > other_obj.hitbox.y:  # move Y position based on collision positions
                        # ccLogger.error("Falling down - if-if ág")
                        outpos_y = intersect.height
                    else:
                        # ccLogger.error("Falling down - if-else ág", intersect.height)
                        outpos_y = -intersect.height
                else:
                    if self.hitbox.x < other_obj.hitbox.x:  # move X position based on collision positions
                        outpos_x = -intersect.width
                        ccGlobals.blocked = True
                    else:
                        outpos_x = intersect.width
            else:
                ccLogger.error("Missing implementation")
        else:  # jumping or walking
            if other_obj.velocity.x == 0 and other_obj.velocity.y == 0:  # other is standing
                if self.hitbox.height / 2 > intersect.height:
                    if self.hitbox.y > other_obj.hitbox.y:  # move Y position based on collision positions
                        # ccLogger.error("Jumping or walking - if-if ág")
                        outpos_y = intersect.height
                        self.velocity.y = 0
                        
                    else:
                        # ccLogger.error("Jumping or walking - if-else ág")
                        outpos_y = -intersect.height

        self.position.x += outpos_x
        self.position.y += outpos_y
        self.hitbox.x += outpos_x
        self.hitbox.y += outpos_y
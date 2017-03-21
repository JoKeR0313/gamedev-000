from cc_basic_object import ccBasicObject

class ccAnimObject(ccBasicObject):
    def __init__(self):
        # call the ancestor's __init__()
        super().__init__()
        # sets the object type to ccAnimObject
        self.type = "ccAnimObject"
        # and inits everything what's needed to default
        # NO loading happens here
        # anims list should contain the loaded ccAnimSprites
        # story the current animation/frame in variable(s) so you will know where are you currently and can step to the next frame/anim
        pass

    def load(self, obj_file_loader):
        # call ancestor's load() method and get the sprite from SpriteManager
        # print error if something bad happens
        # load the data. All the anim should already be in SpriteManager so get it from there!
        # check the last object in test.objects.json file
        pass

    def add_anim(self, anim):
        # add an animation to anims list. anim should be ccAnimSprite
        pass

    def draw(self):
        # this is not needed, it can use the ancestor's draw method
        pass

    def step(self, time_passed):
        # use the ancestor's step to do moving
        # handle the anim changing. The incoming time_passed has the passed millisecs since last frame. Use it to move forward in animation
        # if the displayed sprite should be changed, set the active_sprite with the currently active ccAnimSprite's sprite. active_sprite should always point to a ccSprite object, otherwise the program will crash
        pass

    def play(self, anim_name=current_anim):
        # set and start playing an anim. anim_name is optional, it should play the current animation if the anim_name is not set
        # if an anim was paused, resume from that point where is was
        pass

    def pause(self):
        # pause the current animation
        pass

    def reset(self):
        # don't change the animation but reset it to start
        # pause the animation
        pass
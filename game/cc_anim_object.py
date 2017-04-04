from cc_basic_object import ccBasicObject
from cc_anim_frame import ccAnimFrame
from cc_anim_sprite import ccAnimSprite
from cc_logger import ccLogger
from cc_sprite_manager import ccSpriteManager
from cc_anims_file_loader import ccAnimsFileLoader

class ccAnimObject(ccBasicObject):
    def __init__(self):
        super().__init__()
        self.type = 'ccAnimObject'
        self.time = 0
        # and inits everything what's needed to default
        # NO loading happens here
        self.anims = []
        # anims list should contain the loaded ccAnimSprites
        self.current_anim = None
        self.current_frame = None
        # store the current animation/frame in variable(s) so you will know where are you currently and can step to the next frame/anim

    def load(self, anim_data):
        # call ancestor's load() method and get the sprite from SpriteManager
        try:
            super().load(anim_data)
            for anim_name in anim_data['animations']:
                anim = ccSpriteManager.get_sprite(anim_name)
                self.anims.append(anim)
            self.current_anim = ccSpriteManager.get_sprite(anim_data['start_anim'])
            self.current_frame = self.current_anim.get_frame(0)
            self.active_sprite = self.current_frame.get_sprite()

        except:
            ccLogger.error('Sprite could not be loaded.')
            raise RuntimeError('Sprite could not be loaded.')
        # print error if something bad happens
        # load the data. All the anim should already be in SpriteManager so get it from there!
        # check the last object in test.objects.json file

    def add_anim(self, anim):
        # add an animation to anims list. anim should be ccAnimSprite
        if type(anim) == 'ccAnimSprite':
            self.anims.append(anim)
        else:
            ccLogger.error('Not Anim sprite' + type(anim))

    def draw(self, renderer):
        # this is not needed, it can use the ancestor's draw method
        ccBasicObject.draw(self, renderer)

    def step(self, time_passed):
        # use the ancestor's step to do moving
        super().step(time_passed)
        self.time += time_passed
        if self.current_frame.time < time_passed:
            self.current_frame = self.current_anim.get_frame(self.current_frame.get_next_frame())
            if self.current_frame == None:
                self.current_frame = self.current_anim.get_frame(0)
                ccLogger.warning("Animation change should be implemented")
                #WARNING
            self.active_sprite = self.current_frame.get_sprite()
        # handle the anim changing. The incoming time_passed has the passed millisecs since last frame.
        # Use it to move forward in animation
        # if the displayed sprite should be changed, set the active_sprite with the
        # currently active ccAnimSprite's sprite. active_sprite should always point
        # to a ccSprite object, otherwise the program will crash
        pass

    def play(self, anim_name=None):
        if not anim_name:
            anim_name = self.current_anim
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
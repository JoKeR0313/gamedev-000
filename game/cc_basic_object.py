class ccBasicObject(ccObject):

    def __init__(self):
        # call the ancestor's __init__()
        self.type = "ccBasicObject"  # probably should use python's type(), so set that up with magic method(?)
        self.position = pygame.math.Vector2(0, 0)  # use Vector2. It should be able to store float values
        self.velocity = pygame.math.Vector2(0, 0)

    def load(self, obj_file_loader):
        # call ancestor's load() method and get the sprite from SpriteManager. If
        # sprite is not found, print error and set active_sprite to None
        pass

    def draw(self):
        # draw the active_sprite to the screen, to self.position position
        pass

    def step(self, time_passed):
        # change Object's position with velocity. Specialized object classes will
        # override this method and do other logic here also
        pass

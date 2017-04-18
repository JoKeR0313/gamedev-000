from cc_object_scene import ccObjectScene


class ccCollisionScene(ccObjectScene):
    def __init__(self):
        super().__init__()
        self.object_list = []  # gets objects from load function
        self.type = "ccCollisionScene"

    def load(self, filename):
        loader = ccObjectSceneFileLoader()
        loader.process_file(filename)
        self.object_list = loader.get_objects()

    def draw(self):
        for obj in self.object_list:
            obj.draw(ccGlobals.get_renderer())

    def step(self, time_passed):
        pressed = pygame.key.get_pressed()
        # for obj in self.object_list:

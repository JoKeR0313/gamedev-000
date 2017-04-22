from cc_object_scene import ccObjectScene
from cc_object_scene_file_loader import ccObjectSceneFileLoader
from cc_globals import ccGlobals


class ccCollisionObjectScene(ccObjectScene):
    def __init__(self):
        super().__init__()
        self.object_list = []  # gets objects from load function
        self.type = "ccCollisionObjectScene"

    def load(self, filename):
        loader = ccObjectSceneFileLoader()
        loader.process_file(filename)
        self.object_list = loader.get_objects()

    def draw(self):
        for obj in self.object_list:
            obj.draw(ccGlobals.get_renderer())

    def step(self, time_passed):
        player = None
        pressed = pygame.key.get_pressed()
        for obj in self.object_list:
            if obj.id == 200:
                print("yes")
                player = obj
            else:
                print("no")
        if pressed[pygame.K_LEFT]:
            player.velocity_x = 0.1

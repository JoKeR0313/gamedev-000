from cc_scene import ccScene
from cc_object_scene_file_loader import ccObjectSceneFileLoader


class ccObjectScene(ccScene):
    def __init__(self):
        super().__init__()
        self.object_list = []  # gets objects from load function
        self.type = "ccObjectScene"

    def load(self, filename):
        loader = ccObjectSceneFileLoader()
        loader.process_file(filename)
        self.object_list = loader.get_objects()

    def draw(self):
        for obj in self.object_list:
            obj.draw()

    def step(self, time_passed):
        for obj in self.object_list:
            obj.step(time_passed)

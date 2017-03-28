from cc_scene import ccScene
from cc_object_scene_file_loader import ccObjectSceneFileLoader


class ccObjectScene(ccScene):
    def __init__(self):
        super().__init__() # call ancecstor's init
        self.object_list = [] # create self.objects list, it should be empty now
        self.type = "ccObjectScene" # fill type field with ccObjectScene

    def load(self, filename):
        loader = ccObjectSceneFileLoader()
        loader.process_file(filename)
        self.object_list = loader.get_objects()
        # this will load the scene. There will be a ccObjectSceneFileLoader for this type of scene
        # it is different from the previous load methods (like ccSprite) because you should instantiate ccObjectSceneFileLoader here and do the loading
        # This difference is because we have only one ObjectScene in a file and no more so it's more logical to handle the whole loading here
        # ccObjectSceneFileLoader will have getter methods, you can get the objects, scene props and anything you need from it
        # __process_config() can be used here (it's in ccScene) to load common attributes
        pass

    def draw(self):
        # go through the objects list and call every object's draw method
        for object in self.object_list:
            object.draw()

    def step(self, time_passed):
        pass
        # call all the object's step method with time_passed

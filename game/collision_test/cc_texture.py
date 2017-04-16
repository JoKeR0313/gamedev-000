import pygame
from cc_logger import ccLogger


class ccTexture:
    resource_dir_path = "./resources/"

    def __init__(self):

        self.width = 0
        self.height = 0
        self.image = None

    def load_image(self, file_name):
        # load the image as a pygame.Surface and store it
        self.image = pygame.image.load(self.resource_dir_path + file_name)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def get_width(self):
        # give back loaded texture's width. print error if no texture is loaded
        # and give back 0
        if self.width == 0:
            ccLogger.error("Width is zero!")
        return self.width

    def get_height(self):
        # give back loaded texture's height. print error if no texture is
        # loaded and give back 0
        if self.height == 0:
            ccLogger.error("Height is zero!")
        return self.height

    def get_texture(self):
        # give back the texture stored. If no texture, give back None and print
        # error msg
        if self.image is None:
            ccLogger.error("There is no image!")
        return self.image

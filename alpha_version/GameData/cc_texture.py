import pygame
from GameData.cc_logger import ccLogger
from GameData.cc_resource_paths import ccResourcePaths


class ccTexture:

    def __init__(self):

        self.width = 0
        self.height = 0
        self.image = None

    def load_image(self, file_name):
        self.image = pygame.image.load(ccResourcePaths.get_textures() + file_name)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def get_width(self):
        if self.width == 0:
            ccLogger.error("Error: width is zero.")
        return self.width

    def get_height(self):
        if self.height == 0:
            ccLogger.error("Error: height is zero.")
        return self.height

    def get_texture(self):
        if self.image is None:
            ccLogger.error("Error: there is no image stored.")
        return self.image

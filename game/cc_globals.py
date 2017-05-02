import pygame
# this name is temporary (or not if we can't find a better one)

# currently this will contain a pointer to the pygame renderer

# !!! when this class is ready, remove the renderer parameter from everywhere and use the one provided here

# Skeleton


class ccGlobals:

    renderer = None
    size = (840, 480)

    @classmethod
    def set_renderer(cls, renderer):
        # set the renderer. Incoming param is what pygame provided
        cls.renderer = renderer

    @classmethod
    def get_renderer(cls):
        # get the self.renderer
        return cls.renderer
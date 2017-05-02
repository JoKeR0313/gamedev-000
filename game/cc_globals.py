import pygame


class ccGlobals:

    renderer = None
    size = (840, 480)

    @classmethod
    def set_renderer(cls, renderer):
        cls.renderer = renderer

    @classmethod
    def get_renderer(cls):
        return cls.renderer

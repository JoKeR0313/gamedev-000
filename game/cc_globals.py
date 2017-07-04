import pygame


class ccGlobals:

    renderer = None
    size = (840, 480)
    scene_velocity = pygame.math.Vector2(0, 0)

    @classmethod
    def set_renderer(cls, renderer):
        cls.renderer = renderer

    @classmethod
    def get_renderer(cls):
        return cls.renderer

    @classmethod
    def get_scene_velocity(cls):
        return cls.scene_velocity

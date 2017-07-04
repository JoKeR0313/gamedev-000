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

    @classmethod
    def set_scene_velocity(cls, scene_velocity_x, scene_velocity_y):
        cls.scene_velocity.x = scene_velocity_x
        cls.scene_velocity.y = scene_velocity_y

import pygame

from GameData.cc_key_event_loader import ccKeyEventLoader
from GameData.cc_globals import ccGlobals


class ccKeyEventHandler:

    keys = {"right": pygame.K_RIGHT, "left": pygame.K_LEFT, "up": pygame.K_UP, "down": pygame.K_DOWN,
            "fire": pygame.K_SPACE, "escape": pygame.K_ESCAPE}

    actions = {"right": 2, "left": -1, "up": -1, "down": 1,
               "fire": False, "escape": False}

    is_right_pressed = False
    is_left_pressed = False
    is_up_pressed = False
    is_down_pressed = False
    is_fire_pressed = False
    is_escape_pressed = False

    @classmethod
    def load(cls, filename):
        loader = ccKeyEventLoader()
        loader.process_file(filename)
        for key in list(loader.keys):
            for def_key in list(cls.keys):
                if key == def_key:
                    cls.keys[def_key] = eval(loader.keys[key])
        for action in list(loader.actions):
            for def_action in list(cls.actions):
                if action == def_action:
                    cls.actions[def_action] = loader.actions[action]

    @classmethod
    def update(cls):
        pressed = pygame.key.get_pressed()
        cls.reset_keys()
        if pressed[cls.keys["left"]]:
            cls.is_left_pressed = True
        if pressed[cls.keys["right"]]:
            cls.is_right_pressed = True
        if pressed[cls.keys["up"]]:
            cls.is_up_pressed = True
        if pressed[cls.keys["down"]]:
            cls.is_down_pressed = True
        if pressed[cls.keys["fire"]]:
            cls.is_fire_pressed = True
        if pressed[cls.keys["escape"]]:
            cls.is_escape_pressed = True
        # if not cls.is_left_pressed and not cls.is_right_pressed and not cls.is_up_pressed \
        #         and not cls.is_down_pressed and not cls.is_fire_pressed:

    @classmethod
    def reset_keys(cls):
        cls.is_right_pressed = False
        cls.is_left_pressed = False
        cls.is_up_pressed = False
        cls.is_down_pressed = False
        cls.is_fire_pressed = False
        cls.is_escape_pressed = False

    #------------- Getters --------------------
    @classmethod
    def get_is_right_pressed(cls):
        return cls.is_right_pressed

    @classmethod
    def get_is_left_pressed(cls):
        return cls.is_left_pressed

    @classmethod
    def get_is_up_pressed(cls):
        return cls.is_up_pressed

    @classmethod
    def get_is_down_pressed(cls):
        return cls.is_down_pressed

    @classmethod
    def get_is_fire_pressed(cls):
        return cls.is_fire_pressed

    @classmethod
    def get_is_escape_pressed(cls):
        return cls.is_escape_pressed

    @classmethod
    def get_actions(cls):
        return cls.actions

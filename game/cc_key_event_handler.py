import pygame

from cc_key_event_loader import ccKeyEventLoader


class ccKeyEventHandler:

    def __init__(self):
        self.keys = {"right": pygame.K_RIGHT, "left":  pygame.K_LEFT, "up": pygame.K_UP, "down" : pygame.K_DOWN,
                     "fire": pygame.K_SPACE}
        self.right = self.keys["right"]
        self.left = self.keys["left"]
        self.up = self.keys["up"]
        self.down = self.keys["down"]
        self.fire = self.keys["fire"]
        self.is_right_pressed = False
        self.is_left_pressed = False
        self.is_up_pressed = False
        self.is_down_pressed = False
        self.is_fire_pressed = False

    def load(self, filename):
        loader = ccKeyEventLoader()
        loader.process_file(filename)
        for key in list(loader.keys):
            for def_key in list(self.keys):
                if key == def_key:
                    self.keys[def_key] = eval(loader.keys[key])

    def update(self):
        self.right = self.keys["right"]
        self.left = self.keys["left"]
        self.up = self.keys["up"]
        self.down = self.keys["down"]
        self.fire = self.keys["fire"]
        pressed = pygame.key.get_pressed()
        self.reset_keys()
        if pressed[self.left]:
            self.is_left_pressed = True
        if pressed[self.right]:
            self.is_right_pressed = True
        if pressed[self.up]:
            self.is_up_pressed = True
        if pressed[self.down]:
            self.is_down_pressed = True
        if pressed[self.fire]:
            self.is_fire_pressed = True
        print(self.is_down_pressed, self.is_up_pressed, self.is_right_pressed, self.is_left_pressed, self.is_fire_pressed)

    def reset_keys(self):
        for attribute in dir(self):
            if attribute.startswith('is'):
                self.__setattr__(attribute, False)
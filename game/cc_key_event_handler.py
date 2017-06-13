import pygame

from cc_key_event_loader import ccKeyEventLoader


class ccKeyEventHandler:

    def __init__(self):
        self.keys = {"right": pygame.K_RIGHT, "left": pygame.K_LEFT, "up": pygame.K_UP, "down": pygame.K_DOWN,
                     "fire": pygame.K_SPACE}

        self.actions = {"right": 1, "left": -1, "up": -1, "down": 1,
                        "fire": False}

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
        for action in list(loader.actions):
            for def_action in list(self.actions):
                if action == def_action:
                    self.actions[def_action] = loader.actions[action]

    def update(self, obj):
        pressed = pygame.key.get_pressed()
        self.reset_keys()
        if pressed[self.keys["left"]]:
            self.left_action(obj)
            self.is_left_pressed = True
        if pressed[self.keys["right"]]:
            self.right_action(obj)
            self.is_right_pressed = True
        if pressed[self.keys["up"]]:
            self.up_action(obj)
            self.is_up_pressed = True
        if pressed[self.keys["down"]]:
            self.down_action(obj)
            self.is_down_pressed = True
        if pressed[self.keys["fire"]]:
            self.is_fire_pressed = True
        if not self.is_left_pressed and not self.is_right_pressed and not self.is_up_pressed \
                and not self.is_down_pressed and not self.is_fire_pressed:
            self.no_action(obj)
        print(self.is_down_pressed, self.is_up_pressed, self.is_right_pressed, self.is_left_pressed,
              self.is_fire_pressed)

    def left_action(self, obj):
        obj.position[0] += self.actions["left"]
        obj.play("anim_01")

    def right_action(self, obj):
        obj.position[0] += self.actions["right"]
        obj.pause()

    def up_action(self, obj):
        obj.position[1] += self.actions["up"]
        obj.reset()

    def down_action(self, obj):
        obj.position[1] += self.actions["down"]
        obj.play("anim_01")

    def fire_action(self, obj):
        pass

    def no_action(self, obj):
        obj.play("anim_00")

    def reset_keys(self):
        for attribute in dir(self):
            if attribute.startswith('is'):
                self.__setattr__(attribute, False)

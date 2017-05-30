import pygame


class ccKeyEventHandler:

    def __init__(self):
        self.right = pygame.K_RIGHT
        self.left = pygame.K_LEFT
        self.up = pygame.K_UP
        self.down = pygame.K_DOWN
        self.fire = pygame.K_SPACE
        self.is_right_pressed = False
        self.is_left_pressed = False
        self.is_up_pressed = False
        self.is_down_pressed = False
        self.is_fire_pressed = False

    def update(self):
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
        print(self.is_down_pressed, self.is_up_pressed, self.is_right_pressed, self.is_left_pressed)

    def reset_keys(self):
        for attribute in dir(self):
            if attribute.startswith('is'):
                self.__setattr__(attribute, False)
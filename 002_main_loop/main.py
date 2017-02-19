import sys
import random
import pygame
from fps_manager import FPSManager


class Screen:
    size = width, height = 840, 480
    black = 0, 0, 0
    screen = None

    @staticmethod
    def init():
        pygame.init()
        Screen.screen = pygame.display.set_mode(Screen.size,
                                                pygame.DOUBLEBUF & pygame.HWSURFACE)


class Ball:

    def __init__(self, surface):
        self.position = [0, 0]
        self.surface = surface
        self.speed = [0, 0]
        self.size = [surface.get_rect().width, surface.get_rect().height]

    def move(self, time_passed_in_sec):
        current_speed = [0, 0]
        current_speed[0] = self.speed[0] * time_passed_in_sec
        current_speed[1] = self.speed[1] * time_passed_in_sec
        self.position[0] += current_speed[0]
        self.position[1] += current_speed[1]

        # TODO: width, height are globals and position, size, speed should have
        # been classes
        if self.position[0] < 0 or \
           self.position[0] + self.size[0] > Screen.width:
            self.speed[0] = -self.speed[0]
        if self.position[1] < 0 or \
           self.position[1] + self.size[1] > Screen.height:
            self.speed[1] = -self.speed[1]


def main_loop(objects):
    #fps_man = FPSManager()
    # fps_man.set_fps(60)
    time_passed = 0
    clock = pygame.time.Clock()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        Screen.screen.fill(Screen.black)

        for obj in objects:
            time_passed_sec = time_passed / 1000.0
            obj.move(time_passed_sec)
            Screen.screen.blit(obj.surface, obj.position,
                               obj.surface.get_rect())

        pygame.display.flip()

    #    time_passed = fps_man.finish_frame()
        time_passed = clock.tick(60)


def main():
    speed = [100, 100]
    objects = []

    Screen.init()
    orig_ball_surface = pygame.image.load("ball.gif")
#    orig_ball_surface = pygame.image.load("small_ball.gif")
    for i in range(100):
        ball = Ball(orig_ball_surface)
        ball.position = [random.randint(0, Screen.width - ball.size[0] - 1),
                         random.randint(0, Screen.height - ball.size[1] - 1)]
        ball.speed[0] = random.choice([speed[0], -speed[0]])
        ball.speed[1] = random.choice([speed[1], -speed[1]])
        objects.append(ball)

    main_loop(objects)

main()

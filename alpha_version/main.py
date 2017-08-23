import pygame
import sys
import GameData.import_dir_setter
from GameData.cc_act_manager import ccActManager
from GameData.cc_globals import ccGlobals
from GameData.cc_key_event_handler import ccKeyEventHandler


class TestAlpha:
    logical_size = (1600, 900)
    screen_size = (800, 450)
    num_of_rows = 1
    num_changer = 1
    ccGlobals.frame_rate = 33

    def __init__(self):
        pygame.init()
        renderer = pygame.Surface(self.logical_size)  # creating a Surface with logical_size(1600x900) size
        ccGlobals.set_renderer(renderer)
        ccGlobals.size = self.logical_size
        self.screen_surface = pygame.display.set_mode(self.screen_size)
        # return a surface with screen_size(800x450)
        # pygame.FULLSCREEN you can pass it as second parameter

    def test_run(self):
        ccKeyEventHandler.load("test.keys.json")
        ccActManager.load("player_scene.act.json")
        clock = pygame.time.Clock()
        time_passed = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            if ccKeyEventHandler.get_is_escape_pressed():
                sys.exit()
            ccKeyEventHandler.update()
            self.update_scene_velocity()
            ccActManager.step(time_passed)
            ccGlobals.get_renderer().fill((0, 0, 0))
            ccActManager.draw()
            # there is a simple scale() function, faster than this one, but this is nicer
            pygame.transform.smoothscale(ccGlobals.get_renderer(), self.screen_size, self.screen_surface)
            pygame.display.flip()
            time_passed = clock.tick(30)

    def update_scene_velocity(self):
        if ccGlobals.blocked is True:
            ccGlobals.set_scene_velocity(0, 0)
        else:
            if ccKeyEventHandler.get_is_right_pressed():
                ccGlobals.set_scene_velocity(ccKeyEventHandler.get_actions()["right"], 0)
            else:
                ccGlobals.set_scene_velocity(0, 0)


def main():
    tester = TestAlpha()
    tester.test_run()

main()

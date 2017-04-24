import import_dir_setter
import pygame
import sys
from cc_resource_paths import ccResourcePaths
from cc_act_file_loader import ccActFileLoader
from cc_act_manager import ccActManager
from cc_globals import ccGlobals


class TestActLoader:
    size = (840, 480)
    num_of_rows = 1
    num_changer = 1

    def __init__(self):
        pygame.init()
        renderer = pygame.display.set_mode(self.size)
        ccGlobals.set_renderer(renderer)

    def test_run(self):
        self.load_act()
        clock = pygame.time.Clock()
        temp = ccGlobals.get_renderer()
        time_passed = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            ccGlobals.get_renderer().fill((0, 0, 0))
            ccActManager.step(time_passed)
            ccActManager.draw()
            ccActManager.step(time_passed)
            pygame.display.flip()
            time_passed = clock.tick(60)

    def load_act(self):
        ccActManager.load("test.act.json")


def main():
    tester = TestActLoader()
    tester.test_run()

main()

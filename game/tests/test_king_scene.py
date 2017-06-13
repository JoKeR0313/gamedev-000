import import_dir_setter
import pygame
import sys
from cc_resource_paths import ccResourcePaths
from cc_act_file_loader import ccActFileLoader
from cc_act_manager import ccActManager
from cc_globals import ccGlobals


class TestTileScene:
    size = (440, 480)
    num_of_rows = 1
    num_changer = 1

    def __init__(self):
        pygame.init()
        renderer = pygame.display.set_mode(self.size)
        ccGlobals.set_renderer(renderer)
        ccGlobals.size = self.size

    def test_run(self):
        ccActManager.load("test_king_scene.act.json")
        clock = pygame.time.Clock()
        time_passed = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            ccActManager.step(time_passed)
            ccGlobals.get_renderer().fill((0, 0, 0))
            ccActManager.draw()
            pygame.display.flip()
            time_passed = clock.tick(60)


def main():
    tester = TestTileScene()
    tester.test_run()


main()

import import_dir_setter
import pygame
import sys

from cc_act_manager import ccActManager
from cc_globals import ccGlobals
from cc_key_event_handler import ccKeyEventHandler


class TestTileScrollForKeyInput:
    size = (440, 480)
    num_of_rows = 1
    num_changer = 1

    def __init__(self):
        pygame.init()
        renderer = pygame.display.set_mode(self.size)
        ccGlobals.set_renderer(renderer)
        ccGlobals.size = self.size

    def test_run(self):
        keylistener = ccKeyEventHandler()
        keylistener.load("test.keys.json")
        ccActManager.load("test_tile_scene.act.json")
        clock = pygame.time.Clock()
        time_passed = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            for scene in ccActManager.scenes:
                keylistener.update(scene)
                for l in scene.map:
                    for obj in l:
                        keylistener.update(obj)
            ccActManager.step(time_passed)
            ccGlobals.get_renderer().fill((0, 0, 0))
            ccActManager.draw()
            pygame.display.flip()
            time_passed = clock.tick(30)


def main():
    tester = TestTileScrollForKeyInput()
    tester.test_run()

main()

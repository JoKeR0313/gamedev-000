import pygame

from cc_act_manager import ccActManager
from cc_globals import ccGlobals
from cc_key_event_handler import ccKeyEventHandler
from cc_key_event_loader import ccKeyEventLoader


class TestKeyEventHandler:
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
        ccActManager.load("test.act.json")
        clock = pygame.time.Clock()
        time_passed = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            keylistener.update()
            ccActManager.step(time_passed)
            ccGlobals.get_renderer().fill((0, 0, 0))
            ccActManager.draw()
            pygame.display.flip()
            time_passed = clock.tick(30)


def main():
    tester = TestKeyEventHandler()
    tester.test_run()

main()
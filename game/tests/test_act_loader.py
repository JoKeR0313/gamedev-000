import import_dir_setter
import pygame
from cc_resource_paths import ccResourcePaths
from cc_act_file_loader import ccActFileLoader
from cc_act_manager import ccActManager


class TestActLoader:
    size = (840, 480)
    sprites = []
    renderer = None
    num_of_rows = 1
    num_changer = 1

    def __init__(self):
        pygame.init()
        self.renderer = pygame.display.set_mode(self.size)

    def test_run(self):
        self.load_act()
        while True:
            pass
        # clock = pygame.time.Clock()
        # while True:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             sys.exit()
        #     self.renderer.fill((0, 0, 0))
        #     ccActManager.draw()
        #     pygame.display.flip()
    
    def load_act(self):
        loader = ccActFileLoader()
        loader.process_file(ccResourcePaths.get_acts() + "test.act.json")
        ccActManager.scenes.append(loader.get_scenes())
        print(ccActManager.scenes)


def main():
    tester = TestActLoader()
    tester.test_run()

main()
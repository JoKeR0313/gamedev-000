import import_dir_setter
import pygame
from act_manager import ccActManager


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
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.renderer.fill((0, 0, 0))
            ccActManager.draw()
            pygame.display.flip()
    
    def load_act(self):
        loader = ccSceneFileLoader()
        loader.process_file(ccResourcePaths.get_resources() + "object_scenes/background.objectscene.json")
        ccActManager.scenes.append(scene)

def main():
    tester = TestActLoader()
    tester.test_run()

main()
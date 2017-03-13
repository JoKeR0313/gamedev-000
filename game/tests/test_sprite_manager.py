import pygame
import sys
import import_dir_setter
from cc_texture import ccTexture
from cc_sprites_file_loader import ccSpritesFileLoader
from cc_sprite_manager import ccSpriteManager


class TestSpriteManager:
    size = (840, 480)
    sprites = []
    renderer = None

    def __init__(self):
        pygame.init()
        self.renderer = pygame.display.set_mode(self.size)

    def prepare_test(self):
        self.__load_sprites()
        self.__get_sprites_from_sprite_manager()

    def test_run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.renderer.fill((0, 0, 0))
            self.__draw_sprites()
            pygame.display.flip()

    def __draw_sprites(self):
        for i in range(len(self.sprites)):
            width = self.sprites[i].rectangle[0]
            height = self.sprites[i].rectangle[1]
            self.sprites[i].draw(self.renderer, i*width, i*height)

    def __load_sprites(self):
        ccTexture.resource_dir_path = "../resources/"
        loader = ccSpritesFileLoader()
        loader.process_file("../resources/sprites/test.sprites.json")

    def __get_sprites_from_sprite_manager(self):
        self.sprites.append(ccSpriteManager.get_sprite("test_00"))
        self.sprites.append(ccSpriteManager.get_sprite("test_02"))
        self.sprites.append(ccSpriteManager.get_sprite("test_03"))
        self.sprites.append(ccSpriteManager.get_sprite("test_all_001"))


if '__main__' == __name__:
    test = TestSpriteManager()
    test.prepare_test()
    test.test_run()

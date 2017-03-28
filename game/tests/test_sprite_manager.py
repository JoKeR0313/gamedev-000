import pygame
import sys
import import_dir_setter
from cc_texture import ccTexture
from cc_sprites_file_loader import ccSpritesFileLoader
from cc_sprite_manager import ccSpriteManager
from cc_globals import ccGlobals


class TestSpriteManager:
    sprites = []
    num_of_rows = 1
    num_changer = 1

    def __init__(self):
        pygame.init()
        ccGlobals.set_renderer(pygame.display.set_mode(ccGlobals.size))
        self.renderer = ccGlobals.get_renderer()

    def prepare_test(self):
        self.__load_sprites()
        self.__get_sprites_from_sprite_manager()

    def test_run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.renderer.fill((0, 0, 0))
            self.__draw_sprites()
            pygame.display.flip()
            clock.tick(30)

    def __draw_sprites(self):
        for j in range(self.num_of_rows):
            for i in range(len(self.sprites)):
                width = self.sprites[i].rectangle.width
                height = self.sprites[i].rectangle.height
                self.sprites[i].draw(self.renderer, i * width + j * width, i * height)
                self.sprites[i].draw(self.renderer,
                                     (len(self.sprites) - i - 1) * width + j * width,
                                     len(self.sprites) * height + i * height)
        self.__change_num_of_rows()

    def __change_num_of_rows(self):
        self.num_of_rows += self.num_changer
        if self.num_of_rows > 20:
            self.num_changer = -1
        if self.num_of_rows <= 1:
            self.num_changer = 1

    def __load_sprites(self):
        # we are in the /test directory, so we need to go back
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

from cc_fileloader import *
from cc_logger import *
from cc_sprite_manager import *
from cc_texture import *
from cc_sprite import *
from pygame import *


class ccSpritesFileLoader(ccFileLoader):

    def __init__(self):
        pass

    def process_file(self, filename):
        try:
            self.load_file(filename)

        except:
            ccLogger.error('File could not be loaded.')
            raise RuntimeError('File could not be loaded.')
        self.__configure()
        self.__process_sprites()

    def __configure(self):
        self.file_name = self.current_dict['Config']['filename']
        self.cc_texture = ccTexture()
        self.cc_texture.load_image(self.file_name)
        ccSpriteManager.add_texture(self.file_name, self.cc_texture)
        self.__process_sprites()

    def __process_sprites(self):
        for sprite_key in self.current_dict:
            if sprite_key != 'Config':
                if 'num_of_sprites' in self.current_dict[sprite_key]:
                    self.__create_multiple_sprites(sprite_key)
                else:
                    self.__create_one_sprite(sprite_key)

    def __create_one_sprite(self, sprite_key):
        self.name = sprite_key
        section = self.current_dict[sprite_key]
        rect = pygame.Rect(section['offset_x'], section['offset_y'], section['width'], section['height'])
        ccSpriteManager.add_sprite(self.name, ccSprite(self.cc_texture, rect))

    def __create_multiple_sprites(self, sprite_key):
        offset_x = 0
        offset_y = 0
        num = 0

        for i in range(self.current_dict[sprite_key]['num_of_sprites']):
            if offset_x > self.cc_texture.get_width():
                offset_y += self.current_dict[sprite_key]['height']
                offset_x = 0
            self.name = sprite_key + "%03d" % num
            section = self.current_dict[sprite_key]
            rect = pygame.Rect(offset_x, offset_y, section['width'], section['height'])
            ccSpriteManager.add_sprite(self.name, ccSprite(self.cc_texture, rect))
            offset_x += section['width']
            num += 1


# # Refactoring
#   Use current section

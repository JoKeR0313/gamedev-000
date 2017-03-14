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
        self.__config()

    def __config(self):
        self.file_name = self.current_dict['Config']['filename']
        self.cc_texture = ccTexture()
        self.cc_texture.load_image(self.file_name)
        ccSpriteManager.add_texture(self.file_name, self.cc_texture)
        for sprite_key in self.current_dict:
            if sprite_key != 'Config':
                if 'num_of_sprites' in self.current_dict[sprite_key]:
                    self.__multiple_sprite_init(sprite_key)
                else:
                    self.__sprite_init(sprite_key)

    def __sprite_init(self, sprite_key):
        self.name = sprite_key
        section = self.current_dict[sprite_key]
        width = section['width']
        height = section['height']
        offset_x = section['offset_x']
        offset_y = section['offset_y']
        rect = pygame.Rect(offset_x, offset_y, width, height)
        print(self.name, offset_x, offset_y, width, height)
        self.object = ccSprite(self.cc_texture, rect)
        self.__put_to_manager(self.object)

    def __multiple_sprite_init(self, sprite_key):
        offset_x = 0
        offset_y = 0
        num = 0

        for i in range(self.current_dict[sprite_key]['num_of_sprites']):
            if offset_x > self.cc_texture.get_width():
                offset_y += self.current_dict[sprite_key]['height']
                offset_x = 0
            self.name = sprite_key + "%03d" % num
            section = self.current_dict[sprite_key]
            width = section['width']
            height = section['height']
            offset_x = offset_x
            offset_y = offset_y
            self.rect = pygame.Rect(offset_x, offset_y, width, height)
            self.object = ccSprite(self.cc_texture, self.rect)
            self.__put_to_manager(self.object)
            offset_x += section['width']
            num += 1

    def __put_to_manager(self, sprite_obj):
        ccSpriteManager.add_sprite(self.name, sprite_obj)
from cc_fileloader import *
from cc_logger import *
from cc_sprite_manager import *


class ccSpritesFileLoader(ccFileLoader):

    def __init__(self):
        pass

    def process_file(self, filename):
        try:
            ccload = ccFileLoader()
            self.texture = ccload.load_file(filename)
        except:
            ccLogger.error('File could not be loaded.')
            raise RuntimeError('File could not be loaded.')
        self.__config()

    def __config(self):
        self.file_name = self.texture['Config']['filename']
        ccSpriteManager.add_texture(self.file_name, self.texture)
        for sprite in self.texture:
            if sprite != 'Config':
                if 'num_of_sprites' in self.texture[sprite]:
                    self.__multiple_sprite_init(sprite)
                else:
                    self.__sprite_init(sprite)


    def __sprite_init(self, sprite):
        self.name = sprite
        self.width = self.texture[sprite]['width']
        self.height = self.texture[sprite]['height']
        self.offset_x = self.texture[sprite]['offset_x']
        self.offset_y = self.texture[sprite]['offset_y']
        self.__put_to_manager()

    def __multiple_sprite_init(self, sprite):
        offset_x = 0
        offset_y = 0
        num = 000

        for i in range(self.texture[sprite]['num_of_sprites']):
            key = sprite
            if offset_x > 128:  # Obviously have to get the width of the original image, maybe from get_texture? or make a definition for it?
                offset_y += self.texture[key]['height']
                offset_x = 0
            self.name = key + "%03d" % (num)
            self.width = self.texture[key]['width']
            self.height = self.texture[key]['height']
            self.offset_x = offset_x
            self.offset_y = offset_y
            offset_x += self.texture[key]['width']
            self.__put_to_manager()
            num += 1

    def __put_to_manager(self):
        ccSpriteManager.add_sprite(self.name, self)
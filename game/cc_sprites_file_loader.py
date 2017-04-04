from cc_fileloader import *
from cc_logger import *
from cc_sprite_manager import *
from cc_texture import *
from cc_sprite import *
from pygame import *
from cc_resource_paths import *



class ccSpritesFileLoader(ccFileLoader):

    def __init__(self):
        pass

    def process_file(self, filename):
        try:
            self.load_file(ccResourePaths.get_sprites() + filename)

        except:
            ccLogger.error( str(filename) + ' file could not be loaded.')
            raise RuntimeError('File could not be loaded.')
        self.__configure()
        self.__process_sprites()

    def __configure(self):
        self.file_name = self.current_dict['Config']['filename']
        self.cc_texture = ccTexture()
        resource_path = ccResourePaths.get_textures() + self.file_name
        self.cc_texture.load_image(resource_path)
        ccSpriteManager.add_texture(str(resource_path), self.cc_texture)
        self.__process_sprites()

    def __process_sprites(self):
        self.set_first_section()
        while self.next_section():
            if 'num_of_sprites' in self.current_section:
                    self.__create_multiple_sprites()
            else:
                self.__create_one_sprite()

    def __create_one_sprite(self):
        self.name = list(self.current_dict)[self.current_section_id]
        section = self.current_section
        rect = pygame.Rect(section['offset_x'], section['offset_y'], section['width'], section['height'])
        ccSpriteManager.add_sprite(self.name, ccSprite(self.cc_texture, rect))

    def __create_multiple_sprites(self):
        offset_x = 0
        offset_y = 0
        num = 0

        for i in range(self.current_section['num_of_sprites']):
            print(self.cc_texture.get_width())
            if offset_x > self.cc_texture.get_width():
                offset_y += self.current_section['height']
                offset_x = 0
            self.name = list(self.current_dict)[self.current_section_id] + "%03d" % num
            section = self.current_section
            rect = pygame.Rect(offset_x, offset_y, section['width'], section['height'])
            ccSpriteManager.add_sprite(self.name, ccSprite(self.cc_texture, rect))
            offset_x += section['width']
            num += 1

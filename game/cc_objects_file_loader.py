from cc_file_loader import ccFileLoader
from cc_sprites_file_loader import ccSpritesFileLoader
from cc_basic_object import ccBasicObject
from cc_logger import ccLogger
from cc_object_manager import ccObjectManager
from cc_resource_paths import *
from cc_anim_object import ccAnimObject
from cc_anims_file_loader import ccAnimsFileLoader
from cc_tile_object import ccTileObject


class ccObjectsFileLoader(ccFileLoader):

    def __init__(self):
        super().__init__()

    def process_file(self, filename):
        try:
            self.load_file(filename)
            print(filename)
        except:
            ccLogger.error('{} could not be loaded.'.format(filename))
            raise RuntimeError('{} could not be loaded.'.format(filename))
        self.__process_config()
        self.__process_object_sections()

    def __process_config(self):
        sprites_files = self.get_field(field_name='filenames', mandatory=True, section_name='Config')
        print("sprites_files: ",sprites_files)
        for spr_file in sprites_files:
            loader = None
            if '.sprites.json' in spr_file:
                loader = ccSpritesFileLoader()
            elif '.anims.json' in spr_file:
                loader = ccAnimsFileLoader()
            loader.process_file(spr_file)

    def __process_object_sections(self):
        self.set_first_section()
        while self.next_section():
            constructor = globals()[self.current_section['type']]
            obj = constructor()
            obj.load(self.current_section)
            current_section_name = self.get_current_section_name()
            ccObjectManager.add_object(current_section_name, obj)  # gives objects and their name to the ccObjectManager

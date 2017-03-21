from cc_fileloader import ccFileLoader
from cc_sprites_file_loader import ccSpritesFileLoader
from cc_basic_object import ccBasicObject
from cc_logger import ccLogger


class ccObjectsFileLoader(ccFileLoader):

    def __init__(self):
        super().__init__()

    def process_file(self, filename):
        try:
            self.load_file(filename)

        except:
            ccLogger.error('{} could not be loaded.'.format(filename))
            raise RuntimeError('{} could not be loaded.'.format(filename))
        self.__process_config()

    def __process_config(self):
        sprites_files = self.get_field(field_name='filenames', mandatory=True, section_name='Config')
        for spr_file in sprites_files:
            loader = ccSpritesFileLoader()
            loader.process_file(spr_file)

    def process_object_sections(self):
        self.set_first_section()
        while self.next_section():
            constructor = globals()[self.current_section['type']]
            obj = constructor()
            obj.load(self.current_section)
            current_section_name = self.get_current_Section_name()
            #ccObjectManager.add_object(current_section_name, obj) # ccObjectManager not implemented yet

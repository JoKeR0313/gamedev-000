class ccSpritesFileLoader(ccFileLoader):
    def __init__(self):
        pass

    def process_file(self, filename):
        try:
            self.texture = self.__load_file(filename)
        except:
            raise RuntimeError('File could not be loaded.')  # should use logger
        self.__config()

    def __config(self):
        self.file_name = self.texture['Config']['filename']
        ccSpriteManager.add_texture(self.file_name, self.texture)

        for sprite in self.texture:
            if 'num_of_sprites' in self.texture[sprite]:
                self.__multiple_sprite_init()
                return

        self.__sprite_init()

    def __sprite_init(self):
        self.name = list(self.texture)[1]
        self.width = self.texture[self.name]['width']
        self.height = self.texture[self.name]['height']
        self.offset_x = self.texture[self.name]['offset_x']
        self.offset_y = self.texture[self.name]['offset_y']
        self.__put_to_manager()

    def __multiple_sprite_init(self):
        offset_x = 0
        offset_y = 0

        for key in sorted(self.texture.keys()):
            if key != 'Config':
                if offset_x > 128:  # Obviously have to get the width of the original image, maybe from get_texture? or make a definition for it?
                    offset_y += self.texture[key]['height']
                    offset_x = 0
                self.name = key
                self.width = self.texture[key]['width']
                self.height = self.texture[key]['height']
                self.offset_x = offset_x
                self.offset_y = offset_y
                offset_x += self.texture[key]['width']
                self.__put_to_manager()

    def __put_to_manager(self):
        ccSpriteManager.add_sprite(self.name, self)


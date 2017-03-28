from cc_fileloader import *
from cc_logger import *
from cc_sprite_manager import *
from cc_texture import *
from cc_sprite import *
from cc_anim_sprite import *
from cc_anim_frame import *
from cc_sprites_file_loader import *
from cc_resource_paths import *


class ccAnimsFileLoader(ccFileLoader):
    def __init__(self):
        pass

    def process_file(self, filename):
        try:
            self.load_file(filename)

        except:
            ccLogger.error('File could not be loaded.')
            raise RuntimeError('File could not be loaded.')
        self.__config()
        self.__process_all_anims_sprites()

    def __config(self):

        self.set_section("Config")
        self.file_name = ccResourcePaths.get_sprites() + self.get_field("filename")[7:] #cutting the "sprites" part of the filename in json

        loader = ccSpritesFileLoader()
        loader.process_file(self.file_name)

    def __process_all_anims_sprites(self):

        self.set_first_section()
        while self.next_section():
            self.__process_one_anims_sprite()

    def __process_one_anims_sprite(self):

        sprites = self.get_field("sprites")
        for i in range(len(sprites)):
            sprites[i] = ccSpriteManager.get_sprite(sprites[i])

        frames = self.get_field("frames")
        frame_list = []

        for i in range(len(frames)):
            splitted_frame = frames[i].split()
            frame_list.append(splitted_frame)

        for i in range(len(frame_list)):
            if frame_list[i][0] != 'goto':
                if len(frame_list[i]) == 1:
                    frame_list[i].append(frame_list[i - 1][1])
                if frame_list[i+1][0] != 'goto':
                    frame_list[i].append(frame_list[i+1][0])
                else:
                    frame_list[i].append(frame_list[i+1][1])
            else:
                frame_list.remove(frame_list[i])

        frames = frame_list
        anim_sprite = ccAnimSprite()

        for i in range(len(frames)):
            sprite = sprites[int(frames[i][0])]
            time = int(frames[i][1][1:])
            next_frame = int(frames[i][2])
            anim_frame = ccAnimFrame(sprite, time, next_frame)
            anim_sprite.add_frame(anim_frame)

        ccSpriteManager.add_sprite(self.get_current_section_name(), anim_sprite)


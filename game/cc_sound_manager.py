from cc_resource_paths import ccResourcePaths
import pygame


class ccSoundManager:

    sounds = {}

    @classmethod
    def get_sound(cls, sound_name):
        sound = cls.sounds.get(sound_name)
        if sound:
            return sound
        ccLogger.error(sound_name + " not found.")
        return None

    @classmethod
    def add_sound(cls, sound_name, file_name):
        if sound_name in cls.sounds:
            ccLogger.warning(sound_name + " is already loaded.")
        else:
            print(ccResourcePaths.get_sfx() + file_name)
            cls.sounds[sound_name] = pygame.mixer.Sound(ccResourcePaths.get_sfx() + file_name)

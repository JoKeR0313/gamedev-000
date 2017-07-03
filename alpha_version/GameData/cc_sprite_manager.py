from GameData.cc_logger import ccLogger


class ccSpriteManager:

    textures = {}
    sprites = {}

    def __init__(cls):
        error = "ccSpriteManager is an abstract class, can't call __init__!"
        raise Exception(error)

    @classmethod
    def add_texture(cls, texture_name, texture):
        if texture_name in cls.textures:
            ccLogger.warning(texture_name + " is already loaded.")
        else:
            cls.textures[texture_name] = texture

    @classmethod
    def get_texture(cls, texture_name):
        texture = cls.textures.get(texture_name)
        if texture:
            return texture
        ccLogger.error(texture_name + " not found.")

    @classmethod
    def add_sprite(cls, sprite_name, sprite):
        if sprite_name in cls.sprites:
            ccLogger.warning(sprite_name + " is already loaded. It will not be overwritten.")
        else:
            cls.sprites[sprite_name] = sprite

    @classmethod
    def get_sprite(cls, sprite_name):
        sprite = cls.sprites.get(sprite_name)
        if sprite:
            return sprite
        ccLogger.error(sprite_name + " not found.")

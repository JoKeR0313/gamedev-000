from cc_logger import ccLogger


class ccSpriteManager:

    textures = {}
    sprites = {}

    def __init__(cls):
        stop_being_a_noob = "You cannot instantiate this class. Now go cry in the corner."
        raise Exception(stop_being_a_noob)

    @classmethod
    def add_texture(cls, texture_name, texture):
        # add the ccTexture to the textures dictionary, but only if it's not
        # already there (texture_name is the key). If it is there, don't add and
        # print a warning msg that says that we wanted to load it twice
        if texture_name in cls.textures:
            ccLogger.warning("ccTexture is already loaded.")
        else:
            cls.textures[texture_name] = texture

    @classmethod
    def get_texture(cls, texture_name):
        # give back the ccTexture. If it can't be found, write an error msg and return with None
        texture = cls.textures.get(texture_name)
        if texture:
            return texture
        else:
            ccLogger.error("ccTexture not found.")

    @classmethod
    def add_sprite(cls, sprite_name, sprite):
        # add ccSprite to sprites dictionary but only if it is not there
        # (sprite_name is the key). If it is there, print a warning msg and don't
        # overwrite the previous one
        if sprite_name in cls.sprites:
            ccLogger.warning("ccSprite is already loaded. It will not be overwritten.")
        else:
            cls.sprites[sprite_name] = sprite

    @classmethod
    def get_sprite(cls, sprite_name):
        # give back the ccSprite. If it can't be found, write an error msg and return with None
        sprite = cls.sprites.get(sprite_name)
        if sprite:
            return sprite
        else:
            ccLogger.error("ccSprite not found.")

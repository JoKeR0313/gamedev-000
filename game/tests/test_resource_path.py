import import_dir_setter
import cc_resource_paths


def test_resource_path():

    try:
        if cc_resource_paths.ccResourcePaths.get_resources().find("/game/resources") == -1:
            raise Exception
        if cc_resource_paths.ccResourcePaths.get_objects().find("/game/resources/objects") == -1:
            raise Exception
        if cc_resource_paths.ccResourcePaths.get_sprites().find("/game/resources/sprites") == -1:
            raise Exception
        if cc_resource_paths.ccResourcePaths.get_anims().find("/game/resources/anims") == -1:
            raise Exception
        if cc_resource_paths.ccResourcePaths.get_textures().find("/game/resources/textures") == -1:
            raise Exception
        if cc_resource_paths.ccResourcePaths.get_object_scenes().find("/game/resources/object_scenes") == -1:
            raise Exception
        if cc_resource_paths.ccResourcePaths.get_acts().find("/game/resources/acts") == -1:
            raise Exception
    except TypeError:
        pass


if '__main__' == __name__:
    test_resource_path()

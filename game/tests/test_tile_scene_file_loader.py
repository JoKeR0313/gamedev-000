import import_dir_setter
from cc_tile_scene_file_loader import ccTileSceneFileLoader
from cc_resource_paths import ccResourcePaths


def TestTileSceneLoader():
    loader = ccTileSceneFileLoader()
    loader.process_file(ccResourcePaths.get_tile_scenes() + "test.tilescene.json")
    print("Obj dict: ", loader.objects_dict)
    print("map: ", loader.map)


TestTileSceneLoader()

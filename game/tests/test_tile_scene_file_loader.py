import import_dir_setter
from cc_tile_scene_file_loader import ccTileSceneFileLoader

from cc_tile_map_scene import ccTileMapScene


def TestTileSceneLoader():
    loader = ccTileSceneFileLoader()
    loader.process_file("test.tilescene.json")
    print("gdasvd", loader.objects_dict)
    print("map: ", loader.map)


TestTileSceneLoader()

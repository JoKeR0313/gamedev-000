import import_dir_setter
from cc_tile_scene_file_loader import ccTileSceneFileLoader

def TestTileSceneLoader():
    loader = ccTileSceneFileLoader()
    loader.process_file("test.tilescene.json")
    print(loader.objects_dict)
    print(loader.map)

TestTileSceneLoader()
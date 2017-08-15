import pygame
from GameData.cc_object_scene import ccObjectScene
from GameData.cc_tile_map_scene import ccTileMapScene


class ccCollisionDetector:
    @classmethod
    def update(cls, scenes):
        for i in range(len(scenes) - 1, -1, -1):
            if issubclass(type(scenes[i]), ccObjectScene):
                ccCollisionDetector.update_object_scene(scenes, i)
           # i'm not sure we are needing tilemap-tilemap or tilemap-objectScene collision checks
           # elif issubclass(type(scenes[i]), ccTileMapScene):
           #     ccCollisionDetector.update_tilemap_scene(scenes, i)

    @classmethod
    def update_object_scene(cls, scenes, i):
        for current_obj in scenes[i].object_list:
            if current_obj.hitbox is not None:
                for j in range(i - 1, 0, -1):
                    if issubclass(type(scenes[j]), ccObjectScene):
                        ccCollisionDetector.object_scene_collision(scenes, j, current_obj)
                    elif issubclass(type(scenes[j]), ccTileMapScene):
                        ccCollisionDetector.tilemap_scene_collision(scenes, j, current_obj)

    @classmethod
    def object_scene_collision(cls, scenes, j, current_obj):
        for obj in scenes[j].object_list:
            ccCollisionDetector.object_collision(current_obj, obj)

    @classmethod
    def tilemap_scene_collision(cls, scenes, j, current_obj):
        for m in range(len(scenes[j].map)):
            for obj in scenes[j].map[m]:
                ccCollisionDetector.object_collision(current_obj, obj)

    @classmethod
    def object_collision(cls, current_obj, obj):
        if obj.hitbox is not None:
            if current_obj.hitbox.colliderect(obj.hitbox):
                current_obj.objecthit(obj)
                obj.objecthit(current_obj)

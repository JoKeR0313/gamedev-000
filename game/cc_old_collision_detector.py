import pygame
from cc_object_scene import ccObjectScene
from cc_tile_map_scene import ccTileMapScene

"""
update(list of scenes (cls.scene)):
first scene first obj if hitbox is not None: 
if collide anything:
object.objecthit()

for range(scene)
"""


class ccCollisionDetector:

    @classmethod
    def update(cls, scenes):
        for i in range(len(scenes)):
            if issubclass(type(scenes[i]), ccObjectScene):
                for current_obj in scenes[i].object_list:
                    if current_obj.hitbox is not None:
                        if i <= len(scenes):
                            for j in range(i + 1, len(scenes)):
                                if issubclass(type(scenes[j]), ccObjectScene):
                                    for obj in scenes[j].object_list:
                                        if obj.hitbox is not None:
                                            if current_obj.hitbox.colliderect(obj.hitbox):
                                                current_obj.objecthit(obj)
                                                obj.objecthit(current_obj)

                                if issubclass(type(scenes[j]), ccTileMapScene):
                                    for m in range(len(scenes[i].map)):
                                        for obj in scenes[j].map[m]:
                                            if obj.hitbox is not None:
                                                if current_obj.hitbox.colliderect(obj.hitbox):
                                                    current_obj.objecthit(obj)
                                                    obj.objecthit(current_obj)

            if issubclass(type(scenes[i]), ccTileMapScene):
                for m in range(len(scenes[i].map)):
                    for current_obj in scenes[i].map[m]:
                        if current_obj.hitbox is not None:
                            for j in range(i + 1, len(scenes)):

                                if issubclass(type(scenes[j]), ccObjectScene):
                                    for obj in scenes[j].object_list:
                                        if obj.hitbox is not None:
                                            if current_obj.hitbox.colliderect(obj.hitbox):
                                                current_obj.objecthit(obj)
                                                obj.objecthit(current_obj)

                                if issubclass(type(scenes[j]), ccTileMapScene):
                                    for m in range(len(scenes[i].map)):
                                        for obj in scenes[j].map[m]:
                                            if obj.hitbox is not None:
                                                if current_obj.hitbox.colliderect(obj.hitbox):
                                                    current_obj.objecthit(obj)
                                                    obj.objecthit(current_obj)

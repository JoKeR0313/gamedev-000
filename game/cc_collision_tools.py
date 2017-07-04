import pygame


# This is an abstract class!!!

class ccCollisionTools:

    @staticmethod
    def update_object_hitbox(obj):
        obj.hitbox.x = obj.position.x
        obj.hitbox.y = obj.position.y

    @staticmethod
    def update_list_hitbox(object_list):
        print("start")
        for obj in object_list:
            if obj.hitbox is not None:
                print("hello")
                obj.hitbox.x = obj.position.x
                obj.hitbox.y = obj.position.y

    @staticmethod
    def check_collsion_between_objects(left_obj, right_obj):
        if left_obj.hitbox.colliderect(right_obj.hitbox):
            return True

    @staticmethod
    def check_list_collision(object_list):
        for obj in object_list:
            if obj.hitbox is not None:
                for check_obj in object_list:
                    if check_obj.hitbox is not None:
                        if obj != check_obj:
                            if obj.hitbox.colliderect(check_obj.hitbox):
                                return True

    @staticmethod
    def check_collision_between_lists(left_object_list, right_object_list):
        for left_obj in left_object_list:
            if left_obj.hitbox is not None:
                for right_obj in right_object_list:
                    if right_obj.hitbox is not None:
                        if left_obj.hitbox.colliderect(right_obj.hitbox):
                            return True



from cc_collision_tools import ccCollisionTools


class BouncingBallCollisionDetector(ccCollisionTools):

    @staticmethod
    def check_list_collision(object_list):
        for obj in object_list:
            if obj.hitbox is not None:
                for check_obj in object_list:
                    if check_obj.hitbox is not None:
                        if obj != check_obj:
                            if obj.hitbox.colliderect(check_obj.hitbox):
                                obj.velocity.x = -obj.velocity.x
                                obj.velocity.y = -obj.velocity.y

import pygame


class ccKeyEventHandler:

    def step(self, time_passed):
        pressed = pygame.key.get_pressed()
        for obj in self.object_list:
            obj.step(time_passed)
            if obj.id == 200:
                obj_tomove = obj
                if pressed[pygame.K_LEFT]:
                    print("LEFT")
                    # obj_tomove.position[0] -= 1
                    # self.update_obj_tomove()
                    # if self.collision_check():
                    #     obj_tomove.position[0] += 1
                if pressed[pygame.K_RIGHT]:
                    print("RIGHT")
                    # obj_tomove.position[0] += 1
                    # self.update_obj_tomove()
                    # if self.collision_check():
                    #     obj_tomove.position[0] -= 1
                if pressed[pygame.K_UP]:
                    print("UP")
                    # obj_tomove.position[1] -= 1
                    # self.update_obj_tomove()
                    # if self.collision_check():
                    #     obj_tomove.position[1] += 1
                if pressed[pygame.K_DOWN]:
                    print("DOWN")
                    # obj.position[1] += 1
                    # self.update_obj_tomove()
                    # if self.collision_check():
                    #     obj_tomove.position[1] -=
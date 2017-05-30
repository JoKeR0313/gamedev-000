import pygame

from cc_globals import ccGlobals


class ccKeyEventActions:

    def draw(self):
        for obj in self.object_list:
            obj.draw(ccGlobals.get_renderer())

    def step(self, time_passed):

        for obj in self.object_list:
            obj.step(time_passed)
            binded_object = obj
            if pressed[pygame.K_LEFT]:
                binded_object.position[0] -= 1
                self.update_binded_object()
                if self.collision_check():
                    binded_object.position[0] += 1
            if pressed[pygame.K_RIGHT]:
                binded_object.position[0] += 1
                self.update_binded_object()
                if self.collision_check():
                    binded_object.position[0] -= 1
            if pressed[pygame.K_UP]:
                binded_object.position[1] -= 1
                self.update_binded_object()
                if self.collision_check():
                    binded_object.position[1] += 1
            if pressed[pygame.K_DOWN]:
                obj.position[1] += 1
                self.update_binded_object()
                if self.collision_check():
                    binded_object.position[1] -= 1

    def get_binded_object(self):
        for obj in self.object_list:
            if obj.id == 200:
                binded_object = copy.deepcopy(obj.active_sprite.rectangle)
                binded_object.x = obj.position.x
                binded_object.y = obj.position.y
                return binded_object

    def update_binded_object(self):
        for obj in self.object_list:
            if obj.id == 200:
                self.binded_object.x = obj.position.x
                self.binded_object.y = obj.position.y

    def collision_check(self):
        for rect in self.rect_list:
            if self.binded_object.colliderect(rect):
                return True

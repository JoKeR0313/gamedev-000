from cc_object_scene import ccObjectScene
from cc_object_scene_file_loader import ccObjectSceneFileLoader
from cc_globals import ccGlobals
import pygame
from pprint import pprint
import copy


class ccCollisionObjectScene(ccObjectScene):
    def __init__(self):
        super().__init__()
        self.object_list = []
        self.type = "ccCollisionObjectScene"
        self.obstacles = []  # A deepcopy of the object_list for collision checking

    def load(self, filename):
        loader = ccObjectSceneFileLoader()
        loader.process_file(filename)
        self.object_list = loader.get_objects()
        self.obstacles = self.load_obstacles()

    def draw(self):
        for obj in self.object_list:
            obj.draw(ccGlobals.get_renderer())

    def step(self, time_passed):
        pressed = pygame.key.get_pressed()
        for obj in self.object_list:
            obj.step(time_passed)
            if obj.id == 200:
                player = obj
                if pressed[pygame.K_LEFT]:
                    player.position[0] -= 1
                    self.collision_check(player, "left")
                if pressed[pygame.K_RIGHT]:
                    player.position[0] += 1
                    self.collision_check(player, "right")
                if pressed[pygame.K_UP]:
                    player.position[1] -= 1
                    self.collision_check(player, "up")
                if pressed[pygame.K_DOWN]:
                    obj.position[1] += 1
                    self.collision_check(player, "down")

    def load_obstacles(self):
        """Function that returns a deepcopy of the scene's object list, exluding the player object.
        This step is needed because if the player object is in the list, then the collision
        detection always returns true, because we are checking if the player is colliding
        with itself."""

        obstacles = copy.deepcopy(self.object_list)
        for obj in obstacles:
            if obj.id == 200:  # The object with the id of 200 will be the movable player object
                obstacles.remove(obj)
        return obstacles

    def collision_check(self, player, direction):
        """This function checks if any object in the obstacles list is colliding with
        the player object. It uses pygame's rect.colliderect method. Currently it isn't
        working properly.
        The good news is the check didn' drop any exceptions which means it runs alright.
        The bad news is that it always returns false.
        My wild guess: the problem is that the object's sprite's rectangle
        (which is a pygame Rect object) not defined properly. The x and y position coordinates
        are 0 on every object's rectangles. I think these attributes have to be implemented from the
        object's similary named attributes. Also they needed to be upgraded on every step,
        if the object is moving on the game screen.
        The lots of prints in this method is for testing of course."""

        print("##########################################################")
        print("STARTING COLLISION CHECK FOR ", direction.upper(), " DIRECTION!")
        print("-----------------------------------------")
        print("player object and rectangle coordinates")
        print("player rectangle: ", player.active_sprite.rectangle)
        print("player position: ", player.position)
        print("-----------------------------------------")

        x = 0
        for obj in self.obstacles:

            print("-----------------------------------------")
            print(x, ". obstacle object and rectangle coordinates")
            print("obstacle rectangle: ", obj.active_sprite.rectangle)
            print("obstacle position: ", obj.position)
            print("-----------------------------------------")

            if player.active_sprite.rectangle.colliderect(obj.active_sprite.rectangle):
                print(direction + ": collision true")
            else:
                print(direction + ": collision false")
            x += 1

        print("ENDING COLLISION CHECK FOR ", direction.upper(), " DIRECTION!")
        print("##########################################################")

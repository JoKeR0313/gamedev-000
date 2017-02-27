# TODO
# Important
## * when I say print error/warning/trace msg, I mean to use the Logger class! *

## ccLogger
- when I say print error/warning/trace msg, I mean to use the Logger class!
- a simple logger class. First it calls print() and than also logs to file
- static class because it's needed everywhere

    ### Skeleton
        class ccLogger:
            filename = "" #"logs/sci-fi_game_" + a timestamp from the time module + ".log", so the filename will be different every time we start the game
            def __init__(self):
                #raise an exception (I know we usually don't raise execptions in init but this is an exceptional case :) and also print an error msg to Terminal
                pass
            @classmethod
            def error(cls, *args):
                #call print() but start with a timestamp and !E! and put the msg after. Also open the file and write the same line into it. An error msg would be something like this:
                #2017.02.25.19:23:00 !E! Texture not found: flying saucer.png
                pass
            @classmethod
            def warning(cls, *args):
                #same as error but with !W!
                pass
            @classmethod
            def trace(cls, *args):
                #same as error but with !T! and don't print it out, only write it to the file!
                pass


## ccFileLoader
- ccFileLoader class to parse JSON files. It is needed to decorate the JSON loader so we can use another format if we need to. Pick a JSON loader module what can parse JSON files, a simple one will do
- abstract class

    ### Skeleton:
        class ccFileLoader:
            def __init__(self):
                # init. Use it if you need it
                self.current_section=""
                pass
            def process_file(self, filename):
                #raise an exception that this is an abstract class
                pass
            def load_file(self, filename):
                #make the json loading here and set an instance variable what will hold the json reader and can be accessed from now on
                pass
            def get_section(self, section_name, mandatory=True):
                #give back the named section. If it doesn't exists, send back None and if mandatory is True, print an error msg. If the file is not loaded, print out an error msg and send back None
                pass
            def get_field(self, field_name, mandatory=True, section_name=current_section):
                #give back the field data. If it doesn't exists, send back None and if mandatory is True, print an error msg. If the file is not loaded, print out an error msg and send back None. section_name is optional, set the current_section if not given. If current_section is invalid, write an error msg and send back None
                pass
            def set_section(self, section_name):
                #set self.current_section to the section_name. print error if it doesn't exists, or file is not loaded.
                pass
            def set_first_section(self):
                #set self.current_section to the first section in the file. print error if no file loaded or file doesn't have a single section
                pass
            def next_section(self):
                #if self.current_section is set, set the next section. Return true if there is a next section and False if there is no next section. print error msg if self.current_section is not set and return False
                pass
      
## ccSpritesFileLoader
- processes the sprites files and puts the instanced ccSprites to the ccSpriteManager
- inherits from ccFileLoader
- check the game\resources\sprites\test.sprites.json file to see how it's looking like

    ### Skeleton
        class ccSpritesFileLoader(ccFileLoader):
            def __init__(self):
                pass
            def process_file(self, filename):
                #load the file with the json reader(use load_file() from ancestor). 
                #If error happens, abort loading and print error msg.
                #If a sprites file was loaded before, release that file and initialize
                #before loading the new file. Go through all the sections. 
				#First process the 'Config' section, and process the sprites after Config was processed. 
				#Make as much private methods as you like and don't violate the single responsibility principle. 
				#In the Config section, read the name of the image file and add it to SpriteManager as a ccTexture 
				#(use the filename as the texture name when adding). 
				#Store the filename and when creating the sprites, use it to get the texture from SpriteManager
                pass
				#if there is a "num_of_sprites" field, it means you have to load more than one sprite, starting from
				#the offset_x, offset_y, using the provided width,height for all of them. Handle the case, when you reach the
				#width of the texture! Continue with the next row in this case.

## ccTexture
- load the image file from disk and store it in a pygame Surface type

    ### Skeleton
        class ccTexture:
            def __init__(self):
                pass
            def load_image(self, file_name):
                #load the image as a pygame.Surface and store it
                pass
            def get_witdh(self):
                #give back loaded texture's width. print error if no texture is loaded and give back 0
                pass
            def get_height(self):
                #give back loaded texture's height. print error if no texture is loaded and give back 0
                pass
            def get_texture(self):
                #give back the texture stored. If no texture, give back None and print error msg

## ccSprite
- a sprite renders a quad from a ccTexture to screen when called

    ### Skeleton
        class ccSprite:
            def __init__(self, texture, rectangle):
                #needs an instance variable what stores the width, height and x,y offset. Probably a pygame.Rect type. Store the texture parameter also in an instance variable
                pass
            def draw(self, x, y):
                #draw the sprite to screen with pygame. Draw only the sprite from the texture to x,y position
                pass

## ccObjectProps
- settings for objects: object visible, object enabled
- a simple class with some enums or bitfields or something what handles on/off values efficiently

## ccObject
- very basic object type abstract class. Has type variable, id, object properties, sprite
- it's abstract because we will make a special object class for tiles and this class will be it's ancestor (and this class is the ancestor of other types of objects also)

    ### Skeleton
        class ccObjectBase:
            def __init__(self):
                # initialize instance variables
                self.type = 'ccObjectBase' #not sure this will be needed because python has type() function
                self.idTag = 0
                self.active_sprite = None
                self.object_props = ccObjectProps()
            def load(self, obj_file_loader):
                #receives a ccObjectsFileLoader what already has the file which contains the info for this object and it's current_section is set to this object. Loads all the data from it EXCEPT the active_sprite. Check out test.objects.json for the fields.
            def draw(self):
                # raise an exception that this is an abstract class
    
## ccBasicObject
- inherits from ccObject, loads the sprite and has drawing method, not abstract
- has position variable

    ### Skeleton
        class ccBasicObject(ccObject):
            def __init__(self):
                #call the ancestor's __init__()
                self.type = "ccBasicObject" #probably should use python's type(), so set that up with magic method(?)
                self.position = pygame.math.Vector2(0,0) #use Vector2. It should be able to store float values
                self.velocity = pygame.math.Vector2(0,0)
            def load(self, obj_file_loader):
                #call ancestor's load() method and get the sprite from SpriteManager. If sprite is not found, print error and set active_sprite to None
                pass
            def draw(self):
                #draw the active_sprite to the screen, to self.position position
                pass
            def step(self, time_passed):
                #change Object's position with velocity. Specialized object classes will override this method and do other logic here also
                pass

## ccSpriteManager
- handles all the loaded sprites and textures. Keeps dictionary where the key is the name of the sprite and the value is the ccSprite. Should have a getter what gives back a pointer to a sprite (no copying)
- this class is static, won't be instantiated because we need it all the time while we are running our program

    ### Skeleton
        class ccSpriteManager:
            textures = {}
            sprites = {}
            def __init__(self):
                #raise an exception (I know we usually don't raise execptions in init but this is an exceptional case :) and also print an error msg
                pass
            @classmethod
            def add_texture(cls, texture_name, texture):
                #add the ccTexture to the textures dictionary, but only if it's not already there (texture_name is the key). If it is there, don't add and print a warning msg that says that we wanted to load it twice
                pass
            @classmethod
            def get_texture(cls, texture_name):
                #give back the ccTexture. If it can't be found, write an error msg and return with None
                pass
            @classmethod
            def add_sprite(cls, sprite_name, sprite):
                #add ccSprite to sprites dictionary but only if it is not there (sprite_name is the key). If it is there, print a warning msg and don't overwrite the previous one
                pass
            @classmethod
            def get_sprite(cls, sprite_name):
                #give back the ccSprite. If it can't be found, write an error msg and return with None
                pass

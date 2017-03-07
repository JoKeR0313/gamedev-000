from cc_object_file_loader import ccObjectFileLoader
from cc_object_props import ccObjectProps

class ccObject:

    def __init__(self):
        # initialize instance variables
        self.type = 'ccObject'  # not sure this will be needed because python has type() function
        self.idTag = 0
        self.active_sprite = None
        self.object_props = ccObjectProps()

    def load(self, obj_file_loader):

    # receives a ccObjectsFileLoader what already has the file which contains the info for this object and it's current_section is set to this object. Loads all the data from it EXCEPT the active_sprite. Check out test.objects.json for the fields.
    def draw(self):

    # raise an exception that this is an abstract class
import import_dir_setter
from cc_object import *
from cc_basic_object import *
from cc_file_loader import *
from cc_object_props import *
from cc_objects_file_loader import *

def test_cc_object_create():
    obj = ccObject()
    try:
        if not obj.id and not obj.active_sprite and isinstance(obj.object_props, ccObjectProps):
            print("ccObject creation works!")
    except:
        print("Something off with creating ccObject instance!")

def test_cc_object_load():
    obj = ccObject()
    obj_file_loader = ccObjectsFileLoader()
    obj_file_loader.process_file('../resources/objects/test.objects.json')
    obj.load(obj_file_loader)
    try:
        if obj.visible and obj.enabled:
            print(" OK! ccObject.load function works!")
    except:
        print("FAIL! Something off with ccObject.load function!")

def test_cc_object_draw():
    obj = ccObject()
    try:
        obj.draw()
        print(" FAIL! The draw function didn't raise a proper error!")
    except:
        print(" OK! The ccObject draw function raise a proper error!")

def test_basic_obj_init():
    b_obj = ccBasicObject()
    if b_obj.type and not b_obj.position and b_obj.velocity == [0, 0] and b_obj.position == b_obj.velocity:
        print (" OK! ccBasicObject init works as expected! ")
    else:
        print ("FAIL! ccBasicObject can't be created properly!")

if __name__ == '__main__':
    test_cc_object_load()
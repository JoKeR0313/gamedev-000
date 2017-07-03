import json
from collections import OrderedDict
from GameData.cc_logger import *
from GameData.cc_resource_paths import *


class ccFileLoader:

    def __init__(self):
        self.current_section_id = None
        self.current_section = None
        self.current_dict = {}

    def process_file(self, filename):
        raise NotImplementedError("ccFileLoader is an abstract class, can't call __init__!")

    def load_file(self, filename):
        # make the json loading here and set an instance variable what will hold
        # the json reader and can be accessed from now on
        data = open(filename).read()
        self.current_dict = json.loads(data, object_pairs_hook=OrderedDict)

    def get_section(self, section_name, mandatory=True):
        # give back the named section. If it doesn't exists, send back None and if
        # mandatory is True, print an error msg. If the file is not loaded, print
        # out an error msg and send back None
        if not self.file_is_loaded():
            return None
        try:
            named_section = self.current_dict[section_name]
        except KeyError:
            if mandatory is True:
                print("Error: this section does not exist.")
            return None
        named_section = dict(OrderedDict(named_section))
        return named_section

    def get_field(self, field_name, mandatory=True, section_name=""):
        # give back the field data. If it doesn't exist, send back None and if
        # mandatory is True, print an error msg. If the file is not loaded, print
        # out an error msg and send back None. section_name is optional, set the
        # current_section if not given. If current_section is invalid, write an
        # error msg and send back None
        if not self.file_is_loaded():
            return None
        try:
            if section_name == "":
                section = self.current_section
            else:
                section = self.get_section(section_name, True)
            field_data = section[field_name]
        except KeyError:
            if mandatory is True:
                print("Error: this field does not exist.")
            return None
        except NameError:
            if mandatory is True:
                print("Error: invalid current_section.")
            return None
        return field_data

    def set_section(self, section_name):
        # set self.current_section to the section_name. print error if it doesn't exists, or file is not loaded.
        if self.file_is_loaded():
            i = 0
            for item in self.current_dict.items():
                i += 1
                if item[0] == section_name:
                    self.current_section = dict(OrderedDict(item[1]))
                    self.current_section_id = i - 1
                    break
            else:
                print("Error: the section does not exist.")

    def set_first_section(self):
        # set self.current_section to the first section in the file. print error
        # if no file loaded or file doesn't have a single section
        if self.file_is_loaded():
            first_section_list = (list(self.current_dict.items())[0])
            self.current_section = (dict(OrderedDict(first_section_list[1])))
            self.current_section_id = 0

    def next_section(self):
        # if self.current_section is set, set the next section. Return true if
        # there is a next section and False if there is no next section. print
        # error msg if self.current_section is not set and return False
        if self.current_section:
            try:
                first_section_list = (list(self.current_dict.items())[self.current_section_id + 1])
                self.current_section = (dict(OrderedDict(first_section_list[1])))
                self.current_section_id += 1
                return True
            except IndexError:
                print('Error: there are no more sections.')
                return False

    def file_is_loaded(self):
        if len(self.current_dict) == 0:
            print("Error: file is not loaded, or does not have any sections.")
            return False
        return True

    def get_current_section_name(self):
        return list(self.current_dict.items())[self.current_section_id][0]

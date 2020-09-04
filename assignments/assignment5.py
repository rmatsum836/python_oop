"""
Assignment 5: Build on previous assignment and write to a pickle object
instead of txt file

Create custom key error

Possible errors:
- if file doesn't exist
- Asking for a key that doesn't exist, list out the keys that are
  available "ConfigKeyError(self, key)"
"""

import os
import pickle

class ConfigDict(dict):
    # hardcode a directory path
    config_directory = '/Users/raymatsumoto/moocs/python_oop/assignments/configs'

    def __init__(self, config_name):
        self._full_path = os.path.join(ConfigDict.config_directory,
                config_name+'.pkl')
        if not os.path.isfile(self._full_path):
            with open(self._full_path, 'wb') as fh:
                pickle.dump(dict(self), fh)
        with open(self._full_path, 'rb') as fh:
            pkl = pickle.load(fh)
            self.update(pkl)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._full_path, 'wb') as fh:
            pickle.dump(dict(self), fh)

    def __getitem__(self, key):
        if key not in self:
            raise ConfigKeyError(self, key)
        return dict.__getitem__(self, key)

class ConfigKeyError(Exception):
    def __init__(self, dictionary, key):
        self.key = key
        self.keys = dictionary.keys()

    def __str__(self):
        error_msg = f"'{self.key}' does not exist.  The valid keys are: {', '.join(self.keys)}."

        return error_msg

if __name__ == '__main__':
    import sys

    cd = ConfigDict('configfile')

    # if 2 arguments on the command line,
    # set a key and value in the object's dictionary
    if len(sys.argv) == 3:
        key = sys.argv[1]
        value = sys.argv[2]
        print('writing data:  {0}, {1}'.format(key, value))
        cd[key] = value
    
    # if 1 argument on the command line, treat it as a key and show the value
    elif len(sys.argv) == 2:
        print('reading a value')
        key = sys.argv[1]
        print('the value for {0} is {1}'.format(sys.argv[1], cd[key]))
    
    # if no arguments on the command line, show all keys and values
    else:
        print('keys/values:')
        for key in cd.keys():
            print('   {0} = {1}'.format(key, cd[key]))

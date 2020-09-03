"""
Assignment 4: Trap errors a user may make

Create custom key error

Possible errors:
- if file doesn't exist
- Asking for a key that doesn't exist, list out the keys that are
  available "ConfigKeyError(self, key)"
"""

import os

class ConfigDict(dict):
    def __init__(self, filename):

        self._filename = filename
        if not os.path.isfile(self._filename):
            try:
                open(self._filename, 'w').close()
            except IOError:
                raise IOError("Invalid path given")
        with open(self._filename) as fh:
            for line in fh:
                line = line.rstrip()
                key, value = line.split('=', 1)
                dict.__setitem__(self, key, value)

    def __setitem__(self, key, value):

        dict.__setitem__(self, key, value)
        with open(self._filename, 'w') as fh:
            for key, val in self.items():
                fh.write('{0}={1}\n'.format(key, val))

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

    cd = ConfigDict('files/configfile.txt')

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

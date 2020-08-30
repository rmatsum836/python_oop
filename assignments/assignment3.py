import sys
import os

# Assignment 3

"""
Create a class that inherits from a dictionary.
But "getting" and "setting" values from a txt file.
Read in txt file and grab values

txt file looks like this:
sql_query=SELECT this FROM that WHERE condition
email_to=me@mydomain.com
"""

class ConfigDict(dict):
    def __init__(self, txt_file):
        self.txt_file = txt_file
        if os.path.isfile(self.txt_file):
            with open(self.txt_file, 'r') as fi:
                for line in fi:
                    line = line.rstrip()
                    line_split = line.split('=')
                    dict.__setitem__(self, line_split[0], line_split[1])

    def __setitem__(self, key, val):
        dict.__setitem__(self, key, val)
        
        with open(self.txt_file, 'w') as fo:
            for key, value in self.items():
                fo.write(f'{key}={value}\n')

if __name__ == '__main__':
    cd = ConfigDict('config_file.txt')

    if len(sys.argv) == 3:
        key = sys.argv[1]
        value = sys.argv[2]

        print('writing data: {0}, {1}'.format(key, value))
        cd[key] = value

    else:
        print('reading data')
        for key in cd.kys():
            print('    {0} = {1}'.format(key, cd[key]))

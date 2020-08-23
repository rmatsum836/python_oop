""" 
Assignment 2
Create two classes: "LogFile" and "DelimFile"
LogFile: Prints out log message to txt file
DelimFile: Prints list with delimiter

"""
import datetime
import abc

class WriteFile(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, filename, delimiter=None):
        self.filename = filename
        self.delimiter = delimiter

    @abc.abstractmethod
    def write(self, contents):
        with open(self.filename, 'a+') as fo:
            fo.write(f"{contents}\n")

class LogFile(WriteFile):
    def write(self, contents):
        dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        contents = f"{dt_str}\t{contents}"
        super(LogFile, self).write(contents)

class DelimFile(WriteFile):
    def write(self, contents):
        contents = f"{self.delimiter} ".join(contents)
        super(DelimFile, self).write(contents)

log = LogFile('log.txt')
c = DelimFile('text.csv', ',')
log.write('this is a log message')
log.write('this is another log message')

c.write(['a', 'b', 'c', 'd'])
c.write(['1', '2', '3', '4'])

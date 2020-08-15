""" 
Assignment 1
Create a class that acts like a list with a restrictions on it's length

push: Appends an element to a list
get_list: Gets the `lists` instance attribute

"""
class MaxSizeList(object):
    def __init__(self, maxsize):
        if isinstance(maxsize, int):
            self.maxsize = maxsize
        else:
            return TypeError("`maxsize` must be type(int)")
        self.lists = list()

    def push(self, element):
        """ Append an element to `lists` """
        if type(element) not in (str, float, int):
            return TypeError("Element added to maxlist must be of type int, str, or float")
        else:
            self.lists.append(element)
    
    def get_list(self):
        """ Get list based on specified maxsize """
        if len(self.lists) < self.maxsize:
            return ValueError("`maxsize` is greater than length of list")
        elif len(self.lists) == self.maxsize:
            return self.lists
        
        len_difference = len(self.lists) - self.maxsize
        for i in range(len_difference):
            self.lists.pop(0)

        return self.lists


a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())
print(b.get_list())
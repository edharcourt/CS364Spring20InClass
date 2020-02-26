
# Python's module system

# A python file can be used as a module and creates
# a namespace.  A namespace is a name for a set of
# names

import bar
from bar import name
# from bar import *  # BAD!!!!

if __name__ == "__main__":
    bar.f()
    print(bar.name)
    print(name)
"""

Reading
SOLID https://en.wikipedia.org/wiki/SOLID

MIXIN Classes https://en.wikipedia.org/wiki/Mixin
P. 747 glossary (Fluent Python)

collections.abc documentation
Chapters 1 - 3 in FP (through today)
Chapters 5 - 7, Next week
"""
from collections.abc import Sequence, Iterable, Iterator
#from collections.abc import List

if __name__ == "__main__":
    r = range(1,10)
    print(r,type(r))
    print(isinstance(r,list))
    print(isinstance(r,Iterable))
    print(isinstance(r,Iterator))
    i = iter(r)
    print(next(i))
    print(next(i))
    print(list(r)) # defeats range object purpose

    # The map function
    mo = map(lambda x:x*x, [1,2,3,4])
    print(type(mo))

    lst = [x*x for x in range(1,5)]

    # generator comprehension
    g = (x*x for x in range(1,5))
    print(type(g))
    print(next(g))

    # filter
    f = filter(lambda x: x % 2 == 0, [1,2,3,4])
    print(type(f))

    f1 = (x for x in [1,2,3,4] if x % 2 == 0)

    # dictionary
    d = dict()  # dictionary constructor, preferred
    d1 = {}

    # dictionary literal notation
    d = { "CS140" : "Intro", "CS220" : "Organization" }
    print(d["CS140"])

    d1 = {1 : "Hello"}

    d2 = {("Hello", "World"): "Whatever"}
    #d3 = {["Hello", "World"]: "Whatever"}
    #print(d3)

    # Lists are very general in Python
    from array import array

    # An array is a sequence of itemns of the sdame type
    # They are as fast as C arrays
    vec = array('i', [0]*1000)
    vec[0] = 900
    print(vec[0])

    # Heavy use of arrarys and numbers use the
    # the numpy library
    # used with matplotlib








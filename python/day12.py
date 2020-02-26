# 'C:\Users\ehar\AppData\Roaming\Python\Python37\Scripts'
# which is not on PATH.
# The PATH is the list of directories where the OS
# looks  for executables

"""
this is a
block comment
"""

lines = """
this is

a
 
 
 bunch                of stuff
"""

# Python is dynamically typed
# Don't declare type of variables
# The type of a variable is the type ofd the
# last value assigned to it. It can change at
# runtime

x = 77
print(x**2)
x = "Hello"

# Python invented by Guido van Rossum
# was the BDFL until last year. Benevolent
# Dictator for Life.
# Python is old 1991
# Machine Learning and AI
# numpy - numerical python
# pandas - data science library
# the number of libraries is enormous
# crypto

y : int = 6

# EVERYTHING IS AN OBJECT!
print(type(5))
print(isinstance(5,int))
print(5 + 6)
print(int.__add__(5,6))
print(None, type(None))  # None is False
print(True, type(True))
print(isinstance(True,bool))
print(isinstance(True,int))
print(True + True)
print(issubclass(bool,int))

# The reference implementation of python is called CPython
# Jython - Java implementation
# PyPy - python in python (JIT) just in time compiler
# Don't confuse CPYthon with Cython. Cython is way to
# interface C with Python

# lists?
lst = [1,2,3]    # '(1 2 3)

# lists are mutable
lst[0] = 99

# lists are generic
lst2 = [1, "Hello", 3.14]  # uncommon
lst3 = [[1,2,3],[4,5,6],[7,8,9]]  # matrix

# tuples - Two views of tuples
# 1) like a immutable lists
t1 = (1,2,3)   # tuples are immutable
#t1[0] = 99    error

# 2) Record - aggregates different kinds of data
student = ("Harry", "Potter", [3.5])
student[2][0] = 4.0
# student[0] = "Draco"   crash
print(student[2][0])
# tuples and lists are sequences (and strings are sequences)

print("Hello")   # indentation matters

# sequence3s can be iterated over with a for-loop
for ch in "Hello":
    print(ch,end="")
    # end is called a named parameter
    # ch is called a positional parameter

def f(x: int, y:int) -> None:
    print("x is", x)
    print("y is", y)

f(3,4)
f(y=3,x=4)

# error. named parameters must come after
# positional parameters
# f(y=3,4)
# f(4,x=3)  error y does not have a value

# dictionary
# Java, Map   HashMap, TreeMap
d = {}   # empty dictionary
d['CS364'] = "Programming Languages"
d['CS362'] = 'Algorithms'
print(d['CS364'])
print("Can't")
print('Can\'t')
print('She said "Hello"')


# *args variable length arguments list
# C is called varargs
# kwargs means keyword arguments where positional
# parameters are stored in a dictionary
def g(x, *args, **kwargs):
    print("g:", type(args))
    print("g: ", x)
    print("g:", args)
    print("g:", type(kwargs))
    print("g:", kwargs)

g(0)
g(1,2,3)
g(1,2,3,4,name="CS364",title="Programming Languages")

# parameter passing
# positional, named, positional variable (*args),
# named variable (kwargs)

# sets
s = set()  # s = {} empty dictionary
s = {1, 2, 3, 4}
print(type(s))

# sets are mutable
s = s.union({5,6,7,8})
print(s)

# immutable sets called frozenset
s1 = frozenset({1,2,3,4})
print(s1)

print(id(s1))  # id() gives the memory address for the object

# two references to the same object have the same id
lst = [1,2,3,4,5]
x = map(lambda x:x*x, lst)

# Pythonistas prefer list comprehensions over map and filter
y = [x*x for x in lst]



print(y)
print(list(x))
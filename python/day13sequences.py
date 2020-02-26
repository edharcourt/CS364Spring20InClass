
# Sequences; lists, tuples, strings

# List comprehensions

# [var-expr for var in expression]

# list of squares
lst = [x*x for x in range(10)]
print(lst)

# list of odd squares
lst2 = [x*x for x in range(1,10,2)]
print(lst2)

lst3 = [x*x for x in range(1,10) if x % 2 == 0]
print(lst3)

lst4 = [(x,y) for x in range(3) for y in range(2)]
print(lst4)

# open Moby Dick at T:/Harcourt/data/mobydick.txt

# A little bad style? Check if file exists
lines = open("T:/Harcourt/data/mobydick.txt").readlines()
print(len(lines))

words = [line.split() for line in lines]
low = []
for w in words:
    low += w         # __iadd__  (in place add)
    #low = low + w   # __add__
print(len(low))

# sorted returns a new list

# soprted uses the < operator BUT!
# The string (str) data type defines < by
# implementing __lt__

# sorted and sort are stable sorts, for equal items
# does not change their relative order
inorder = sorted(low, key=str.upper)

print(inorder[len(inorder) - 1])

# should not call dunders directly yourself
# except when writing complex classes that
# override lots of dunders
print(inorder[inorder.__len__() - 1])

# print the alphabetically greatest word
# lexicographically greatest word


# the sort method on lists modifies the
# list passed to it
#low.sort()

roster = [("Harry", 3.0), ("Ron", 2.01), ("Hermione", 4.0)]
print(sorted(roster, key=lambda x:x[0]))
print(sorted(roster, key=lambda x:x[1], reverse=True))

"""
>>> def f(x): return x*x - 33
...
>>> import dis
>>> dis.dis(f)
  1           0 LOAD_FAST                0 (x)
              2 LOAD_FAST                0 (x)
              4 BINARY_MULTIPLY
              6 LOAD_CONST               1 (33)
              8 BINARY_SUBTRACT
             10 RETURN_VALUE
>>>
"""
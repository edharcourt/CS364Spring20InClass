
# function returns None and has the side effect of
# printing a value
# The scope of c is the function f2c
# The scope of a variable is the region of the program where
# the name is visible.
def f2c(f:float) -> None:
    c = 5/9*(f - 32)
    print(c)

c = 0  # global variable

# f3c has a side effect of modify the global state (variable)
# f is passed by value. A copy of the argument is made in to
# the parameter f.
def f3c(f: float) -> None:
    global c
    c = 5/9*(f - 32)
    f = 99

def f(lst: list) -> None:
    lst[0] = 99


# has a side effect of modifying a
# pass by reference parameter
def f4c(f: list) -> None:
    c = 5/9*(f[0] - 32)
    f[0] = c

# Is a "good" function. Because it has no side effects.
# A function w/o side effects is called "pure".
# "Good" functions can be easily reused
# Pure functions represent values and can be used
# in expressions
def ftoc(f: float) -> float:
    return 5/9*(f - 32)

if __name__ == "__main__":
   f2c(32)
   f3c(32)
   print(f)
   print(c)

   l = [9,8,7]
   f(l)
   print(l)

   l = [32]
   f4c(l)
   print(l[0])

   print(ftoc(32)**.5 * 2 + 4)


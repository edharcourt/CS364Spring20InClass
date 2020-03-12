
def foo(x, y, z, key = None):
    print("DEBUG: foo called")
    # work work work
    print("I'm a foo {} {} {} {}".format(x,y,z,key))
    print("DEBUG: foo exiting")

def goo(x,y):
    print("I'm goo {} {}".format(x,y))
    return 42

# A decorator
from typing import Callable
def wrap(f):   # f is a Callable

    count = 0

    # create a new version of f
    def newf(*args, **kwargs):
        nonlocal count
        count += 1
        print("{}: DEBUG {} called".format(count, f.__name__))
        retval = f(*args,**kwargs)
        print("{}: DEBUG {} exiting".format(count, f.__name__))
        return retval

    return newf  # newf is a closure

# wrap is a decorator
@wrap
def moo():
    print("I'm moo")

# Create a timeit decorator
import time
def timeit(f):

    def newf(*args, **kwargs):
        start = time.perf_counter()
        retval = f(*args, **kwargs)
        end = time.perf_counter()
        print("Time: {}".format(end - start))
        return retval

    return newf

def quicksort(lst):
    if len(lst) == 0:
        return []

    pivot = lst[0]
    lt = [x for x in lst if x < pivot ]
    gt = [x for x in lst if x > pivot ]
    pivots = [x for x in lst if x == pivot ]
    return quicksort(lt) + pivots + quicksort(gt)

@timeit
def timed_sort(lst, sorting_strategy):
    l = sorting_strategy(lst)
    return l


import random
if __name__ == '__main__':
    test_vector = [random.randrange(100000) for _ in range(10000000)]
    print("Doh!")
    lst1 = timed_sort(test_vector, quicksort)
    lst =  timed_sort(test_vector, sorted)

    """
    moo()
    foo(1,2,3)
    newgoo = wrap(goo)
    print(newgoo(1,y=33))
    print(newgoo(2,y=34))
    print(newgoo(3,y=35))
    """
from typing import Callable, Union
from numbers import Real, Integral
from operator import *

RealOrInt = Union[Real, Integral]


def f(op: Callable[[RealOrInt, RealOrInt], RealOrInt], x:RealOrInt, y:RealOrInt):
    return op(x, y)


if __name__ == '__main__':
    print(add(3.14,5))

class Point:
    """
    This is called a docstring
    """

    # class data
    pi = 3.14159

    def __init__(self, x:float, y:float):
        """
        Always need to refer to self when referring
        to the instance of thew class, it is never
        implied like in Java or C++.
        """
        self._x = x   # instance variables
        self._y = y

    # instance method
    def dist(self, other):
        return ((self._x - other._x)**2 +
                (self._y - other._y)**2)**.5

    # static method decorator
    @staticmethod
    def dist2(p1, p2):
        return ((p1._x - p2._x)**2 +
               (p1._y - p2._y)**2)**.5

    def __str__(self):
        return "({0},{1})".format(self._x, self._y)

class ColoredPoint(Point):
    def __init__(self, x, y, color):
        super().__init__(x,y)
        self.color = color


class NPoint:
    """
    An N-dimension point, default to two dimensions
    """
    def __init__(self, x, y, *args):
        self.vals = [x,y]
        self.vals += list(args)

    def __str__(self):
        r = ""
        for v in self.vals:
            r += str(v) + ","
        return "({0})".format(r)

    def __repr__(self):
        """
        The repr() function is similar to str() except
        it is supposed to retuirn a valid string that can
        be used to reproduce the object in python
        :return:
        """
        return NPoint.__name__ + str(self)

    # implementing __len__ and __getitem__
    # turns the class in to a Sequence
    def __len__(self):
        return(len(self.vals))

    # override [] notation
    def __getitem__(self, idx):
        return self.vals[idx]

    def dist(self, other):
        """
        Compute the distance between self and other
        :param other:
        :return:
        """
        pass

"""
SOLID Principle

Single responsibility - a class should have one purpose
and do it well. Classes should not have extra unrelated
crud in them.

Open/closed - classes should be closed for modification
but open for extension

Liskov substitution - If S inherts T wherever I expect
a T and substitute an S

Interface segregation - prefer small (preferabley very small) 
interfaces rather than larger general purpose interfaces

Dependency Inversion - code to interfaces and not concrete 
implementations.  Code to thje most general base class interface
not specific implementations of the base class. For example
code to a Sequence if possible instead of a list or tuple.

"""


if __name__ == "__main__":
    p1 = Point(3,4)
    p2 = Point(6,7)

    print(p1.dist(p2))
    print(Point.dist(p1,p2))
    print(Point.dist2(p1,p2))
    print(str(p1))
    print(p1.__str__())   # not correct way

    p3 = NPoint(1,2,3,4,5)
    print(str(p3))
    print(repr(p3))

    print(len(p3))
    for v in p3:  # because p3 is a sequence
        print(v)

    # Liskob Substitution
    cp1 = ColoredPoint(2,3,(255,0,0))
    cp2 = ColoredPoint(4,5,(0,0,0))
    print(cp1.dist(cp2))


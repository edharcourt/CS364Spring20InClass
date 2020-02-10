"""
Compute the cartesian product of two sets.
"""
if __name__ == "__main__":

    set1 = {1, 2, 3, 4}
    set2 = {'a', 'b', 'c'}
    cp = set()

    # Version 1: Cartesian Product of set1 and set2
    for x in set1:
        for y in set2:
            cp.add((x,y))

    print(len(cp))

    # Version 2: set comprehensions
    cp2 = {(x,y) for x in set1 for y in set2}
    print(len(cp2))

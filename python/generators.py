
def greeting():
    print('Hello')
    print('World')

# countdown is a function that creates a generator
# generators remember where they "left off" so that
# the next time next() is called they start
# where they left off
def countdown():
    yield 5
    yield 4
    yield 3
    yield 2
    yield 1
    yield "blast off"

g = countdown()
print(type(g))
print(next(g))
print(next(g))

def counter():
    i = 0
    while True:
        yield i
        i = i + 1


c1 = counter()
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))



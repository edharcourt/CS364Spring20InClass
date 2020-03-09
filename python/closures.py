
# closure is a function and its environment

x = 0
def f():
    print(x)

# The closure of f is (f,x)

count = 0
def inc():
    global count
    count = count + 1
    return count

def make_counter():
    count = 0

    def g():
        nonlocal count
        count = count + 1
        return count
    return g

c1 = make_counter()
c2 = make_counter()
print(c1())
print(c1())
print(c2())

print(inc())
print(inc())
count = 33
print(inc())
from operator import add  # add is the function corresponding to +

df = { '+' : lambda x,y: x + y}
df = { '+' : add}

# Don't optimize prematurely  for both code length *and* runtime speed
# The process of consildating and cleaning up code, making it DRY and so forth
# is called "refactoring".     ax + ay = a(x+y)

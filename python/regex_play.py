# A file for messing around with regular expressions
import re

# test string
s = "apple the best thing about a boolean is that 0b101001 if you are wrong you are off by a bool"

patt = re.compile("bool")  # characters mathc themselves unless they are
                           # special metacharacters []

# [abc]   matches either a or b or c

mo = patt.search(s)   # searching s for the pattern

# mo - match object

print(mo.start(), mo.end())
print(mo.span())

# what if bool appeared more than once?
miter = patt.finditer(s)
for mo in miter:
    print(mo.span())

# star operator - means zero or more
patt = re.compile("b.*t")   # . matches any character
                           # * is greedy, matches as large a string as it can

miter = patt.finditer(s)
for mo in miter:
    print(mo.span())

# search for a binary number
patt = re.compile('0b[01][01]*')   # 0b
miter = patt.finditer(s)
for mo in miter:
    print(mo.span(),s[mo.start():mo.end()])

# + operator mean one or more
patt = re.compile('0b[01]+')  # 0b followed by one or more 0 or 1

# | - or operator
patt = re.compile('(thing)|(wrong)')
miter = patt.finditer(s)
for mo in miter:
    print(mo.span(), s[mo.start():mo.end()])

patt = re.compile('0b(1|0)+')

# ^ - start of the string
patt = re.compile('^apple') # does this start with apple

mo = patt.search(s)
if mo is not None:
    print("DEBUG", mo.span())
else:
    print("Match not found")

# $ - end with
patt = re.compile('bool$')   # match an ending bool
mo = patt.search(s)
if mo is not None:
    print("DEBUG", mo.span())
else:
    print("Match not found")

"""
library of regular expression metaharacters

[] - character class match one of a set of characters
* - zero or more
+ - one or more
| - or, match one of the other
^ - starts with
$ - ends with operator



"""

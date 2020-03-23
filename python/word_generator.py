from typing import Generator
import re

def word_generator(fn: str) -> Generator[str,None,None]:

    try:
        f = open(fn)
    except OSError as e:
        print("Cannot open file {}".format(fn))
        return None

    split_patt = re.compile('[\\s.,!\()\-;:"]')

    for line in f:
        words = (w for w in split_patt.split(line) if w)

        for w in words:
            yield w

if __name__ == "__main__":
    wg = word_generator('word_generator.py')

    while True:
        try:
            print(next(wg))
        except StopIteration as e:
            break

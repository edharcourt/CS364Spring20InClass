# and index is a dictionary where the key
# is the word and the values is a list of line numbers

from typing import Set, Union, Optional, Dict, List
import re  # regular expression

def load_stopwords() -> Optional[Set[str]]:
    try:
        f = open("stopwords.txt")
    except OSError as e:
        print("Error: file stopwords.txt cannot be opened")
        return None

    # set comprehension
    return { w.strip() for w in f.readlines() }


def create_index(fn: str) -> Optional[Dict[str, List[int]]]:
    try:
        f = open(fn)
    except OSError as e:
        print("Error: could not open file {}".format(fn))
        return None

    s: Optional[Set[str]] = load_stopwords()
    if s is None:
        return None

    index = dict()
    split_patt = re.compile('[\s.,!\-();:"]')
    count = 0

    # iterate through the lines
    for line in f:
        count += 1
        words = [w.lower() for w in split_patt.split(line) if w ]

        for w in words:
            # TODO - check for word on line twice
            if w not in s:
                index.setdefault(w.lower(),[]).append(count)
    return index


if __name__ == "__main__":

    index = create_index("mobydick.txt")
    print(index['whenever'])

    # EXERCISE: Find the longest word
    longest = max(index.keys(), key=len)

    # EXERCISE: How many times does
    # the most frequent word appear
    most = len(max(index.values(), key=len))
    print(most)

    # EXERCISE: What word is it?
    t = max([(k,len(v)) for (k,v) in index.items()], key=lambda x:x[1])
    print(t)
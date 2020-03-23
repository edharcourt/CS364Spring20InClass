import sys
from typing import Generator, Tuple
import re


class Lexer:

    # class variables
    INTLIT = 0  # codes for the "kind" of value
    PLUS   = 1
    ID     = 2

    # fn - file name we are lexing
    def __init__(self, fn:str):

        try:
            self.f = open(fn)
        except IOError:
            print("File {} not found".format(fn))
            print("Exiting")
            # what should we do here?
            sys.exit(1)  # can't go on

    def token_generator(self) -> Generator[Tuple[int,str], None, None]:
        """
        Returns tokens of the language
        """

        split_patt = re.compile("(\+)|\s")  # parentheses around a pattern
                                            # captures the value

        # pick up here on Wednesday and process a SLU C file line by line
        # and yield the tokens.

        # capture group

if __name__ == "__main__":

    lex = Lexer("test.sluc")
    # how do we know file was opened?



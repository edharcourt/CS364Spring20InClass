from lexer import Lexer
from ast import Expr

class Parser:

    def __init__(self, fn: str):

        self.lex = Lexer(fn)
        self.tg = self.lex.token_generator()
        self.currtok = next(self.tg)

    """
        Expr  →  Term { + Term }
        Term  → Fact { * Fact }
        Fact  → [ - ] Primary
        Primary  → ID | INTLIT | ( Expr )
        
        Recursive descent parser. Each non-terminal corresponds 
        to a function.
        
        -7  -(7 * 5)  -b   unary minus
    """

    def expr(self) -> Expr:
        left = self.term()
        # finish this next time

    def term(self) -> Expr:
        pass

    def fact(self) -> Expr:
        pass

    def primary(self) -> Expr:
        pass
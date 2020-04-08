"""
SLU-C Abstract Syntax Trees

An abstract syntax tree (AST) is a data structure that represents
the concrete (text) syntax of a program
"""

class Expr:
    pass

# TODO Don't just cut-and-paste new operations, abstract!

class AddExpr(Expr):
    def __init__(self, left: Expr, right: Expr):
        self.left = left
        self.right = right

    def __str__(self):
        return "({0} + {1})".format(str(self.left), str(self.right))

class MultExpr(Expr):
    def __init__(self, left: Expr, right: Expr):
        self.left = left
        self.right = right

    def __str__(self):
        return "({0} * {1})".format(str(self.left), str(self.right))


class UnaryMinus(Expr):
    def __init__(self, tree: Expr):
        self.tree = tree

    def __str__(self):
        return "-{0}".format(str(self.tree))

class IDExpr(Expr):

    def __init__(self, id: str):
        self.id = id

    def __str__(self):
        return self.id

class IntLitExpr(Expr):

    def __init__(self, intlit: str):
        self.intlit = int(intlit)

    def __str__(self):
        return str(self.intlit)

if __name__ == '__main__':
    """
    Represent a + b + c * d
    ((a + b) + (c * d))
    """
    expr = AddExpr(AddExpr(IDExpr('a'), IDExpr('b')),
                   MultExpr(IDExpr('c'), IDExpr('d')))
    print(expr)

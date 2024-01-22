from antlr4 import *
from gen.ExprLexer import ExprLexer
from gen.ExprParser import ExprParser
from gen.ExprVisitor import ExprVisitor
from gp.BiggerGP import BiggerGP


def fitness_function(program):
    try:
        lexer = ExprLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        visitor = ExprVisitor()
        output = visitor.visit(tree)
        #print("Output: ", output)
        if 1 in output:
            return 0
        else:
            return -10*abs(min(output)+1)
    except Exception as e:
        #print(e)
        return -1000


if __name__ == '__main__':
    gp = BiggerGP()
    gp.evolve(fitness_function)

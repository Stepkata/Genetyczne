from antlr4 import *
from gen.ExprLexer import ExprLexer
from gen.ExprParser import ExprParser
from gen.ExprVisitor import ExprVisitor


def main(filename):
    input_stream = FileStream(filename)
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()
    visitor = ExprVisitor()
    output = visitor.visit(tree)
    print(output)
    print( 1 in output)
    print(1 in [-2.032727272727479, 1])


if __name__ == '__main__':
    main("program.txt")

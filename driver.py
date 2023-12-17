import sys
from antlr4 import *
from gen.ExprLexer import ExprLexer
from gen.ExprParser import ExprParser


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.start_()


if __name__ == '__main__':
    main(sys.argv)

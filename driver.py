from antlr4 import *
from gen.ExprLexer import ExprLexer
from gen.ExprParser import ExprParser
from gen.ExprVisitor import ExprVisitor


def main(filename):
    input_stream = FileStream(filename)
    lexer = ExprLexer(InputStream("print ( 860 ) .\n\n."))
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()
    visitor = ExprVisitor()
    output = visitor.visit(tree)
    print(output)


if __name__ == '__main__':
    main("program.txt")

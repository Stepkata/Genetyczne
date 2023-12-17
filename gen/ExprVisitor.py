# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx:ExprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expr.
    def visitExpr(self, ctx:ExprParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#variable_assign.
    def visitVariable_assign(self, ctx:ExprParser.Variable_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#print.
    def visitPrint(self, ctx:ExprParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#operators.
    def visitOperators(self, ctx:ExprParser.OperatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#logic_operators.
    def visitLogic_operators(self, ctx:ExprParser.Logic_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#literals.
    def visitLiterals(self, ctx:ExprParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#comparisson_type.
    def visitComparisson_type(self, ctx:ExprParser.Comparisson_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#if_statement.
    def visitIf_statement(self, ctx:ExprParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#condition.
    def visitCondition(self, ctx:ExprParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#while.
    def visitWhile(self, ctx:ExprParser.WhileContext):
        return self.visitChildren(ctx)



del ExprParser
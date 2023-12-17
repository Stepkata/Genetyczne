# Generated from C:/Users/keste/PycharmProjects/Genetyczne/Expr.g4 by ANTLR 4.13.1
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


    # Visit a parse tree produced by ExprParser#variable.
    def visitVariable(self, ctx:ExprParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#variable_declaration.
    def visitVariable_declaration(self, ctx:ExprParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#variable_assign.
    def visitVariable_assign(self, ctx:ExprParser.Variable_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parameter.
    def visitParameter(self, ctx:ExprParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#operators.
    def visitOperators(self, ctx:ExprParser.OperatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#logic_operators.
    def visitLogic_operators(self, ctx:ExprParser.Logic_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#numeric_literals.
    def visitNumeric_literals(self, ctx:ExprParser.Numeric_literalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#text_type.
    def visitText_type(self, ctx:ExprParser.Text_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#numeric_type.
    def visitNumeric_type(self, ctx:ExprParser.Numeric_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#literals.
    def visitLiterals(self, ctx:ExprParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#comparisson_type.
    def visitComparisson_type(self, ctx:ExprParser.Comparisson_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#typ.
    def visitTyp(self, ctx:ExprParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#if_statement.
    def visitIf_statement(self, ctx:ExprParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#if_body.
    def visitIf_body(self, ctx:ExprParser.If_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#for_loop_condition.
    def visitFor_loop_condition(self, ctx:ExprParser.For_loop_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#for_loop.
    def visitFor_loop(self, ctx:ExprParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#func_call.
    def visitFunc_call(self, ctx:ExprParser.Func_callContext):
        return self.visitChildren(ctx)



del ExprParser
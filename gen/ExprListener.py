# Generated from Expr.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#expr.
    def enterExpr(self, ctx:ExprParser.ExprContext):
        pass

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx:ExprParser.ExprContext):
        pass


    # Enter a parse tree produced by ExprParser#variable_assign.
    def enterVariable_assign(self, ctx:ExprParser.Variable_assignContext):
        pass

    # Exit a parse tree produced by ExprParser#variable_assign.
    def exitVariable_assign(self, ctx:ExprParser.Variable_assignContext):
        pass


    # Enter a parse tree produced by ExprParser#print_function.
    def enterPrint_function(self, ctx:ExprParser.Print_functionContext):
        pass

    # Exit a parse tree produced by ExprParser#print_function.
    def exitPrint_function(self, ctx:ExprParser.Print_functionContext):
        pass


    # Enter a parse tree produced by ExprParser#operators.
    def enterOperators(self, ctx:ExprParser.OperatorsContext):
        pass

    # Exit a parse tree produced by ExprParser#operators.
    def exitOperators(self, ctx:ExprParser.OperatorsContext):
        pass


    # Enter a parse tree produced by ExprParser#logic_operators.
    def enterLogic_operators(self, ctx:ExprParser.Logic_operatorsContext):
        pass

    # Exit a parse tree produced by ExprParser#logic_operators.
    def exitLogic_operators(self, ctx:ExprParser.Logic_operatorsContext):
        pass


    # Enter a parse tree produced by ExprParser#literals.
    def enterLiterals(self, ctx:ExprParser.LiteralsContext):
        pass

    # Exit a parse tree produced by ExprParser#literals.
    def exitLiterals(self, ctx:ExprParser.LiteralsContext):
        pass


    # Enter a parse tree produced by ExprParser#comparisson_type.
    def enterComparisson_type(self, ctx:ExprParser.Comparisson_typeContext):
        pass

    # Exit a parse tree produced by ExprParser#comparisson_type.
    def exitComparisson_type(self, ctx:ExprParser.Comparisson_typeContext):
        pass


    # Enter a parse tree produced by ExprParser#if_statement.
    def enterIf_statement(self, ctx:ExprParser.If_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#if_statement.
    def exitIf_statement(self, ctx:ExprParser.If_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#condition.
    def enterCondition(self, ctx:ExprParser.ConditionContext):
        pass

    # Exit a parse tree produced by ExprParser#condition.
    def exitCondition(self, ctx:ExprParser.ConditionContext):
        pass


    # Enter a parse tree produced by ExprParser#while_loop.
    def enterWhile_loop(self, ctx:ExprParser.While_loopContext):
        pass

    # Exit a parse tree produced by ExprParser#while_loop.
    def exitWhile_loop(self, ctx:ExprParser.While_loopContext):
        pass



# Generated from C:/Users/keste/PycharmProjects/Genetyczne/Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
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


    # Enter a parse tree produced by ExprParser#variable.
    def enterVariable(self, ctx:ExprParser.VariableContext):
        pass

    # Exit a parse tree produced by ExprParser#variable.
    def exitVariable(self, ctx:ExprParser.VariableContext):
        pass


    # Enter a parse tree produced by ExprParser#variable_declaration.
    def enterVariable_declaration(self, ctx:ExprParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by ExprParser#variable_declaration.
    def exitVariable_declaration(self, ctx:ExprParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by ExprParser#variable_assign.
    def enterVariable_assign(self, ctx:ExprParser.Variable_assignContext):
        pass

    # Exit a parse tree produced by ExprParser#variable_assign.
    def exitVariable_assign(self, ctx:ExprParser.Variable_assignContext):
        pass


    # Enter a parse tree produced by ExprParser#parameter.
    def enterParameter(self, ctx:ExprParser.ParameterContext):
        pass

    # Exit a parse tree produced by ExprParser#parameter.
    def exitParameter(self, ctx:ExprParser.ParameterContext):
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


    # Enter a parse tree produced by ExprParser#numeric_literals.
    def enterNumeric_literals(self, ctx:ExprParser.Numeric_literalsContext):
        pass

    # Exit a parse tree produced by ExprParser#numeric_literals.
    def exitNumeric_literals(self, ctx:ExprParser.Numeric_literalsContext):
        pass


    # Enter a parse tree produced by ExprParser#text_type.
    def enterText_type(self, ctx:ExprParser.Text_typeContext):
        pass

    # Exit a parse tree produced by ExprParser#text_type.
    def exitText_type(self, ctx:ExprParser.Text_typeContext):
        pass


    # Enter a parse tree produced by ExprParser#numeric_type.
    def enterNumeric_type(self, ctx:ExprParser.Numeric_typeContext):
        pass

    # Exit a parse tree produced by ExprParser#numeric_type.
    def exitNumeric_type(self, ctx:ExprParser.Numeric_typeContext):
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


    # Enter a parse tree produced by ExprParser#typ.
    def enterTyp(self, ctx:ExprParser.TypContext):
        pass

    # Exit a parse tree produced by ExprParser#typ.
    def exitTyp(self, ctx:ExprParser.TypContext):
        pass


    # Enter a parse tree produced by ExprParser#if_statement.
    def enterIf_statement(self, ctx:ExprParser.If_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#if_statement.
    def exitIf_statement(self, ctx:ExprParser.If_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#if_body.
    def enterIf_body(self, ctx:ExprParser.If_bodyContext):
        pass

    # Exit a parse tree produced by ExprParser#if_body.
    def exitIf_body(self, ctx:ExprParser.If_bodyContext):
        pass


    # Enter a parse tree produced by ExprParser#for_loop_condition.
    def enterFor_loop_condition(self, ctx:ExprParser.For_loop_conditionContext):
        pass

    # Exit a parse tree produced by ExprParser#for_loop_condition.
    def exitFor_loop_condition(self, ctx:ExprParser.For_loop_conditionContext):
        pass


    # Enter a parse tree produced by ExprParser#for_loop.
    def enterFor_loop(self, ctx:ExprParser.For_loopContext):
        pass

    # Exit a parse tree produced by ExprParser#for_loop.
    def exitFor_loop(self, ctx:ExprParser.For_loopContext):
        pass


    # Enter a parse tree produced by ExprParser#func_call.
    def enterFunc_call(self, ctx:ExprParser.Func_callContext):
        pass

    # Exit a parse tree produced by ExprParser#func_call.
    def exitFunc_call(self, ctx:ExprParser.Func_callContext):
        pass



del ExprParser
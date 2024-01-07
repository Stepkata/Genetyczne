# Generated from Expr.g4 by ANTLR 4.7.2
import time
from antlr4 import *
from dataclasses import dataclass
from typing import List, Union, Tuple
import random

if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser


@dataclass
class Variable:
    name: str
    value: int


# This class defines a complete generic visitor for a parse tree produced by ExprParser.
class ExprVisitor(ParseTreeVisitor):

    def __init__(self):
        self.variables: List[Variable] = []
        self.outputs: List[int] = []

    def findVariable(self, var_name: str) -> Tuple[bool, Union[Variable, None]]:
        """
        Find a variable by name.

        Args:
            var_name (str): The name of the variable to find.

        Returns:
            Tuple[bool, Union[Variable, None]]: A tuple containing a boolean indicating whether the variable was found and the variable object if found, otherwise None.
        """
        for var in self.variables:
            if var.name == var_name:
                return True, var
        return False, None

    def visitProg(self, ctx: ExprParser.ProgContext):
        """
        Visit a parse tree produced by ExprParser#prog.

        Args:
            ctx (ExprParser.ProgContext): The parse tree context.

        Returns:
            List[int]: The list of output values.
        """
        self.visitChildren(ctx)
        return self.outputs

    def visitExpr(self, ctx: ExprParser.ExprContext):
        """
        Visit a parse tree produced by ExprParser#expr.

        Args:
            ctx (ExprParser.ExprContext): The parse tree context.

        Returns:
            Any: The result of visiting the children of the parse tree.
        """
        return self.visitChildren(ctx)

    def visitVariable_assign(self, ctx: ExprParser.Variable_assignContext):
        """
        Visit a parse tree produced by ExprParser#variable_assign.

        Args:
            ctx (ExprParser.Variable_assignContext): The parse tree context.

        Returns:
            Any: The result of visiting the children of the parse tree.
        """
        name = ctx.IDENTIFIER().getText()
        value = 0
        if ctx.literals():
            value = self.visitLiterals(ctx.literals())
        else:
            value = random.randint(0, 100)

        names = [var.name for var in self.variables]
        if name in names:
            was_variable_found, variable = self.findVariable(name)
            if was_variable_found:
                variable.value = value
        else:
            self.variables.append(Variable(name, value))
        return self.visitChildren(ctx)

    def visitPrint_function(self, ctx: ExprParser.Print_functionContext):
        """
        Visit a parse tree produced by ExprParser#print_function.

        Args:
            ctx (ExprParser.Print_functionContext): The parse tree context.
        """
        value = self.visitLiterals(ctx.literals())
        self.outputs.append(value)

    def visitOperators(self, ctx: ExprParser.OperatorsContext, literal1: int, literal2: int):
        """
        Visit a parse tree produced by ExprParser#operators.

        Args:
            ctx (ExprParser.OperatorsContext): The parse tree context.
            literal1 (int): The first literal value.
            literal2 (int): The second literal value.

        Returns:
            int: The result of the operator operation.
        """
        if ctx.ADD():
            return literal1 + literal2
        elif ctx.SUBSTRACT():
            return literal1 - literal2
        elif ctx.MULTIPLY():
            return literal1 * literal2
        elif ctx.DIVIDE():
            if literal2 == 0:
                return 0
            else:
                return int(literal1 / literal2)
        elif ctx.MOD():
            if literal2 == 0:
                return 0
            else:
                return literal1 % literal2
        else:
            return 0

    def visitLogic_operators(self, ctx: ExprParser.Logic_operatorsContext, condition1: bool, condition2: bool):
        """
        Visit a parse tree produced by ExprParser#logic_operators.

        Args:
            ctx (ExprParser.Logic_operatorsContext): The parse tree context.
            condition1 (bool): The first condition value.
            condition2 (bool): The second condition value.

        Returns:
            bool: The result of the logic operator operation.
        """
        if ctx.AND():
            return condition1 and condition2
        elif ctx.OR():
            return condition1 or condition2

    def visitLiterals(self, ctx: ExprParser.LiteralsContext):
        """
        Visit a parse tree produced by ExprParser#literals.

        Args:
            ctx (ExprParser.LiteralsContext): The parse tree context.

        Returns:
            Union[int, Any]: The value of the literals.
        """
        if ctx.IDENTIFIER():
            was_variable_found, variable = self.findVariable(ctx.IDENTIFIER().getText())
            if was_variable_found:
                return variable.value
            else:
                return 0
        elif ctx.INTLITERAL():
            return int(ctx.INTLITERAL().getText())
        elif ctx.literals():
            literal1, literal2 = self.visitLiterals(ctx.literals(0)), self.visitLiterals(ctx.literals(1))
            return self.visitOperators(ctx.operators(), literal1, literal2)

    def visitComparisson_type(self, ctx: ExprParser.Comparisson_typeContext, literal1: int, literal2: int):
        """
        Visit a parse tree produced by ExprParser#comparisson_type.

        Args:
            ctx (ExprParser.Comparisson_typeContext): The parse tree context.
            literal1 (int): The first literal value.
            literal2 (int): The second literal value.

        Returns:
            bool: The result of the comparison operation.
        """
        if ctx.EQEQ():
            return literal1 == literal2
        elif ctx.GTHAN():
            return literal1 > literal2
        elif ctx.LTHAN():
            return literal1 < literal2
        elif ctx.NOTEQ():
            return literal1 != literal2

    def visitIf_statement(self, ctx: ExprParser.If_statementContext):
        """
        Visit a parse tree produced by ExprParser#if_statement.

        Args:
            ctx (ExprParser.If_statementContext): The parse tree context.

        Returns:
            Any: The result of visiting the children of the parse tree.
        """
        condition = self.visitCondition(ctx.condition())
        if condition:
            return self.visitChildren(ctx)

    def visitCondition(self, ctx: ExprParser.ConditionContext):
        """
        Visit a parse tree produced by ExprParser#condition.

        Args:
            ctx (ExprParser.ConditionContext): The parse tree context.

        Returns:
            Union[bool, Any]: The result of the condition evaluation.
        """
        if ctx.literals():
            literal1 = self.visitLiterals(ctx.literals(0))
            literal2 = self.visitLiterals(ctx.literals(1))
            return self.visitComparisson_type(ctx.comparisson_type(), literal1, literal2)
        else:
            condition1 = self.visitCondition(ctx.condition(0))
            condition2 = self.visitCondition(ctx.condition(1))
            return self.visitLogic_operators(ctx.logic_operators(), condition1, condition2)

    def visitWhile_loop(self, ctx: ExprParser.While_loopContext):
        """
        Visit a parse tree produced by ExprParser#while_loop.

        Args:
            ctx (ExprParser.While_loopContext): The parse tree context.
        """
        condition = self.visitCondition(ctx.condition())
        while condition:
            self.visitChildren(ctx)
            condition = self.visitCondition(ctx.condition())

del ExprParser

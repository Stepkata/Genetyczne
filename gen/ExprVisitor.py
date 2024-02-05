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

    def __init__(self, max_loop_iter:int = 10, min_range: int = 5, max_range: int = 30):
        self.variables: List[Variable] = []
        self.outputs: List[int] = []
        self.inputs: List[int] = []
        self.max_loop_iter = max_loop_iter
        self.counter = 0
        self.min_range = min_range
        self.max_range = max_range
        self.index = 0

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
    def get_value(self, values, outputs):
        length = len(outputs)
        i = 0
        j = 0
        while (len(outputs) != 0):
            while (True):
                if outputs[i] in ["*", "/", "%"]:
                    if outputs[i] == "*":
                        values[i] = values[i] * values[i + 1]
                        values.pop(i + 1)
                        outputs.pop(i)
                        i -= 1
                    elif outputs[i] == "/":
                        values[i] = values[i] / values[i + 1] if values[i + 1] != 0 else values[i] / 1
                        values.pop(i + 1)
                        outputs.pop(i)
                        i -= 1
                    elif outputs[i] == "%":
                        values[i] = values[i] % values[i + 1] if values[i + 1] != 0 else values[i] % 1
                        values.pop(i + 1)
                        outputs.pop(i)
                        i -= 1
                i += 1
                if "*" not in outputs and "/" not in outputs and "%" not in outputs:
                    break
            while (True):
                if len(outputs) == 0:
                    break
                if outputs[j] in ["+", "-"]:
                    if outputs[j] == "+":
                        values[j] = values[j] + values[j + 1]
                        values.pop(j + 1)
                        outputs.pop(j)
                        j -= 1
                    elif outputs[j] == "-":
                        values[j] = values[j] - values[j + 1]
                        values.pop(j + 1)
                        outputs.pop(j)
                        j -= 1
                j += 1
                if "+" not in outputs and "-" not in outputs:
                    break
            break
        value = values[0]
        return value

    def visitProg(self, ctx: ExprParser.ProgContext):
        """
        Visit a parse tree produced by ExprParser#prog.

        Args:
            ctx (ExprParser.ProgContext): The parse tree context.

        Returns:
            List[int]: The list of output values.
        """
        self.visitChildren(ctx)
        return self.outputs, self.inputs

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
            values, outputs = self.visitLiterals(ctx.literals(), [], [])
            value = self.get_value(values, outputs)
        else:
            value = random.randint(self.min_range, self.max_range) if self.index % 2 == 0 \
                    else round(random.uniform(self.min_range, self.max_range), 2)
            self.inputs.append(value)
            self.index += 1

        names = [var.name for var in self.variables]
        if name in names:
            was_variable_found, variable = self.findVariable(name)
            if was_variable_found:
                variable.value = value
        else:
            self.variables.append(Variable(name, value))
        # return self.visitChildren(ctx)

    def visitPrint_function(self, ctx: ExprParser.Print_functionContext):
        """
        Visit a parse tree produced by ExprParser#print_function.

        Args:
            ctx (ExprParser.Print_functionContext): The parse tree context.
        """
        values, outputs = self.visitLiterals(ctx.literals(), [], [])
        length = len(outputs)
        i = 0
        j = 0
        while (len(outputs) != 0):
            while (True):
                if outputs[i] in ["*", "/", "%"]:
                    if outputs[i] == "*":
                        values[i] = values[i] * values[i + 1]
                        values.pop(i + 1)
                        outputs.pop(i)
                        i -= 1
                    elif outputs[i] == "/":
                        values[i] = round(values[i] / values[i + 1], 2) if values[i + 1] != 0 else values[i] / 1
                        values.pop(i + 1)
                        outputs.pop(i)
                        i -= 1
                    elif outputs[i] == "%":
                        values[i] = values[i] % values[i + 1] if values[i + 1] != 0 else values[i] % 1
                        values.pop(i + 1)
                        outputs.pop(i)
                        i -= 1
                i += 1
                if "*" not in outputs and "/" not in outputs and "%" not in outputs:
                    break
            while (True):
                if len(outputs) == 0:
                    break
                if outputs[j] in ["+", "-"]:
                    if outputs[j] == "+":
                        values[j] = values[j] + values[j + 1]
                        values.pop(j + 1)
                        outputs.pop(j)
                        j -= 1
                    elif outputs[j] == "-":
                        values[j] = values[j] - values[j + 1]
                        values.pop(j + 1)
                        outputs.pop(j)
                        j -= 1
                j += 1
                if "+" not in outputs and "-" not in outputs:
                    break
            break
        value = values[0]
        self.outputs.append(value)

    def visitOperators(self, ctx: ExprParser.OperatorsContext):
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
            return "+"
        elif ctx.SUBSTRACT():
            return "-"
        elif ctx.MULTIPLY():
            return "*"
        elif ctx.DIVIDE():
            return "/"
        elif ctx.MOD():
            return "%"
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

    def visitLiterals(self, ctx: ExprParser.LiteralsContext, values:List[int], outputs:List):
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
                values.append(variable.value)
                return values, outputs
            else:
                values.append(0)
                return values,outputs
        elif ctx.INTLITERAL():
            values.append(int(ctx.INTLITERAL().getText()))
            return values, outputs
        elif ctx.literals():
            values,outputs = self.visitLiterals(ctx.literals(0), values, outputs)
            outputs.append(self.visitOperators(ctx.operators()))
            values, outputs = self.visitLiterals(ctx.literals(1), values, outputs)
            return values,outputs

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
        if ctx.NOT() is not None:
            condition = not condition

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
            values, outputs = self.visitLiterals(ctx.literals(0), [], [])
            literal1 = self.get_value(values, outputs)
            values, outputs = self.visitLiterals(ctx.literals(1), [], [])
            literal2 = self.get_value(values, outputs)
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
        if ctx.NOT() is not None:
            condition = not condition
        while condition and self.counter < self.max_loop_iter:
            self.counter += 1
            self.visitChildren(ctx)
            condition = self.visitCondition(ctx.condition())
            if ctx.NOT() is not None:
                condition = not condition

del ExprParser

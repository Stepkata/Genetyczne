# Generated from Expr.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,137,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,5,0,25,8,0,10,0,12,0,
        28,9,0,5,0,30,8,0,10,0,12,0,33,9,0,1,1,1,1,1,1,1,1,1,1,3,1,40,8,
        1,1,2,1,2,1,2,1,2,3,2,46,8,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,
        1,6,1,6,1,6,3,6,60,8,6,1,6,1,6,1,6,1,6,5,6,66,8,6,10,6,12,6,69,9,
        6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,79,8,8,10,8,12,8,82,9,8,1,
        8,5,8,85,8,8,10,8,12,8,88,9,8,1,8,5,8,91,8,8,10,8,12,8,94,9,8,1,
        8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,107,8,9,10,9,12,9,
        110,9,9,1,10,1,10,1,10,1,10,1,10,1,10,5,10,118,8,10,10,10,12,10,
        121,9,10,1,10,5,10,124,8,10,10,10,12,10,127,9,10,1,10,5,10,130,8,
        10,10,10,12,10,133,9,10,1,10,1,10,1,10,0,2,12,18,11,0,2,4,6,8,10,
        12,14,16,18,20,0,3,1,0,2,6,1,0,16,17,1,0,12,15,141,0,31,1,0,0,0,
        2,39,1,0,0,0,4,41,1,0,0,0,6,47,1,0,0,0,8,52,1,0,0,0,10,54,1,0,0,
        0,12,59,1,0,0,0,14,70,1,0,0,0,16,72,1,0,0,0,18,97,1,0,0,0,20,111,
        1,0,0,0,22,26,3,2,1,0,23,25,5,20,0,0,24,23,1,0,0,0,25,28,1,0,0,0,
        26,24,1,0,0,0,26,27,1,0,0,0,27,30,1,0,0,0,28,26,1,0,0,0,29,22,1,
        0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,1,1,0,0,0,33,
        31,1,0,0,0,34,40,3,6,3,0,35,40,3,16,8,0,36,40,3,4,2,0,37,40,3,20,
        10,0,38,40,5,20,0,0,39,34,1,0,0,0,39,35,1,0,0,0,39,36,1,0,0,0,39,
        37,1,0,0,0,39,38,1,0,0,0,40,3,1,0,0,0,41,42,5,22,0,0,42,45,5,7,0,
        0,43,46,3,12,6,0,44,46,5,24,0,0,45,43,1,0,0,0,45,44,1,0,0,0,46,5,
        1,0,0,0,47,48,5,21,0,0,48,49,5,8,0,0,49,50,3,12,6,0,50,51,5,9,0,
        0,51,7,1,0,0,0,52,53,7,0,0,0,53,9,1,0,0,0,54,55,7,1,0,0,55,11,1,
        0,0,0,56,57,6,6,-1,0,57,60,5,22,0,0,58,60,5,23,0,0,59,56,1,0,0,0,
        59,58,1,0,0,0,60,67,1,0,0,0,61,62,10,1,0,0,62,63,3,8,4,0,63,64,3,
        12,6,2,64,66,1,0,0,0,65,61,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,
        68,1,0,0,0,68,13,1,0,0,0,69,67,1,0,0,0,70,71,7,2,0,0,71,15,1,0,0,
        0,72,73,5,18,0,0,73,74,5,8,0,0,74,75,3,18,9,0,75,76,5,9,0,0,76,80,
        5,10,0,0,77,79,5,20,0,0,78,77,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,
        0,80,81,1,0,0,0,81,86,1,0,0,0,82,80,1,0,0,0,83,85,3,2,1,0,84,83,
        1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,92,1,0,0,0,
        88,86,1,0,0,0,89,91,5,20,0,0,90,89,1,0,0,0,91,94,1,0,0,0,92,90,1,
        0,0,0,92,93,1,0,0,0,93,95,1,0,0,0,94,92,1,0,0,0,95,96,5,11,0,0,96,
        17,1,0,0,0,97,98,6,9,-1,0,98,99,3,12,6,0,99,100,3,14,7,0,100,101,
        3,12,6,0,101,108,1,0,0,0,102,103,10,1,0,0,103,104,3,10,5,0,104,105,
        3,18,9,2,105,107,1,0,0,0,106,102,1,0,0,0,107,110,1,0,0,0,108,106,
        1,0,0,0,108,109,1,0,0,0,109,19,1,0,0,0,110,108,1,0,0,0,111,112,5,
        19,0,0,112,113,5,8,0,0,113,114,3,18,9,0,114,115,5,9,0,0,115,119,
        5,10,0,0,116,118,5,20,0,0,117,116,1,0,0,0,118,121,1,0,0,0,119,117,
        1,0,0,0,119,120,1,0,0,0,120,125,1,0,0,0,121,119,1,0,0,0,122,124,
        3,2,1,0,123,122,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,
        1,0,0,0,126,131,1,0,0,0,127,125,1,0,0,0,128,130,5,20,0,0,129,128,
        1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,134,
        1,0,0,0,133,131,1,0,0,0,134,135,5,11,0,0,135,21,1,0,0,0,13,26,31,
        39,45,59,67,80,86,92,108,119,125,131
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "' '", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'='", "'('", "')'", "'{'", "'}'", "'<'", "'>'", "'=='", 
                     "'!='", "'&&'", "'||'", "'if'", "'while'", "<INVALID>", 
                     "'print'", "<INVALID>", "<INVALID>", "'input()'" ]

    symbolicNames = [ "<INVALID>", "WS", "ADD", "SUBSTRACT", "MULTIPLY", 
                      "DIVIDE", "MOD", "EQ", "LPAREN", "RPAREN", "LCURL", 
                      "RCURL", "LTHAN", "GTHAN", "EQEQ", "NOTEQ", "AND", 
                      "OR", "IF", "WHILE", "NEWLINE", "PRINT", "IDENTIFIER", 
                      "INTLITERAL", "INPUT" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_variable_assign = 2
    RULE_print = 3
    RULE_operators = 4
    RULE_logic_operators = 5
    RULE_literals = 6
    RULE_comparisson_type = 7
    RULE_if_statement = 8
    RULE_condition = 9
    RULE_while = 10

    ruleNames =  [ "prog", "expr", "variable_assign", "print", "operators", 
                   "logic_operators", "literals", "comparisson_type", "if_statement", 
                   "condition", "while" ]

    EOF = Token.EOF
    WS=1
    ADD=2
    SUBSTRACT=3
    MULTIPLY=4
    DIVIDE=5
    MOD=6
    EQ=7
    LPAREN=8
    RPAREN=9
    LCURL=10
    RCURL=11
    LTHAN=12
    GTHAN=13
    EQEQ=14
    NOTEQ=15
    AND=16
    OR=17
    IF=18
    WHILE=19
    NEWLINE=20
    PRINT=21
    IDENTIFIER=22
    INTLITERAL=23
    INPUT=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.NEWLINE)
            else:
                return self.getToken(ExprParser.NEWLINE, i)

        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8126464) != 0):
                self.state = 22
                self.expr()
                self.state = 26
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 23
                        self.match(ExprParser.NEWLINE) 
                    self.state = 28
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def print_(self):
            return self.getTypedRuleContext(ExprParser.PrintContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(ExprParser.If_statementContext,0)


        def variable_assign(self):
            return self.getTypedRuleContext(ExprParser.Variable_assignContext,0)


        def while_(self):
            return self.getTypedRuleContext(ExprParser.WhileContext,0)


        def NEWLINE(self):
            return self.getToken(ExprParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.state = 34
                self.print_()
                pass
            elif token in [18]:
                self.state = 35
                self.if_statement()
                pass
            elif token in [22]:
                self.state = 36
                self.variable_assign()
                pass
            elif token in [19]:
                self.state = 37
                self.while_()
                pass
            elif token in [20]:
                self.state = 38
                self.match(ExprParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ExprParser.IDENTIFIER, 0)

        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)

        def literals(self):
            return self.getTypedRuleContext(ExprParser.LiteralsContext,0)


        def INPUT(self):
            return self.getToken(ExprParser.INPUT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_variable_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_assign" ):
                listener.enterVariable_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_assign" ):
                listener.exitVariable_assign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_assign" ):
                return visitor.visitVariable_assign(self)
            else:
                return visitor.visitChildren(self)




    def variable_assign(self):

        localctx = ExprParser.Variable_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variable_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(ExprParser.IDENTIFIER)
            self.state = 42
            self.match(ExprParser.EQ)
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 23]:
                self.state = 43
                self.literals(0)
                pass
            elif token in [24]:
                self.state = 44
                self.match(ExprParser.INPUT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(ExprParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def literals(self):
            return self.getTypedRuleContext(ExprParser.LiteralsContext,0)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = ExprParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(ExprParser.PRINT)
            self.state = 48
            self.match(ExprParser.LPAREN)
            self.state = 49
            self.literals(0)
            self.state = 50
            self.match(ExprParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULTIPLY(self):
            return self.getToken(ExprParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(ExprParser.DIVIDE, 0)

        def ADD(self):
            return self.getToken(ExprParser.ADD, 0)

        def MOD(self):
            return self.getToken(ExprParser.MOD, 0)

        def SUBSTRACT(self):
            return self.getToken(ExprParser.SUBSTRACT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_operators

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperators" ):
                listener.enterOperators(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperators" ):
                listener.exitOperators(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperators" ):
                return visitor.visitOperators(self)
            else:
                return visitor.visitChildren(self)




    def operators(self):

        localctx = ExprParser.OperatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 124) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logic_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(ExprParser.AND, 0)

        def OR(self):
            return self.getToken(ExprParser.OR, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_logic_operators

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_operators" ):
                listener.enterLogic_operators(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_operators" ):
                listener.exitLogic_operators(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_operators" ):
                return visitor.visitLogic_operators(self)
            else:
                return visitor.visitChildren(self)




    def logic_operators(self):

        localctx = ExprParser.Logic_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_logic_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            _la = self._input.LA(1)
            if not(_la==16 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ExprParser.IDENTIFIER, 0)

        def INTLITERAL(self):
            return self.getToken(ExprParser.INTLITERAL, 0)

        def literals(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.LiteralsContext)
            else:
                return self.getTypedRuleContext(ExprParser.LiteralsContext,i)


        def operators(self):
            return self.getTypedRuleContext(ExprParser.OperatorsContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_literals

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiterals" ):
                listener.enterLiterals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiterals" ):
                listener.exitLiterals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)



    def literals(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.LiteralsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_literals, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.state = 57
                self.match(ExprParser.IDENTIFIER)
                pass
            elif token in [23]:
                self.state = 58
                self.match(ExprParser.INTLITERAL)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 67
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.LiteralsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_literals)
                    self.state = 61
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 62
                    self.operators()
                    self.state = 63
                    self.literals(2) 
                self.state = 69
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Comparisson_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQEQ(self):
            return self.getToken(ExprParser.EQEQ, 0)

        def GTHAN(self):
            return self.getToken(ExprParser.GTHAN, 0)

        def LTHAN(self):
            return self.getToken(ExprParser.LTHAN, 0)

        def NOTEQ(self):
            return self.getToken(ExprParser.NOTEQ, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_comparisson_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisson_type" ):
                listener.enterComparisson_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisson_type" ):
                listener.exitComparisson_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisson_type" ):
                return visitor.visitComparisson_type(self)
            else:
                return visitor.visitChildren(self)




    def comparisson_type(self):

        localctx = ExprParser.Comparisson_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comparisson_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ExprParser.IF, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(ExprParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def LCURL(self):
            return self.getToken(ExprParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(ExprParser.RCURL, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.NEWLINE)
            else:
                return self.getToken(ExprParser.NEWLINE, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ExprParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(ExprParser.IF)
            self.state = 73
            self.match(ExprParser.LPAREN)
            self.state = 74
            self.condition(0)
            self.state = 75
            self.match(ExprParser.RPAREN)
            self.state = 76
            self.match(ExprParser.LCURL)
            self.state = 80
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 77
                    self.match(ExprParser.NEWLINE) 
                self.state = 82
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 86
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 83
                    self.expr() 
                self.state = 88
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 89
                self.match(ExprParser.NEWLINE)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
            self.match(ExprParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.LiteralsContext)
            else:
                return self.getTypedRuleContext(ExprParser.LiteralsContext,i)


        def comparisson_type(self):
            return self.getTypedRuleContext(ExprParser.Comparisson_typeContext,0)


        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ConditionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ConditionContext,i)


        def logic_operators(self):
            return self.getTypedRuleContext(ExprParser.Logic_operatorsContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)



    def condition(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ConditionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_condition, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.literals(0)
            self.state = 99
            self.comparisson_type()
            self.state = 100
            self.literals(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 108
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ConditionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                    self.state = 102
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 103
                    self.logic_operators()
                    self.state = 104
                    self.condition(2) 
                self.state = 110
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class WhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(ExprParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(ExprParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def LCURL(self):
            return self.getToken(ExprParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(ExprParser.RCURL, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.NEWLINE)
            else:
                return self.getToken(ExprParser.NEWLINE, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)




    def while_(self):

        localctx = ExprParser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(ExprParser.WHILE)
            self.state = 112
            self.match(ExprParser.LPAREN)
            self.state = 113
            self.condition(0)
            self.state = 114
            self.match(ExprParser.RPAREN)
            self.state = 115
            self.match(ExprParser.LCURL)
            self.state = 119
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 116
                    self.match(ExprParser.NEWLINE) 
                self.state = 121
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 125
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 122
                    self.expr() 
                self.state = 127
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 128
                self.match(ExprParser.NEWLINE)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
            self.match(ExprParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.literals_sempred
        self._predicates[9] = self.condition_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def literals_sempred(self, localctx:LiteralsContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def condition_sempred(self, localctx:ConditionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         





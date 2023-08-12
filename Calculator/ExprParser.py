# Generated from .\ExprParser.g4 by ANTLR 4.13.0
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
        4,1,18,36,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,
        1,14,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,5,1,31,8,1,10,1,12,1,34,9,1,1,1,0,1,2,2,0,2,0,0,39,0,4,1,0,0,
        0,2,13,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,8,6,1,-1,0,
        8,9,5,7,0,0,9,10,3,2,1,0,10,11,5,8,0,0,11,14,1,0,0,0,12,14,5,16,
        0,0,13,7,1,0,0,0,13,12,1,0,0,0,14,32,1,0,0,0,15,16,10,6,0,0,16,17,
        5,14,0,0,17,31,3,2,1,6,18,19,10,5,0,0,19,20,5,13,0,0,20,31,3,2,1,
        6,21,22,10,4,0,0,22,23,5,11,0,0,23,31,3,2,1,5,24,25,10,3,0,0,25,
        26,5,12,0,0,26,31,3,2,1,4,27,28,10,2,0,0,28,29,5,15,0,0,29,31,3,
        2,1,3,30,15,1,0,0,0,30,18,1,0,0,0,30,21,1,0,0,0,30,24,1,0,0,0,30,
        27,1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,3,1,0,0,
        0,34,32,1,0,0,0,3,13,30,32
    ]

class ExprParser ( Parser ):

    grammarFileName = "ExprParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'and'", "'or'", "'not'", "'='", "','", 
                     "';'", "'('", "')'", "'{'", "'}'", "'*'", "'+'", "'/'", 
                     "'^'", "'-'" ]

    symbolicNames = [ "<INVALID>", "AND", "OR", "NOT", "EQ", "COMMA", "SEMI", 
                      "LPAREN", "RPAREN", "LCURLY", "RCURLY", "MUL", "PLUS", 
                      "DIV", "POW", "MINUS", "INT", "ID", "WS" ]

    RULE_program = 0
    RULE_expr = 1

    ruleNames =  [ "program", "expr" ]

    EOF = Token.EOF
    AND=1
    OR=2
    NOT=3
    EQ=4
    COMMA=5
    SEMI=6
    LPAREN=7
    RPAREN=8
    LCURLY=9
    RCURLY=10
    MUL=11
    PLUS=12
    DIV=13
    POW=14
    MINUS=15
    INT=16
    ID=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ExprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr(0)
            self.state = 5
            self.match(ExprParser.EOF)
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

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def POW(self):
            return self.getToken(ExprParser.POW, 0)

        def DIV(self):
            return self.getToken(ExprParser.DIV, 0)

        def MUL(self):
            return self.getToken(ExprParser.MUL, 0)

        def PLUS(self):
            return self.getToken(ExprParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ExprParser.MINUS, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.state = 8
                self.match(ExprParser.LPAREN)
                self.state = 9
                self.expr(0)
                self.state = 10
                self.match(ExprParser.RPAREN)
                pass
            elif token in [16]:
                self.state = 12
                self.match(ExprParser.INT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 32
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 30
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 15
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 16
                        self.match(ExprParser.POW)
                        self.state = 17
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 18
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 19
                        self.match(ExprParser.DIV)
                        self.state = 20
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 21
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 22
                        self.match(ExprParser.MUL)
                        self.state = 23
                        self.expr(5)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 24
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 25
                        self.match(ExprParser.PLUS)
                        self.state = 26
                        self.expr(4)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 27
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 28
                        self.match(ExprParser.MINUS)
                        self.state = 29
                        self.expr(3)
                        pass

             
                self.state = 34
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         





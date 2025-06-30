# Generated from grammar/ComparaProd.g4 by ANTLR 4.13.2
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
        4,1,16,57,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,1,0,1,1,1,1,1,1,1,
        1,5,1,29,8,1,10,1,12,1,32,9,1,1,1,3,1,35,8,1,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,43,8,2,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,
        6,0,0,7,0,2,4,6,8,10,12,0,1,1,0,5,9,53,0,19,1,0,0,0,2,24,1,0,0,0,
        4,36,1,0,0,0,6,44,1,0,0,0,8,47,1,0,0,0,10,49,1,0,0,0,12,52,1,0,0,
        0,14,15,3,2,1,0,15,16,5,15,0,0,16,18,1,0,0,0,17,14,1,0,0,0,18,21,
        1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,22,1,0,0,0,21,19,1,0,0,0,
        22,23,5,0,0,1,23,1,1,0,0,0,24,25,5,1,0,0,25,30,3,4,2,0,26,27,5,2,
        0,0,27,29,3,4,2,0,28,26,1,0,0,0,29,32,1,0,0,0,30,28,1,0,0,0,30,31,
        1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,33,35,5,15,0,0,34,33,1,0,0,0,
        34,35,1,0,0,0,35,3,1,0,0,0,36,37,5,13,0,0,37,38,5,3,0,0,38,39,3,
        6,3,0,39,40,5,4,0,0,40,42,3,10,5,0,41,43,3,12,6,0,42,41,1,0,0,0,
        42,43,1,0,0,0,43,5,1,0,0,0,44,45,5,14,0,0,45,46,3,8,4,0,46,7,1,0,
        0,0,47,48,7,0,0,0,48,9,1,0,0,0,49,50,5,10,0,0,50,51,5,14,0,0,51,
        11,1,0,0,0,52,53,5,11,0,0,53,54,5,14,0,0,54,55,5,12,0,0,55,13,1,
        0,0,0,4,19,30,34,42
    ]

class ComparaProdParser ( Parser ):

    grammarFileName = "ComparaProd.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'compare'", "','", "'de'", "'por'", "'ml'", 
                     "'l'", "'g'", "'kg'", "'oz'", "'R$'", "'com'", "'% off'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "STRING", "NUMBER", "NEWLINE", "WS" ]

    RULE_program = 0
    RULE_comparison = 1
    RULE_product = 2
    RULE_quantity = 3
    RULE_unit = 4
    RULE_price = 5
    RULE_promotion = 6

    ruleNames =  [ "program", "comparison", "product", "quantity", "unit", 
                   "price", "promotion" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    STRING=13
    NUMBER=14
    NEWLINE=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ComparaProdParser.EOF, 0)

        def comparison(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ComparaProdParser.ComparisonContext)
            else:
                return self.getTypedRuleContext(ComparaProdParser.ComparisonContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ComparaProdParser.NEWLINE)
            else:
                return self.getToken(ComparaProdParser.NEWLINE, i)

        def getRuleIndex(self):
            return ComparaProdParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ComparaProdParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 14
                self.comparison()
                self.state = 15
                self.match(ComparaProdParser.NEWLINE)
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(ComparaProdParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def product(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ComparaProdParser.ProductContext)
            else:
                return self.getTypedRuleContext(ComparaProdParser.ProductContext,i)


        def NEWLINE(self):
            return self.getToken(ComparaProdParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ComparaProdParser.RULE_comparison

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = ComparaProdParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(ComparaProdParser.T__0)
            self.state = 25
            self.product()
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 26
                self.match(ComparaProdParser.T__1)
                self.state = 27
                self.product()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 33
                self.match(ComparaProdParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProductContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ComparaProdParser.STRING, 0)

        def quantity(self):
            return self.getTypedRuleContext(ComparaProdParser.QuantityContext,0)


        def price(self):
            return self.getTypedRuleContext(ComparaProdParser.PriceContext,0)


        def promotion(self):
            return self.getTypedRuleContext(ComparaProdParser.PromotionContext,0)


        def getRuleIndex(self):
            return ComparaProdParser.RULE_product

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProduct" ):
                return visitor.visitProduct(self)
            else:
                return visitor.visitChildren(self)




    def product(self):

        localctx = ComparaProdParser.ProductContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_product)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(ComparaProdParser.STRING)
            self.state = 37
            self.match(ComparaProdParser.T__2)
            self.state = 38
            self.quantity()
            self.state = 39
            self.match(ComparaProdParser.T__3)
            self.state = 40
            self.price()
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 41
                self.promotion()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ComparaProdParser.NUMBER, 0)

        def unit(self):
            return self.getTypedRuleContext(ComparaProdParser.UnitContext,0)


        def getRuleIndex(self):
            return ComparaProdParser.RULE_quantity

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuantity" ):
                return visitor.visitQuantity(self)
            else:
                return visitor.visitChildren(self)




    def quantity(self):

        localctx = ComparaProdParser.QuantityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_quantity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(ComparaProdParser.NUMBER)
            self.state = 45
            self.unit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ComparaProdParser.RULE_unit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnit" ):
                return visitor.visitUnit(self)
            else:
                return visitor.visitChildren(self)




    def unit(self):

        localctx = ComparaProdParser.UnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_unit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 992) != 0)):
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


    class PriceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ComparaProdParser.NUMBER, 0)

        def getRuleIndex(self):
            return ComparaProdParser.RULE_price

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrice" ):
                return visitor.visitPrice(self)
            else:
                return visitor.visitChildren(self)




    def price(self):

        localctx = ComparaProdParser.PriceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_price)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(ComparaProdParser.T__9)
            self.state = 50
            self.match(ComparaProdParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PromotionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ComparaProdParser.NUMBER, 0)

        def getRuleIndex(self):
            return ComparaProdParser.RULE_promotion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPromotion" ):
                return visitor.visitPromotion(self)
            else:
                return visitor.visitChildren(self)




    def promotion(self):

        localctx = ComparaProdParser.PromotionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_promotion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(ComparaProdParser.T__10)
            self.state = 53
            self.match(ComparaProdParser.NUMBER)
            self.state = 54
            self.match(ComparaProdParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






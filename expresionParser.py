# Generated from expresion.g by ANTLR 4.13.1
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
        4,1,18,91,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,0,1,0,1,
        1,1,1,1,2,1,2,1,2,5,2,33,8,2,10,2,12,2,36,9,2,1,3,1,3,1,3,5,3,41,
        8,3,10,3,12,3,44,9,3,1,4,1,4,1,4,5,4,49,8,4,10,4,12,4,52,9,4,1,5,
        1,5,1,5,5,5,57,8,5,10,5,12,5,60,9,5,1,6,1,6,1,6,5,6,65,8,6,10,6,
        12,6,68,9,6,1,7,1,7,1,7,5,7,73,8,7,10,7,12,7,76,9,7,1,8,1,8,1,8,
        3,8,81,8,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,89,8,9,1,9,0,0,10,0,2,4,6,
        8,10,12,14,16,18,0,4,1,0,7,8,1,0,9,12,1,0,1,2,1,0,3,4,90,0,21,1,
        0,0,0,2,27,1,0,0,0,4,29,1,0,0,0,6,37,1,0,0,0,8,45,1,0,0,0,10,53,
        1,0,0,0,12,61,1,0,0,0,14,69,1,0,0,0,16,80,1,0,0,0,18,88,1,0,0,0,
        20,22,3,2,1,0,21,20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,
        0,0,0,24,25,1,0,0,0,25,26,5,0,0,1,26,1,1,0,0,0,27,28,3,4,2,0,28,
        3,1,0,0,0,29,34,3,6,3,0,30,31,5,14,0,0,31,33,3,6,3,0,32,30,1,0,0,
        0,33,36,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,5,1,0,0,0,36,34,1,
        0,0,0,37,42,3,8,4,0,38,39,5,13,0,0,39,41,3,8,4,0,40,38,1,0,0,0,41,
        44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,7,1,0,0,0,44,42,1,0,0,
        0,45,50,3,10,5,0,46,47,7,0,0,0,47,49,3,10,5,0,48,46,1,0,0,0,49,52,
        1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,9,1,0,0,0,52,50,1,0,0,0,53,
        58,3,12,6,0,54,55,7,1,0,0,55,57,3,12,6,0,56,54,1,0,0,0,57,60,1,0,
        0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,11,1,0,0,0,60,58,1,0,0,0,61,66,
        3,14,7,0,62,63,7,2,0,0,63,65,3,14,7,0,64,62,1,0,0,0,65,68,1,0,0,
        0,66,64,1,0,0,0,66,67,1,0,0,0,67,13,1,0,0,0,68,66,1,0,0,0,69,74,
        3,16,8,0,70,71,7,3,0,0,71,73,3,16,8,0,72,70,1,0,0,0,73,76,1,0,0,
        0,74,72,1,0,0,0,74,75,1,0,0,0,75,15,1,0,0,0,76,74,1,0,0,0,77,78,
        5,15,0,0,78,81,3,16,8,0,79,81,3,18,9,0,80,77,1,0,0,0,80,79,1,0,0,
        0,81,17,1,0,0,0,82,89,5,16,0,0,83,89,5,17,0,0,84,85,5,5,0,0,85,86,
        3,2,1,0,86,87,5,6,0,0,87,89,1,0,0,0,88,82,1,0,0,0,88,83,1,0,0,0,
        88,84,1,0,0,0,89,19,1,0,0,0,9,23,34,42,50,58,66,74,80,88
    ]

class expresionParser ( Parser ):

    grammarFileName = "expresion.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'&&'", 
                     "'||'", "'!'" ]

    symbolicNames = [ "<INVALID>", "SUM", "RES", "MUL", "DIV", "PAI", "PAD", 
                      "IGUAL", "NOIGUAL", "MENOR", "MAYOR", "MENORI", "MAYORI", 
                      "AND", "OR", "NOT", "NUM", "ID", "WS" ]

    RULE_root = 0
    RULE_expresion = 1
    RULE_orLogico = 2
    RULE_andLogico = 3
    RULE_igualdad = 4
    RULE_comparacion = 5
    RULE_suma = 6
    RULE_multiplicacion = 7
    RULE_unario = 8
    RULE_base = 9

    ruleNames =  [ "root", "expresion", "orLogico", "andLogico", "igualdad", 
                   "comparacion", "suma", "multiplicacion", "unario", "base" ]

    EOF = Token.EOF
    SUM=1
    RES=2
    MUL=3
    DIV=4
    PAI=5
    PAD=6
    IGUAL=7
    NOIGUAL=8
    MENOR=9
    MAYOR=10
    MENORI=11
    MAYORI=12
    AND=13
    OR=14
    NOT=15
    NUM=16
    ID=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(expresionParser.EOF, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(expresionParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(expresionParser.ExpresionContext,i)


        def getRuleIndex(self):
            return expresionParser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)




    def root(self):

        localctx = expresionParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.expresion()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 229408) != 0)):
                    break

            self.state = 25
            self.match(expresionParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def orLogico(self):
            return self.getTypedRuleContext(expresionParser.OrLogicoContext,0)


        def getRuleIndex(self):
            return expresionParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)




    def expresion(self):

        localctx = expresionParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.orLogico()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrLogicoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andLogico(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(expresionParser.AndLogicoContext)
            else:
                return self.getTypedRuleContext(expresionParser.AndLogicoContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(expresionParser.OR)
            else:
                return self.getToken(expresionParser.OR, i)

        def getRuleIndex(self):
            return expresionParser.RULE_orLogico

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrLogico" ):
                listener.enterOrLogico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrLogico" ):
                listener.exitOrLogico(self)




    def orLogico(self):

        localctx = expresionParser.OrLogicoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_orLogico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.andLogico()
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 30
                self.match(expresionParser.OR)
                self.state = 31
                self.andLogico()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndLogicoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def igualdad(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(expresionParser.IgualdadContext)
            else:
                return self.getTypedRuleContext(expresionParser.IgualdadContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(expresionParser.AND)
            else:
                return self.getToken(expresionParser.AND, i)

        def getRuleIndex(self):
            return expresionParser.RULE_andLogico

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndLogico" ):
                listener.enterAndLogico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndLogico" ):
                listener.exitAndLogico(self)




    def andLogico(self):

        localctx = expresionParser.AndLogicoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_andLogico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.igualdad()
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 38
                self.match(expresionParser.AND)
                self.state = 39
                self.igualdad()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgualdadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(expresionParser.ComparacionContext)
            else:
                return self.getTypedRuleContext(expresionParser.ComparacionContext,i)


        def IGUAL(self, i:int=None):
            if i is None:
                return self.getTokens(expresionParser.IGUAL)
            else:
                return self.getToken(expresionParser.IGUAL, i)

        def NOIGUAL(self, i:int=None):
            if i is None:
                return self.getTokens(expresionParser.NOIGUAL)
            else:
                return self.getToken(expresionParser.NOIGUAL, i)

        def getRuleIndex(self):
            return expresionParser.RULE_igualdad

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIgualdad" ):
                listener.enterIgualdad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIgualdad" ):
                listener.exitIgualdad(self)




    def igualdad(self):

        localctx = expresionParser.IgualdadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_igualdad)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.comparacion()
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 46
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 47
                self.comparacion()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def suma(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(expresionParser.SumaContext)
            else:
                return self.getTypedRuleContext(expresionParser.SumaContext,i)


        def MAYOR(self, i:int=None):
            if i is None:
                return self.getTokens(expresionParser.MAYOR)
            else:
                return self.getToken(expresionParser.MAYOR, i)

        def MENOR(self, i:int=None):
            if i is None:
                return self.getTokens(expresionParser.MENOR)
            else:
                return self.getToken(expresionParser.MENOR, i)

        def MAYORI(self, i:int=None):
            if i is None:
                return self.getTokens(expresionParser.MAYORI)
            else:
                return self.getToken(expresionParser.MAYORI, i)

        def MENORI(self, i:int=None):
            if i is None:
                return self.getTokens(expresionParser.MENORI)
            else:
                return self.getToken(expresionParser.MENORI, i)

        def getRuleIndex(self):
            return expresionParser.RULE_comparacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparacion" ):
                listener.enterComparacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparacion" ):
                listener.exitComparacion(self)




    def comparacion(self):

        localctx = expresionParser.ComparacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comparacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.suma()
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0):
                self.state = 54
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 55
                self.suma()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SumaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(expresionParser.MultiplicacionContext)
            else:
                return self.getTypedRuleContext(expresionParser.MultiplicacionContext,i)


        def SUM(self, i:int=None):
            if i is None:
                return self.getTokens(expresionParser.SUM)
            else:
                return self.getToken(expresionParser.SUM, i)

        def RES(self, i:int=None):
            if i is None:
                return self.getTokens(expresionParser.RES)
            else:
                return self.getToken(expresionParser.RES, i)

        def getRuleIndex(self):
            return expresionParser.RULE_suma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuma" ):
                listener.enterSuma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuma" ):
                listener.exitSuma(self)




    def suma(self):

        localctx = expresionParser.SumaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_suma)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.multiplicacion()
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 62
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 63
                self.multiplicacion()
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unario(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(expresionParser.UnarioContext)
            else:
                return self.getTypedRuleContext(expresionParser.UnarioContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(expresionParser.MUL)
            else:
                return self.getToken(expresionParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(expresionParser.DIV)
            else:
                return self.getToken(expresionParser.DIV, i)

        def getRuleIndex(self):
            return expresionParser.RULE_multiplicacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicacion" ):
                listener.enterMultiplicacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicacion" ):
                listener.exitMultiplicacion(self)




    def multiplicacion(self):

        localctx = expresionParser.MultiplicacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_multiplicacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.unario()
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 70
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 71
                self.unario()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(expresionParser.NOT, 0)

        def unario(self):
            return self.getTypedRuleContext(expresionParser.UnarioContext,0)


        def base(self):
            return self.getTypedRuleContext(expresionParser.BaseContext,0)


        def getRuleIndex(self):
            return expresionParser.RULE_unario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnario" ):
                listener.enterUnario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnario" ):
                listener.exitUnario(self)




    def unario(self):

        localctx = expresionParser.UnarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_unario)
        try:
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.match(expresionParser.NOT)
                self.state = 78
                self.unario()
                pass
            elif token in [5, 16, 17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.base()
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


    class BaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(expresionParser.NUM, 0)

        def ID(self):
            return self.getToken(expresionParser.ID, 0)

        def PAI(self):
            return self.getToken(expresionParser.PAI, 0)

        def expresion(self):
            return self.getTypedRuleContext(expresionParser.ExpresionContext,0)


        def PAD(self):
            return self.getToken(expresionParser.PAD, 0)

        def getRuleIndex(self):
            return expresionParser.RULE_base

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBase" ):
                listener.enterBase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBase" ):
                listener.exitBase(self)




    def base(self):

        localctx = expresionParser.BaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_base)
        try:
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.match(expresionParser.NUM)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.match(expresionParser.ID)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.match(expresionParser.PAI)
                self.state = 85
                self.expresion()
                self.state = 86
                self.match(expresionParser.PAD)
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






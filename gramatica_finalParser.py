# Generated from gramatica_final.g4 by ANTLR 4.13.1
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
        4,1,45,328,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,1,0,1,0,5,0,64,8,0,10,0,12,0,67,
        9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,79,8,1,1,2,1,2,1,
        2,1,2,1,3,1,3,1,3,1,3,3,3,89,8,3,1,4,1,4,1,4,1,4,3,4,95,8,4,1,4,
        1,4,1,4,1,5,1,5,1,5,5,5,103,8,5,10,5,12,5,106,9,5,1,6,1,6,1,6,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,3,7,128,8,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,139,8,9,10,
        9,12,9,142,9,9,3,9,144,8,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,3,10,160,8,10,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,3,11,172,8,11,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,3,12,181,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,
        1,14,1,14,1,14,3,14,193,8,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,15,1,15,1,15,1,15,1,15,1,15,5,15,208,8,15,10,15,12,15,211,9,15,
        1,15,3,15,214,8,15,1,15,1,15,1,16,1,16,1,16,1,16,5,16,222,8,16,10,
        16,12,16,225,9,16,1,17,1,17,1,17,5,17,230,8,17,10,17,12,17,233,9,
        17,1,18,1,18,1,18,1,19,1,19,1,19,1,20,1,20,5,20,243,8,20,10,20,12,
        20,246,9,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,3,21,256,8,21,
        1,22,1,22,1,22,5,22,261,8,22,10,22,12,22,264,9,22,1,23,1,23,1,23,
        5,23,269,8,23,10,23,12,23,272,9,23,1,24,1,24,1,24,5,24,277,8,24,
        10,24,12,24,280,9,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,
        1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,299,8,25,1,26,1,26,
        1,26,3,26,304,8,26,1,26,1,26,1,27,1,27,1,27,5,27,311,8,27,10,27,
        12,27,314,9,27,1,28,1,28,3,28,318,8,28,1,28,1,28,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,0,0,30,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,0,3,1,0,31,36,1,
        0,26,27,1,0,28,30,342,0,60,1,0,0,0,2,78,1,0,0,0,4,80,1,0,0,0,6,88,
        1,0,0,0,8,90,1,0,0,0,10,99,1,0,0,0,12,107,1,0,0,0,14,127,1,0,0,0,
        16,129,1,0,0,0,18,134,1,0,0,0,20,159,1,0,0,0,22,171,1,0,0,0,24,173,
        1,0,0,0,26,182,1,0,0,0,28,188,1,0,0,0,30,201,1,0,0,0,32,217,1,0,
        0,0,34,226,1,0,0,0,36,234,1,0,0,0,38,237,1,0,0,0,40,240,1,0,0,0,
        42,249,1,0,0,0,44,257,1,0,0,0,46,265,1,0,0,0,48,273,1,0,0,0,50,298,
        1,0,0,0,52,300,1,0,0,0,54,307,1,0,0,0,56,315,1,0,0,0,58,321,1,0,
        0,0,60,61,5,7,0,0,61,65,5,18,0,0,62,64,3,2,1,0,63,62,1,0,0,0,64,
        67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,65,1,0,0,
        0,68,69,5,19,0,0,69,70,5,0,0,1,70,1,1,0,0,0,71,79,3,8,4,0,72,79,
        3,14,7,0,73,79,3,6,3,0,74,79,3,26,13,0,75,79,3,28,14,0,76,79,3,24,
        12,0,77,79,3,30,15,0,78,71,1,0,0,0,78,72,1,0,0,0,78,73,1,0,0,0,78,
        74,1,0,0,0,78,75,1,0,0,0,78,76,1,0,0,0,78,77,1,0,0,0,79,3,1,0,0,
        0,80,81,5,1,0,0,81,82,5,42,0,0,82,83,5,25,0,0,83,5,1,0,0,0,84,89,
        3,58,29,0,85,86,3,22,11,0,86,87,5,25,0,0,87,89,1,0,0,0,88,84,1,0,
        0,0,88,85,1,0,0,0,89,7,1,0,0,0,90,91,5,17,0,0,91,92,5,42,0,0,92,
        94,5,20,0,0,93,95,3,10,5,0,94,93,1,0,0,0,94,95,1,0,0,0,95,96,1,0,
        0,0,96,97,5,21,0,0,97,98,3,40,20,0,98,9,1,0,0,0,99,104,3,12,6,0,
        100,101,5,2,0,0,101,103,3,12,6,0,102,100,1,0,0,0,103,106,1,0,0,0,
        104,102,1,0,0,0,104,105,1,0,0,0,105,11,1,0,0,0,106,104,1,0,0,0,107,
        108,5,17,0,0,108,109,5,42,0,0,109,13,1,0,0,0,110,111,5,17,0,0,111,
        112,5,42,0,0,112,113,5,24,0,0,113,114,3,42,21,0,114,115,5,25,0,0,
        115,128,1,0,0,0,116,117,5,17,0,0,117,118,5,42,0,0,118,128,5,25,0,
        0,119,120,5,17,0,0,120,121,5,22,0,0,121,122,5,23,0,0,122,123,5,42,
        0,0,123,124,5,24,0,0,124,125,3,18,9,0,125,126,5,25,0,0,126,128,1,
        0,0,0,127,110,1,0,0,0,127,116,1,0,0,0,127,119,1,0,0,0,128,15,1,0,
        0,0,129,130,5,42,0,0,130,131,5,22,0,0,131,132,3,42,21,0,132,133,
        5,23,0,0,133,17,1,0,0,0,134,143,5,22,0,0,135,140,3,42,21,0,136,137,
        5,2,0,0,137,139,3,42,21,0,138,136,1,0,0,0,139,142,1,0,0,0,140,138,
        1,0,0,0,140,141,1,0,0,0,141,144,1,0,0,0,142,140,1,0,0,0,143,135,
        1,0,0,0,143,144,1,0,0,0,144,145,1,0,0,0,145,146,5,23,0,0,146,19,
        1,0,0,0,147,160,3,14,7,0,148,149,3,22,11,0,149,150,5,25,0,0,150,
        160,1,0,0,0,151,160,3,24,12,0,152,160,3,58,29,0,153,160,3,26,13,
        0,154,160,3,28,14,0,155,160,3,30,15,0,156,160,3,56,28,0,157,160,
        3,36,18,0,158,160,3,38,19,0,159,147,1,0,0,0,159,148,1,0,0,0,159,
        151,1,0,0,0,159,152,1,0,0,0,159,153,1,0,0,0,159,154,1,0,0,0,159,
        155,1,0,0,0,159,156,1,0,0,0,159,157,1,0,0,0,159,158,1,0,0,0,160,
        21,1,0,0,0,161,162,5,42,0,0,162,163,5,24,0,0,163,172,3,42,21,0,164,
        165,5,42,0,0,165,166,5,22,0,0,166,167,3,42,21,0,167,168,5,23,0,0,
        168,169,5,24,0,0,169,170,3,42,21,0,170,172,1,0,0,0,171,161,1,0,0,
        0,171,164,1,0,0,0,172,23,1,0,0,0,173,174,5,8,0,0,174,175,5,20,0,
        0,175,176,3,42,21,0,176,177,5,21,0,0,177,180,3,40,20,0,178,179,5,
        9,0,0,179,181,3,40,20,0,180,178,1,0,0,0,180,181,1,0,0,0,181,25,1,
        0,0,0,182,183,5,10,0,0,183,184,5,20,0,0,184,185,3,42,21,0,185,186,
        5,21,0,0,186,187,3,40,20,0,187,27,1,0,0,0,188,189,5,11,0,0,189,192,
        5,20,0,0,190,193,3,14,7,0,191,193,3,22,11,0,192,190,1,0,0,0,192,
        191,1,0,0,0,193,194,1,0,0,0,194,195,5,25,0,0,195,196,3,42,21,0,196,
        197,5,25,0,0,197,198,3,22,11,0,198,199,5,21,0,0,199,200,3,40,20,
        0,200,29,1,0,0,0,201,202,5,14,0,0,202,203,5,20,0,0,203,204,3,42,
        21,0,204,205,5,21,0,0,205,209,5,18,0,0,206,208,3,32,16,0,207,206,
        1,0,0,0,208,211,1,0,0,0,209,207,1,0,0,0,209,210,1,0,0,0,210,213,
        1,0,0,0,211,209,1,0,0,0,212,214,3,34,17,0,213,212,1,0,0,0,213,214,
        1,0,0,0,214,215,1,0,0,0,215,216,5,19,0,0,216,31,1,0,0,0,217,218,
        5,15,0,0,218,219,5,41,0,0,219,223,5,3,0,0,220,222,3,20,10,0,221,
        220,1,0,0,0,222,225,1,0,0,0,223,221,1,0,0,0,223,224,1,0,0,0,224,
        33,1,0,0,0,225,223,1,0,0,0,226,227,5,16,0,0,227,231,5,3,0,0,228,
        230,3,20,10,0,229,228,1,0,0,0,230,233,1,0,0,0,231,229,1,0,0,0,231,
        232,1,0,0,0,232,35,1,0,0,0,233,231,1,0,0,0,234,235,5,4,0,0,235,236,
        5,25,0,0,236,37,1,0,0,0,237,238,5,5,0,0,238,239,5,25,0,0,239,39,
        1,0,0,0,240,244,5,18,0,0,241,243,3,20,10,0,242,241,1,0,0,0,243,246,
        1,0,0,0,244,242,1,0,0,0,244,245,1,0,0,0,245,247,1,0,0,0,246,244,
        1,0,0,0,247,248,5,19,0,0,248,41,1,0,0,0,249,255,3,44,22,0,250,251,
        5,6,0,0,251,252,3,42,21,0,252,253,5,3,0,0,253,254,3,42,21,0,254,
        256,1,0,0,0,255,250,1,0,0,0,255,256,1,0,0,0,256,43,1,0,0,0,257,262,
        3,46,23,0,258,259,7,0,0,0,259,261,3,46,23,0,260,258,1,0,0,0,261,
        264,1,0,0,0,262,260,1,0,0,0,262,263,1,0,0,0,263,45,1,0,0,0,264,262,
        1,0,0,0,265,270,3,48,24,0,266,267,7,1,0,0,267,269,3,48,24,0,268,
        266,1,0,0,0,269,272,1,0,0,0,270,268,1,0,0,0,270,271,1,0,0,0,271,
        47,1,0,0,0,272,270,1,0,0,0,273,278,3,50,25,0,274,275,7,2,0,0,275,
        277,3,50,25,0,276,274,1,0,0,0,277,280,1,0,0,0,278,276,1,0,0,0,278,
        279,1,0,0,0,279,49,1,0,0,0,280,278,1,0,0,0,281,299,5,41,0,0,282,
        299,5,40,0,0,283,299,3,52,26,0,284,285,5,42,0,0,285,286,5,22,0,0,
        286,287,3,42,21,0,287,288,5,23,0,0,288,299,1,0,0,0,289,299,5,42,
        0,0,290,291,5,20,0,0,291,292,3,42,21,0,292,293,5,21,0,0,293,299,
        1,0,0,0,294,295,5,39,0,0,295,299,3,50,25,0,296,297,5,27,0,0,297,
        299,3,50,25,0,298,281,1,0,0,0,298,282,1,0,0,0,298,283,1,0,0,0,298,
        284,1,0,0,0,298,289,1,0,0,0,298,290,1,0,0,0,298,294,1,0,0,0,298,
        296,1,0,0,0,299,51,1,0,0,0,300,301,5,42,0,0,301,303,5,20,0,0,302,
        304,3,54,27,0,303,302,1,0,0,0,303,304,1,0,0,0,304,305,1,0,0,0,305,
        306,5,21,0,0,306,53,1,0,0,0,307,312,3,42,21,0,308,309,5,2,0,0,309,
        311,3,42,21,0,310,308,1,0,0,0,311,314,1,0,0,0,312,310,1,0,0,0,312,
        313,1,0,0,0,313,55,1,0,0,0,314,312,1,0,0,0,315,317,5,12,0,0,316,
        318,3,42,21,0,317,316,1,0,0,0,317,318,1,0,0,0,318,319,1,0,0,0,319,
        320,5,25,0,0,320,57,1,0,0,0,321,322,5,13,0,0,322,323,5,20,0,0,323,
        324,3,42,21,0,324,325,5,21,0,0,325,326,5,25,0,0,326,59,1,0,0,0,25,
        65,78,88,94,104,127,140,143,159,171,180,192,209,213,223,231,244,
        255,262,270,278,298,303,312,317
    ]

class gramatica_finalParser ( Parser ):

    grammarFileName = "gramatica_final.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'import'", "','", "':'", "'break'", "'continue'", 
                     "'?'", "'program'", "'si'", "'sino'", "'while'", "'for'", 
                     "'return'", "'print'", "'switch'", "'case'", "'default'", 
                     "<INVALID>", "'{'", "'}'", "'('", "')'", "'['", "']'", 
                     "'='", "';'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'&&'", "'||'", 
                     "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "PROGRAM", 
                      "SI", "SINO", "WHILE", "FOR", "RETURN", "PRINT", "SWITCH", 
                      "CASE", "DEFAULT", "TIPO", "LLAVEI", "LLAVED", "PAI", 
                      "PAD", "CORI", "CORD", "ASIG", "FINAL", "SUM", "RES", 
                      "MUL", "DIV", "MOD", "IGUAL", "NOIGUAL", "MENOR", 
                      "MAYOR", "MENORI", "MAYORI", "AND", "OR", "NOT", "STRING", 
                      "NUM", "ID", "COMENTARIO_LINEA", "COMENTARIO_BLOQUE", 
                      "WS" ]

    RULE_root = 0
    RULE_programa = 1
    RULE_importStmt = 2
    RULE_sentenciaGlobal = 3
    RULE_funcion = 4
    RULE_parametros = 5
    RULE_parametro = 6
    RULE_declaracion = 7
    RULE_accesoArray = 8
    RULE_arrayLiteral = 9
    RULE_sentencia = 10
    RULE_asignacion = 11
    RULE_expresionSi = 12
    RULE_cicloWhile = 13
    RULE_cicloFor = 14
    RULE_switchStmt = 15
    RULE_caseStmt = 16
    RULE_defaultStmt = 17
    RULE_breakStmt = 18
    RULE_continueStmt = 19
    RULE_bloque = 20
    RULE_expresion = 21
    RULE_comparacion = 22
    RULE_suma = 23
    RULE_termino = 24
    RULE_factor = 25
    RULE_llamadaFuncion = 26
    RULE_argumentos = 27
    RULE_returnStmt = 28
    RULE_printt = 29

    ruleNames =  [ "root", "programa", "importStmt", "sentenciaGlobal", 
                   "funcion", "parametros", "parametro", "declaracion", 
                   "accesoArray", "arrayLiteral", "sentencia", "asignacion", 
                   "expresionSi", "cicloWhile", "cicloFor", "switchStmt", 
                   "caseStmt", "defaultStmt", "breakStmt", "continueStmt", 
                   "bloque", "expresion", "comparacion", "suma", "termino", 
                   "factor", "llamadaFuncion", "argumentos", "returnStmt", 
                   "printt" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    PROGRAM=7
    SI=8
    SINO=9
    WHILE=10
    FOR=11
    RETURN=12
    PRINT=13
    SWITCH=14
    CASE=15
    DEFAULT=16
    TIPO=17
    LLAVEI=18
    LLAVED=19
    PAI=20
    PAD=21
    CORI=22
    CORD=23
    ASIG=24
    FINAL=25
    SUM=26
    RES=27
    MUL=28
    DIV=29
    MOD=30
    IGUAL=31
    NOIGUAL=32
    MENOR=33
    MAYOR=34
    MENORI=35
    MAYORI=36
    AND=37
    OR=38
    NOT=39
    STRING=40
    NUM=41
    ID=42
    COMENTARIO_LINEA=43
    COMENTARIO_BLOQUE=44
    WS=45

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

        def PROGRAM(self):
            return self.getToken(gramatica_finalParser.PROGRAM, 0)

        def LLAVEI(self):
            return self.getToken(gramatica_finalParser.LLAVEI, 0)

        def LLAVED(self):
            return self.getToken(gramatica_finalParser.LLAVED, 0)

        def EOF(self):
            return self.getToken(gramatica_finalParser.EOF, 0)

        def programa(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_finalParser.ProgramaContext)
            else:
                return self.getTypedRuleContext(gramatica_finalParser.ProgramaContext,i)


        def getRuleIndex(self):
            return gramatica_finalParser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = gramatica_finalParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(gramatica_finalParser.PROGRAM)
            self.state = 61
            self.match(gramatica_finalParser.LLAVEI)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398046670080) != 0):
                self.state = 62
                self.programa()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self.match(gramatica_finalParser.LLAVED)
            self.state = 69
            self.match(gramatica_finalParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcion(self):
            return self.getTypedRuleContext(gramatica_finalParser.FuncionContext,0)


        def declaracion(self):
            return self.getTypedRuleContext(gramatica_finalParser.DeclaracionContext,0)


        def sentenciaGlobal(self):
            return self.getTypedRuleContext(gramatica_finalParser.SentenciaGlobalContext,0)


        def cicloWhile(self):
            return self.getTypedRuleContext(gramatica_finalParser.CicloWhileContext,0)


        def cicloFor(self):
            return self.getTypedRuleContext(gramatica_finalParser.CicloForContext,0)


        def expresionSi(self):
            return self.getTypedRuleContext(gramatica_finalParser.ExpresionSiContext,0)


        def switchStmt(self):
            return self.getTypedRuleContext(gramatica_finalParser.SwitchStmtContext,0)


        def getRuleIndex(self):
            return gramatica_finalParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = gramatica_finalParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_programa)
        try:
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.funcion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.declaracion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.sentenciaGlobal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 74
                self.cicloWhile()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 75
                self.cicloFor()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 76
                self.expresionSi()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 77
                self.switchStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramatica_finalParser.ID, 0)

        def FINAL(self):
            return self.getToken(gramatica_finalParser.FINAL, 0)

        def getRuleIndex(self):
            return gramatica_finalParser.RULE_importStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportStmt" ):
                listener.enterImportStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportStmt" ):
                listener.exitImportStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportStmt" ):
                return visitor.visitImportStmt(self)
            else:
                return visitor.visitChildren(self)




    def importStmt(self):

        localctx = gramatica_finalParser.ImportStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_importStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(gramatica_finalParser.T__0)
            self.state = 81
            self.match(gramatica_finalParser.ID)
            self.state = 82
            self.match(gramatica_finalParser.FINAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaGlobalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def printt(self):
            return self.getTypedRuleContext(gramatica_finalParser.PrinttContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(gramatica_finalParser.AsignacionContext,0)


        def FINAL(self):
            return self.getToken(gramatica_finalParser.FINAL, 0)

        def getRuleIndex(self):
            return gramatica_finalParser.RULE_sentenciaGlobal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaGlobal" ):
                listener.enterSentenciaGlobal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaGlobal" ):
                listener.exitSentenciaGlobal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaGlobal" ):
                return visitor.visitSentenciaGlobal(self)
            else:
                return visitor.visitChildren(self)




    def sentenciaGlobal(self):

        localctx = gramatica_finalParser.SentenciaGlobalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sentenciaGlobal)
        try:
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.printt()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.asignacion()
                self.state = 86
                self.match(gramatica_finalParser.FINAL)
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


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPO(self):
            return self.getToken(gramatica_finalParser.TIPO, 0)

        def ID(self):
            return self.getToken(gramatica_finalParser.ID, 0)

        def PAI(self):
            return self.getToken(gramatica_finalParser.PAI, 0)

        def PAD(self):
            return self.getToken(gramatica_finalParser.PAD, 0)

        def bloque(self):
            return self.getTypedRuleContext(gramatica_finalParser.BloqueContext,0)


        def parametros(self):
            return self.getTypedRuleContext(gramatica_finalParser.ParametrosContext,0)


        def getRuleIndex(self):
            return gramatica_finalParser.RULE_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncion" ):
                return visitor.visitFuncion(self)
            else:
                return visitor.visitChildren(self)




    def funcion(self):

        localctx = gramatica_finalParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(gramatica_finalParser.TIPO)
            self.state = 91
            self.match(gramatica_finalParser.ID)
            self.state = 92
            self.match(gramatica_finalParser.PAI)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 93
                self.parametros()


            self.state = 96
            self.match(gramatica_finalParser.PAD)
            self.state = 97
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_finalParser.ParametroContext)
            else:
                return self.getTypedRuleContext(gramatica_finalParser.ParametroContext,i)


        def getRuleIndex(self):
            return gramatica_finalParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = gramatica_finalParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.parametro()
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 100
                self.match(gramatica_finalParser.T__1)
                self.state = 101
                self.parametro()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPO(self):
            return self.getToken(gramatica_finalParser.TIPO, 0)

        def ID(self):
            return self.getToken(gramatica_finalParser.ID, 0)

        def getRuleIndex(self):
            return gramatica_finalParser.RULE_parametro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametro" ):
                listener.enterParametro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametro" ):
                listener.exitParametro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametro" ):
                return visitor.visitParametro(self)
            else:
                return visitor.visitChildren(self)




    def parametro(self):

        localctx = gramatica_finalParser.ParametroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parametro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(gramatica_finalParser.TIPO)
            self.state = 108
            self.match(gramatica_finalParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPO(self):
            return self.getToken(gramatica_finalParser.TIPO, 0)

        def ID(self):
            return self.getToken(gramatica_finalParser.ID, 0)

        def ASIG(self):
            return self.getToken(gramatica_finalParser.ASIG, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramatica_finalParser.ExpresionContext,0)


        def FINAL(self):
            return self.getToken(gramatica_finalParser.FINAL, 0)

        def CORI(self):
            return self.getToken(gramatica_finalParser.CORI, 0)

        def CORD(self):
            return self.getToken(gramatica_finalParser.CORD, 0)

        def arrayLiteral(self):
            return self.getTypedRuleContext(gramatica_finalParser.ArrayLiteralContext,0)


        def getRuleIndex(self):
            return gramatica_finalParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = gramatica_finalParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_declaracion)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.match(gramatica_finalParser.TIPO)
                self.state = 111
                self.match(gramatica_finalParser.ID)
                self.state = 112
                self.match(gramatica_finalParser.ASIG)
                self.state = 113
                self.expresion()
                self.state = 114
                self.match(gramatica_finalParser.FINAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.match(gramatica_finalParser.TIPO)
                self.state = 117
                self.match(gramatica_finalParser.ID)
                self.state = 118
                self.match(gramatica_finalParser.FINAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.match(gramatica_finalParser.TIPO)
                self.state = 120
                self.match(gramatica_finalParser.CORI)
                self.state = 121
                self.match(gramatica_finalParser.CORD)
                self.state = 122
                self.match(gramatica_finalParser.ID)
                self.state = 123
                self.match(gramatica_finalParser.ASIG)
                self.state = 124
                self.arrayLiteral()
                self.state = 125
                self.match(gramatica_finalParser.FINAL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccesoArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramatica_finalParser.ID, 0)

        def CORI(self):
            return self.getToken(gramatica_finalParser.CORI, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramatica_finalParser.ExpresionContext,0)


        def CORD(self):
            return self.getToken(gramatica_finalParser.CORD, 0)

        def getRuleIndex(self):
            return gramatica_finalParser.RULE_accesoArray

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccesoArray" ):
                listener.enterAccesoArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccesoArray" ):
                listener.exitAccesoArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccesoArray" ):
                return visitor.visitAccesoArray(self)
            else:
                return visitor.visitChildren(self)




    def accesoArray(self):

        localctx = gramatica_finalParser.AccesoArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_accesoArray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(gramatica_finalParser.ID)
            self.state = 130
            self.match(gramatica_finalParser.CORI)
            self.state = 131
            self.expresion()
            self.state = 132
            self.match(gramatica_finalParser.CORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CORI(self):
            return self.getToken(gramatica_finalParser.CORI, 0)

        def CORD(self):
            return self.getToken(gramatica_finalParser.CORD, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_finalParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(gramatica_finalParser.ExpresionContext,i)


        def getRuleIndex(self):
            return gramatica_finalParser.RULE_arrayLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayLiteral" ):
                listener.enterArrayLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayLiteral" ):
                listener.exitArrayLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLiteral" ):
                return visitor.visitArrayLiteral(self)
            else:
                return visitor.visitChildren(self)




    def arrayLiteral(self):

        localctx = gramatica_finalParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(gramatica_finalParser.CORI)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8246472474624) != 0):
                self.state = 135
                self.expresion()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 136
                    self.match(gramatica_finalParser.T__1)
                    self.state = 137
                    self.expresion()
                    self.state = 142
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 145
            self.match(gramatica_finalParser.CORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(gramatica_finalParser.DeclaracionContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(gramatica_finalParser.AsignacionContext,0)


        def FINAL(self):
            return self.getToken(gramatica_finalParser.FINAL, 0)

        def expresionSi(self):
            return self.getTypedRuleContext(gramatica_finalParser.ExpresionSiContext,0)


        def printt(self):
            return self.getTypedRuleContext(gramatica_finalParser.PrinttContext,0)


        def cicloWhile(self):
            return self.getTypedRuleContext(gramatica_finalParser.CicloWhileContext,0)


        def cicloFor(self):
            return self.getTypedRuleContext(gramatica_finalParser.CicloForContext,0)


        def switchStmt(self):
            return self.getTypedRuleContext(gramatica_finalParser.SwitchStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(gramatica_finalParser.ReturnStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(gramatica_finalParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(gramatica_finalParser.ContinueStmtContext,0)


        def getRuleIndex(self):
            return gramatica_finalParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = gramatica_finalParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_sentencia)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.declaracion()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.asignacion()
                self.state = 149
                self.match(gramatica_finalParser.FINAL)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 151
                self.expresionSi()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 152
                self.printt()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 153
                self.cicloWhile()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 6)
                self.state = 154
                self.cicloFor()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 7)
                self.state = 155
                self.switchStmt()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 8)
                self.state = 156
                self.returnStmt()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 9)
                self.state = 157
                self.breakStmt()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 10)
                self.state = 158
                self.continueStmt()
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


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramatica_finalParser.ID, 0)

        def ASIG(self):
            return self.getToken(gramatica_finalParser.ASIG, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_finalParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(gramatica_finalParser.ExpresionContext,i)


        def CORI(self):
            return self.getToken(gramatica_finalParser.CORI, 0)

        def CORD(self):
            return self.getToken(gramatica_finalParser.CORD, 0)

        def getRuleIndex(self):
            return gramatica_finalParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = gramatica_finalParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_asignacion)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.match(gramatica_finalParser.ID)
                self.state = 162
                self.match(gramatica_finalParser.ASIG)
                self.state = 163
                self.expresion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.match(gramatica_finalParser.ID)
                self.state = 165
                self.match(gramatica_finalParser.CORI)
                self.state = 166
                self.expresion()
                self.state = 167
                self.match(gramatica_finalParser.CORD)
                self.state = 168
                self.match(gramatica_finalParser.ASIG)
                self.state = 169
                self.expresion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionSiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(gramatica_finalParser.SI, 0)

        def PAI(self):
            return self.getToken(gramatica_finalParser.PAI, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramatica_finalParser.ExpresionContext,0)


        def PAD(self):
            return self.getToken(gramatica_finalParser.PAD, 0)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_finalParser.BloqueContext)
            else:
                return self.getTypedRuleContext(gramatica_finalParser.BloqueContext,i)


        def SINO(self):
            return self.getToken(gramatica_finalParser.SINO, 0)

        def getRuleIndex(self):
            return gramatica_finalParser.RULE_expresionSi

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionSi" ):
                listener.enterExpresionSi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionSi" ):
                listener.exitExpresionSi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionSi" ):
                return visitor.visitExpresionSi(self)
            else:
                return visitor.visitChildren(self)




    def expresionSi(self):

        localctx = gramatica_finalParser.ExpresionSiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expresionSi)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(gramatica_finalParser.SI)
            self.state = 174
            self.match(gramatica_finalParser.PAI)
            self.state = 175
            self.expresion()
            self.state = 176
            self.match(gramatica_finalParser.PAD)
            self.state = 177
            self.bloque()
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 178
                self.match(gramatica_finalParser.SINO)
                self.state = 179
                self.bloque()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CicloWhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(gramatica_finalParser.WHILE, 0)

        def PAI(self):
            return self.getToken(gramatica_finalParser.PAI, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramatica_finalParser.ExpresionContext,0)


        def PAD(self):
            return self.getToken(gramatica_finalParser.PAD, 0)

        def bloque(self):
            return self.getTypedRuleContext(gramatica_finalParser.BloqueContext,0)


        def getRuleIndex(self):
            return gramatica_finalParser.RULE_cicloWhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCicloWhile" ):
                listener.enterCicloWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCicloWhile" ):
                listener.exitCicloWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCicloWhile" ):
                return visitor.visitCicloWhile(self)
            else:
                return visitor.visitChildren(self)




    def cicloWhile(self):

        localctx = gramatica_finalParser.CicloWhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_cicloWhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(gramatica_finalParser.WHILE)
            self.state = 183
            self.match(gramatica_finalParser.PAI)
            self.state = 184
            self.expresion()
            self.state = 185
            self.match(gramatica_finalParser.PAD)
            self.state = 186
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CicloForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(gramatica_finalParser.FOR, 0)

        def PAI(self):
            return self.getToken(gramatica_finalParser.PAI, 0)

        def FINAL(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_finalParser.FINAL)
            else:
                return self.getToken(gramatica_finalParser.FINAL, i)

        def expresion(self):
            return self.getTypedRuleContext(gramatica_finalParser.ExpresionContext,0)


        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_finalParser.AsignacionContext)
            else:
                return self.getTypedRuleContext(gramatica_finalParser.AsignacionContext,i)


        def PAD(self):
            return self.getToken(gramatica_finalParser.PAD, 0)

        def bloque(self):
            return self.getTypedRuleContext(gramatica_finalParser.BloqueContext,0)


        def declaracion(self):
            return self.getTypedRuleContext(gramatica_finalParser.DeclaracionContext,0)


        def getRuleIndex(self):
            return gramatica_finalParser.RULE_cicloFor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCicloFor" ):
                listener.enterCicloFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCicloFor" ):
                listener.exitCicloFor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCicloFor" ):
                return visitor.visitCicloFor(self)
            else:
                return visitor.visitChildren(self)




    def cicloFor(self):

        localctx = gramatica_finalParser.CicloForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_cicloFor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(gramatica_finalParser.FOR)
            self.state = 189
            self.match(gramatica_finalParser.PAI)
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.state = 190
                self.declaracion()
                pass
            elif token in [42]:
                self.state = 191
                self.asignacion()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 194
            self.match(gramatica_finalParser.FINAL)
            self.state = 195
            self.expresion()
            self.state = 196
            self.match(gramatica_finalParser.FINAL)
            self.state = 197
            self.asignacion()
            self.state = 198
            self.match(gramatica_finalParser.PAD)
            self.state = 199
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(gramatica_finalParser.SWITCH, 0)

        def PAI(self):
            return self.getToken(gramatica_finalParser.PAI, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramatica_finalParser.ExpresionContext,0)


        def PAD(self):
            return self.getToken(gramatica_finalParser.PAD, 0)

        def LLAVEI(self):
            return self.getToken(gramatica_finalParser.LLAVEI, 0)

        def LLAVED(self):
            return self.getToken(gramatica_finalParser.LLAVED, 0)

        def caseStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_finalParser.CaseStmtContext)
            else:
                return self.getTypedRuleContext(gramatica_finalParser.CaseStmtContext,i)


        def defaultStmt(self):
            return self.getTypedRuleContext(gramatica_finalParser.DefaultStmtContext,0)


        def getRuleIndex(self):
            return gramatica_finalParser.RULE_switchStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStmt" ):
                listener.enterSwitchStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStmt" ):
                listener.exitSwitchStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchStmt" ):
                return visitor.visitSwitchStmt(self)
            else:
                return visitor.visitChildren(self)




    def switchStmt(self):

        localctx = gramatica_finalParser.SwitchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_switchStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(gramatica_finalParser.SWITCH)
            self.state = 202
            self.match(gramatica_finalParser.PAI)
            self.state = 203
            self.expresion()
            self.state = 204
            self.match(gramatica_finalParser.PAD)
            self.state = 205
            self.match(gramatica_finalParser.LLAVEI)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 206
                self.caseStmt()
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 212
                self.defaultStmt()


            self.state = 215
            self.match(gramatica_finalParser.LLAVED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(gramatica_finalParser.CASE, 0)

        def NUM(self):
            return self.getToken(gramatica_finalParser.NUM, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_finalParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(gramatica_finalParser.SentenciaContext,i)


        def getRuleIndex(self):
            return gramatica_finalParser.RULE_caseStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseStmt" ):
                listener.enterCaseStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseStmt" ):
                listener.exitCaseStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseStmt" ):
                return visitor.visitCaseStmt(self)
            else:
                return visitor.visitChildren(self)




    def caseStmt(self):

        localctx = gramatica_finalParser.CaseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_caseStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(gramatica_finalParser.CASE)
            self.state = 218
            self.match(gramatica_finalParser.NUM)
            self.state = 219
            self.match(gramatica_finalParser.T__2)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398046674224) != 0):
                self.state = 220
                self.sentencia()
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(gramatica_finalParser.DEFAULT, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_finalParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(gramatica_finalParser.SentenciaContext,i)


        def getRuleIndex(self):
            return gramatica_finalParser.RULE_defaultStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultStmt" ):
                listener.enterDefaultStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultStmt" ):
                listener.exitDefaultStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefaultStmt" ):
                return visitor.visitDefaultStmt(self)
            else:
                return visitor.visitChildren(self)




    def defaultStmt(self):

        localctx = gramatica_finalParser.DefaultStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_defaultStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(gramatica_finalParser.DEFAULT)
            self.state = 227
            self.match(gramatica_finalParser.T__2)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398046674224) != 0):
                self.state = 228
                self.sentencia()
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINAL(self):
            return self.getToken(gramatica_finalParser.FINAL, 0)

        def getRuleIndex(self):
            return gramatica_finalParser.RULE_breakStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStmt" ):
                listener.enterBreakStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStmt" ):
                listener.exitBreakStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = gramatica_finalParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(gramatica_finalParser.T__3)
            self.state = 235
            self.match(gramatica_finalParser.FINAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINAL(self):
            return self.getToken(gramatica_finalParser.FINAL, 0)

        def getRuleIndex(self):
            return gramatica_finalParser.RULE_continueStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStmt" ):
                listener.enterContinueStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStmt" ):
                listener.exitContinueStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStmt" ):
                return visitor.visitContinueStmt(self)
            else:
                return visitor.visitChildren(self)




    def continueStmt(self):

        localctx = gramatica_finalParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(gramatica_finalParser.T__4)
            self.state = 238
            self.match(gramatica_finalParser.FINAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLAVEI(self):
            return self.getToken(gramatica_finalParser.LLAVEI, 0)

        def LLAVED(self):
            return self.getToken(gramatica_finalParser.LLAVED, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_finalParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(gramatica_finalParser.SentenciaContext,i)


        def getRuleIndex(self):
            return gramatica_finalParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = gramatica_finalParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(gramatica_finalParser.LLAVEI)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398046674224) != 0):
                self.state = 241
                self.sentencia()
                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 247
            self.match(gramatica_finalParser.LLAVED)
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

        def comparacion(self):
            return self.getTypedRuleContext(gramatica_finalParser.ComparacionContext,0)


        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_finalParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(gramatica_finalParser.ExpresionContext,i)


        def getRuleIndex(self):
            return gramatica_finalParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)




    def expresion(self):

        localctx = gramatica_finalParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.comparacion()
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 250
                self.match(gramatica_finalParser.T__5)
                self.state = 251
                self.expresion()
                self.state = 252
                self.match(gramatica_finalParser.T__2)
                self.state = 253
                self.expresion()


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
                return self.getTypedRuleContexts(gramatica_finalParser.SumaContext)
            else:
                return self.getTypedRuleContext(gramatica_finalParser.SumaContext,i)


        def MAYOR(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_finalParser.MAYOR)
            else:
                return self.getToken(gramatica_finalParser.MAYOR, i)

        def MENOR(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_finalParser.MENOR)
            else:
                return self.getToken(gramatica_finalParser.MENOR, i)

        def MAYORI(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_finalParser.MAYORI)
            else:
                return self.getToken(gramatica_finalParser.MAYORI, i)

        def MENORI(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_finalParser.MENORI)
            else:
                return self.getToken(gramatica_finalParser.MENORI, i)

        def IGUAL(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_finalParser.IGUAL)
            else:
                return self.getToken(gramatica_finalParser.IGUAL, i)

        def NOIGUAL(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_finalParser.NOIGUAL)
            else:
                return self.getToken(gramatica_finalParser.NOIGUAL, i)

        def getRuleIndex(self):
            return gramatica_finalParser.RULE_comparacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparacion" ):
                listener.enterComparacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparacion" ):
                listener.exitComparacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparacion" ):
                return visitor.visitComparacion(self)
            else:
                return visitor.visitChildren(self)




    def comparacion(self):

        localctx = gramatica_finalParser.ComparacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_comparacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.suma()
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 135291469824) != 0):
                self.state = 258
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 135291469824) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 259
                self.suma()
                self.state = 264
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

        def termino(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_finalParser.TerminoContext)
            else:
                return self.getTypedRuleContext(gramatica_finalParser.TerminoContext,i)


        def SUM(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_finalParser.SUM)
            else:
                return self.getToken(gramatica_finalParser.SUM, i)

        def RES(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_finalParser.RES)
            else:
                return self.getToken(gramatica_finalParser.RES, i)

        def getRuleIndex(self):
            return gramatica_finalParser.RULE_suma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuma" ):
                listener.enterSuma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuma" ):
                listener.exitSuma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuma" ):
                return visitor.visitSuma(self)
            else:
                return visitor.visitChildren(self)




    def suma(self):

        localctx = gramatica_finalParser.SumaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_suma)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.termino()
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26 or _la==27:
                self.state = 266
                _la = self._input.LA(1)
                if not(_la==26 or _la==27):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 267
                self.termino()
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_finalParser.FactorContext)
            else:
                return self.getTypedRuleContext(gramatica_finalParser.FactorContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_finalParser.MUL)
            else:
                return self.getToken(gramatica_finalParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_finalParser.DIV)
            else:
                return self.getToken(gramatica_finalParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_finalParser.MOD)
            else:
                return self.getToken(gramatica_finalParser.MOD, i)

        def getRuleIndex(self):
            return gramatica_finalParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermino" ):
                return visitor.visitTermino(self)
            else:
                return visitor.visitChildren(self)




    def termino(self):

        localctx = gramatica_finalParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.factor()
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1879048192) != 0):
                self.state = 274
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1879048192) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 275
                self.factor()
                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(gramatica_finalParser.NUM, 0)

        def STRING(self):
            return self.getToken(gramatica_finalParser.STRING, 0)

        def llamadaFuncion(self):
            return self.getTypedRuleContext(gramatica_finalParser.LlamadaFuncionContext,0)


        def ID(self):
            return self.getToken(gramatica_finalParser.ID, 0)

        def CORI(self):
            return self.getToken(gramatica_finalParser.CORI, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramatica_finalParser.ExpresionContext,0)


        def CORD(self):
            return self.getToken(gramatica_finalParser.CORD, 0)

        def PAI(self):
            return self.getToken(gramatica_finalParser.PAI, 0)

        def PAD(self):
            return self.getToken(gramatica_finalParser.PAD, 0)

        def NOT(self):
            return self.getToken(gramatica_finalParser.NOT, 0)

        def factor(self):
            return self.getTypedRuleContext(gramatica_finalParser.FactorContext,0)


        def RES(self):
            return self.getToken(gramatica_finalParser.RES, 0)

        def getRuleIndex(self):
            return gramatica_finalParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = gramatica_finalParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_factor)
        try:
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.match(gramatica_finalParser.NUM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.match(gramatica_finalParser.STRING)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 283
                self.llamadaFuncion()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 284
                self.match(gramatica_finalParser.ID)
                self.state = 285
                self.match(gramatica_finalParser.CORI)
                self.state = 286
                self.expresion()
                self.state = 287
                self.match(gramatica_finalParser.CORD)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 289
                self.match(gramatica_finalParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 290
                self.match(gramatica_finalParser.PAI)
                self.state = 291
                self.expresion()
                self.state = 292
                self.match(gramatica_finalParser.PAD)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 294
                self.match(gramatica_finalParser.NOT)
                self.state = 295
                self.factor()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 296
                self.match(gramatica_finalParser.RES)
                self.state = 297
                self.factor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamadaFuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramatica_finalParser.ID, 0)

        def PAI(self):
            return self.getToken(gramatica_finalParser.PAI, 0)

        def PAD(self):
            return self.getToken(gramatica_finalParser.PAD, 0)

        def argumentos(self):
            return self.getTypedRuleContext(gramatica_finalParser.ArgumentosContext,0)


        def getRuleIndex(self):
            return gramatica_finalParser.RULE_llamadaFuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamadaFuncion" ):
                listener.enterLlamadaFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamadaFuncion" ):
                listener.exitLlamadaFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamadaFuncion" ):
                return visitor.visitLlamadaFuncion(self)
            else:
                return visitor.visitChildren(self)




    def llamadaFuncion(self):

        localctx = gramatica_finalParser.LlamadaFuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_llamadaFuncion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(gramatica_finalParser.ID)
            self.state = 301
            self.match(gramatica_finalParser.PAI)
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8246472474624) != 0):
                self.state = 302
                self.argumentos()


            self.state = 305
            self.match(gramatica_finalParser.PAD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_finalParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(gramatica_finalParser.ExpresionContext,i)


        def getRuleIndex(self):
            return gramatica_finalParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos" ):
                return visitor.visitArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def argumentos(self):

        localctx = gramatica_finalParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_argumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.expresion()
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 308
                self.match(gramatica_finalParser.T__1)
                self.state = 309
                self.expresion()
                self.state = 314
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(gramatica_finalParser.RETURN, 0)

        def FINAL(self):
            return self.getToken(gramatica_finalParser.FINAL, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramatica_finalParser.ExpresionContext,0)


        def getRuleIndex(self):
            return gramatica_finalParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = gramatica_finalParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(gramatica_finalParser.RETURN)
            self.state = 317
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8246472474624) != 0):
                self.state = 316
                self.expresion()


            self.state = 319
            self.match(gramatica_finalParser.FINAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrinttContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(gramatica_finalParser.PRINT, 0)

        def PAI(self):
            return self.getToken(gramatica_finalParser.PAI, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramatica_finalParser.ExpresionContext,0)


        def PAD(self):
            return self.getToken(gramatica_finalParser.PAD, 0)

        def FINAL(self):
            return self.getToken(gramatica_finalParser.FINAL, 0)

        def getRuleIndex(self):
            return gramatica_finalParser.RULE_printt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintt" ):
                listener.enterPrintt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintt" ):
                listener.exitPrintt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintt" ):
                return visitor.visitPrintt(self)
            else:
                return visitor.visitChildren(self)




    def printt(self):

        localctx = gramatica_finalParser.PrinttContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_printt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(gramatica_finalParser.PRINT)
            self.state = 322
            self.match(gramatica_finalParser.PAI)
            self.state = 323
            self.expresion()
            self.state = 324
            self.match(gramatica_finalParser.PAD)
            self.state = 325
            self.match(gramatica_finalParser.FINAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






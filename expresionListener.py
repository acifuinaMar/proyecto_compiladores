# Generated from expresion.g by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .expresionParser import expresionParser
else:
    from expresionParser import expresionParser

# This class defines a complete listener for a parse tree produced by expresionParser.
class expresionListener(ParseTreeListener):

    # Enter a parse tree produced by expresionParser#root.
    def enterRoot(self, ctx:expresionParser.RootContext):
        pass

    # Exit a parse tree produced by expresionParser#root.
    def exitRoot(self, ctx:expresionParser.RootContext):
        pass


    # Enter a parse tree produced by expresionParser#expresion.
    def enterExpresion(self, ctx:expresionParser.ExpresionContext):
        pass

    # Exit a parse tree produced by expresionParser#expresion.
    def exitExpresion(self, ctx:expresionParser.ExpresionContext):
        pass


    # Enter a parse tree produced by expresionParser#orLogico.
    def enterOrLogico(self, ctx:expresionParser.OrLogicoContext):
        pass

    # Exit a parse tree produced by expresionParser#orLogico.
    def exitOrLogico(self, ctx:expresionParser.OrLogicoContext):
        pass


    # Enter a parse tree produced by expresionParser#andLogico.
    def enterAndLogico(self, ctx:expresionParser.AndLogicoContext):
        pass

    # Exit a parse tree produced by expresionParser#andLogico.
    def exitAndLogico(self, ctx:expresionParser.AndLogicoContext):
        pass


    # Enter a parse tree produced by expresionParser#igualdad.
    def enterIgualdad(self, ctx:expresionParser.IgualdadContext):
        pass

    # Exit a parse tree produced by expresionParser#igualdad.
    def exitIgualdad(self, ctx:expresionParser.IgualdadContext):
        pass


    # Enter a parse tree produced by expresionParser#comparacion.
    def enterComparacion(self, ctx:expresionParser.ComparacionContext):
        pass

    # Exit a parse tree produced by expresionParser#comparacion.
    def exitComparacion(self, ctx:expresionParser.ComparacionContext):
        pass


    # Enter a parse tree produced by expresionParser#suma.
    def enterSuma(self, ctx:expresionParser.SumaContext):
        pass

    # Exit a parse tree produced by expresionParser#suma.
    def exitSuma(self, ctx:expresionParser.SumaContext):
        pass


    # Enter a parse tree produced by expresionParser#multiplicacion.
    def enterMultiplicacion(self, ctx:expresionParser.MultiplicacionContext):
        pass

    # Exit a parse tree produced by expresionParser#multiplicacion.
    def exitMultiplicacion(self, ctx:expresionParser.MultiplicacionContext):
        pass


    # Enter a parse tree produced by expresionParser#unario.
    def enterUnario(self, ctx:expresionParser.UnarioContext):
        pass

    # Exit a parse tree produced by expresionParser#unario.
    def exitUnario(self, ctx:expresionParser.UnarioContext):
        pass


    # Enter a parse tree produced by expresionParser#base.
    def enterBase(self, ctx:expresionParser.BaseContext):
        pass

    # Exit a parse tree produced by expresionParser#base.
    def exitBase(self, ctx:expresionParser.BaseContext):
        pass



del expresionParser
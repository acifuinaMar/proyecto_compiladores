# Generated from expresion.g by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .expresionParser import expresionParser
else:
    from expresionParser import expresionParser

# This class defines a complete generic visitor for a parse tree produced by expresionParser.

class expresionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by expresionParser#root.
    def visitRoot(self, ctx:expresionParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expresionParser#sentencia.
    def visitSentencia(self, ctx:expresionParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expresionParser#asignacion.
    def visitAsignacion(self, ctx:expresionParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expresionParser#expresionSi.
    def visitExpresionSi(self, ctx:expresionParser.ExpresionSiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expresionParser#bloque.
    def visitBloque(self, ctx:expresionParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expresionParser#expresion.
    def visitExpresion(self, ctx:expresionParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expresionParser#orLogico.
    def visitOrLogico(self, ctx:expresionParser.OrLogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expresionParser#andLogico.
    def visitAndLogico(self, ctx:expresionParser.AndLogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expresionParser#igualdad.
    def visitIgualdad(self, ctx:expresionParser.IgualdadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expresionParser#comparacion.
    def visitComparacion(self, ctx:expresionParser.ComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expresionParser#suma.
    def visitSuma(self, ctx:expresionParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expresionParser#multiplicacion.
    def visitMultiplicacion(self, ctx:expresionParser.MultiplicacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expresionParser#unico.
    def visitUnico(self, ctx:expresionParser.UnicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expresionParser#base.
    def visitBase(self, ctx:expresionParser.BaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expresionParser#declaracion.
    def visitDeclaracion(self, ctx:expresionParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expresionParser#printt.
    def visitPrintt(self, ctx:expresionParser.PrinttContext):
        return self.visitChildren(ctx)



del expresionParser
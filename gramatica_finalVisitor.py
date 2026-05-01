# Generated from gramatica_final.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramatica_finalParser import gramatica_finalParser
else:
    from gramatica_finalParser import gramatica_finalParser

# This class defines a complete generic visitor for a parse tree produced by gramatica_finalParser.

class gramatica_finalVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramatica_finalParser#root.
    def visitRoot(self, ctx:gramatica_finalParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#programa.
    def visitPrograma(self, ctx:gramatica_finalParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#importStmt.
    def visitImportStmt(self, ctx:gramatica_finalParser.ImportStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#sentenciaGlobal.
    def visitSentenciaGlobal(self, ctx:gramatica_finalParser.SentenciaGlobalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#funcion.
    def visitFuncion(self, ctx:gramatica_finalParser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#parametros.
    def visitParametros(self, ctx:gramatica_finalParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#parametro.
    def visitParametro(self, ctx:gramatica_finalParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#declaracion.
    def visitDeclaracion(self, ctx:gramatica_finalParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#arrayLiteral.
    def visitArrayLiteral(self, ctx:gramatica_finalParser.ArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#sentencia.
    def visitSentencia(self, ctx:gramatica_finalParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#asignacion.
    def visitAsignacion(self, ctx:gramatica_finalParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#expresionSi.
    def visitExpresionSi(self, ctx:gramatica_finalParser.ExpresionSiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#cicloWhile.
    def visitCicloWhile(self, ctx:gramatica_finalParser.CicloWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#cicloFor.
    def visitCicloFor(self, ctx:gramatica_finalParser.CicloForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#breakStmt.
    def visitBreakStmt(self, ctx:gramatica_finalParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#continueStmt.
    def visitContinueStmt(self, ctx:gramatica_finalParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#bloque.
    def visitBloque(self, ctx:gramatica_finalParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#expresion.
    def visitExpresion(self, ctx:gramatica_finalParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#comparacion.
    def visitComparacion(self, ctx:gramatica_finalParser.ComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#suma.
    def visitSuma(self, ctx:gramatica_finalParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#termino.
    def visitTermino(self, ctx:gramatica_finalParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#factor.
    def visitFactor(self, ctx:gramatica_finalParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#llamadaFuncion.
    def visitLlamadaFuncion(self, ctx:gramatica_finalParser.LlamadaFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#argumentos.
    def visitArgumentos(self, ctx:gramatica_finalParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#returnStmt.
    def visitReturnStmt(self, ctx:gramatica_finalParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_finalParser#printt.
    def visitPrintt(self, ctx:gramatica_finalParser.PrinttContext):
        return self.visitChildren(ctx)



del gramatica_finalParser
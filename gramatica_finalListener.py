# Generated from gramatica_final.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramatica_finalParser import gramatica_finalParser
else:
    from gramatica_finalParser import gramatica_finalParser

# This class defines a complete listener for a parse tree produced by gramatica_finalParser.
class gramatica_finalListener(ParseTreeListener):

    # Enter a parse tree produced by gramatica_finalParser#root.
    def enterRoot(self, ctx:gramatica_finalParser.RootContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#root.
    def exitRoot(self, ctx:gramatica_finalParser.RootContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#programa.
    def enterPrograma(self, ctx:gramatica_finalParser.ProgramaContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#programa.
    def exitPrograma(self, ctx:gramatica_finalParser.ProgramaContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#importStmt.
    def enterImportStmt(self, ctx:gramatica_finalParser.ImportStmtContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#importStmt.
    def exitImportStmt(self, ctx:gramatica_finalParser.ImportStmtContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#sentenciaGlobal.
    def enterSentenciaGlobal(self, ctx:gramatica_finalParser.SentenciaGlobalContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#sentenciaGlobal.
    def exitSentenciaGlobal(self, ctx:gramatica_finalParser.SentenciaGlobalContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#funcion.
    def enterFuncion(self, ctx:gramatica_finalParser.FuncionContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#funcion.
    def exitFuncion(self, ctx:gramatica_finalParser.FuncionContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#parametros.
    def enterParametros(self, ctx:gramatica_finalParser.ParametrosContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#parametros.
    def exitParametros(self, ctx:gramatica_finalParser.ParametrosContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#parametro.
    def enterParametro(self, ctx:gramatica_finalParser.ParametroContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#parametro.
    def exitParametro(self, ctx:gramatica_finalParser.ParametroContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#declaracion.
    def enterDeclaracion(self, ctx:gramatica_finalParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#declaracion.
    def exitDeclaracion(self, ctx:gramatica_finalParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#arrayLiteral.
    def enterArrayLiteral(self, ctx:gramatica_finalParser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#arrayLiteral.
    def exitArrayLiteral(self, ctx:gramatica_finalParser.ArrayLiteralContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#sentencia.
    def enterSentencia(self, ctx:gramatica_finalParser.SentenciaContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#sentencia.
    def exitSentencia(self, ctx:gramatica_finalParser.SentenciaContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#asignacion.
    def enterAsignacion(self, ctx:gramatica_finalParser.AsignacionContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#asignacion.
    def exitAsignacion(self, ctx:gramatica_finalParser.AsignacionContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#expresionSi.
    def enterExpresionSi(self, ctx:gramatica_finalParser.ExpresionSiContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#expresionSi.
    def exitExpresionSi(self, ctx:gramatica_finalParser.ExpresionSiContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#cicloWhile.
    def enterCicloWhile(self, ctx:gramatica_finalParser.CicloWhileContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#cicloWhile.
    def exitCicloWhile(self, ctx:gramatica_finalParser.CicloWhileContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#cicloFor.
    def enterCicloFor(self, ctx:gramatica_finalParser.CicloForContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#cicloFor.
    def exitCicloFor(self, ctx:gramatica_finalParser.CicloForContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#breakStmt.
    def enterBreakStmt(self, ctx:gramatica_finalParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#breakStmt.
    def exitBreakStmt(self, ctx:gramatica_finalParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#continueStmt.
    def enterContinueStmt(self, ctx:gramatica_finalParser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#continueStmt.
    def exitContinueStmt(self, ctx:gramatica_finalParser.ContinueStmtContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#bloque.
    def enterBloque(self, ctx:gramatica_finalParser.BloqueContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#bloque.
    def exitBloque(self, ctx:gramatica_finalParser.BloqueContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#expresion.
    def enterExpresion(self, ctx:gramatica_finalParser.ExpresionContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#expresion.
    def exitExpresion(self, ctx:gramatica_finalParser.ExpresionContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#comparacion.
    def enterComparacion(self, ctx:gramatica_finalParser.ComparacionContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#comparacion.
    def exitComparacion(self, ctx:gramatica_finalParser.ComparacionContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#suma.
    def enterSuma(self, ctx:gramatica_finalParser.SumaContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#suma.
    def exitSuma(self, ctx:gramatica_finalParser.SumaContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#termino.
    def enterTermino(self, ctx:gramatica_finalParser.TerminoContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#termino.
    def exitTermino(self, ctx:gramatica_finalParser.TerminoContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#factor.
    def enterFactor(self, ctx:gramatica_finalParser.FactorContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#factor.
    def exitFactor(self, ctx:gramatica_finalParser.FactorContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#llamadaFuncion.
    def enterLlamadaFuncion(self, ctx:gramatica_finalParser.LlamadaFuncionContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#llamadaFuncion.
    def exitLlamadaFuncion(self, ctx:gramatica_finalParser.LlamadaFuncionContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#argumentos.
    def enterArgumentos(self, ctx:gramatica_finalParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#argumentos.
    def exitArgumentos(self, ctx:gramatica_finalParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#returnStmt.
    def enterReturnStmt(self, ctx:gramatica_finalParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#returnStmt.
    def exitReturnStmt(self, ctx:gramatica_finalParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by gramatica_finalParser#printt.
    def enterPrintt(self, ctx:gramatica_finalParser.PrinttContext):
        pass

    # Exit a parse tree produced by gramatica_finalParser#printt.
    def exitPrintt(self, ctx:gramatica_finalParser.PrinttContext):
        pass



del gramatica_finalParser
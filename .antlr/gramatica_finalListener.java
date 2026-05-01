// Generated from /home/jimmmy/proyecto_compiladores/gramatica_final.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link gramatica_finalParser}.
 */
public interface gramatica_finalListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link gramatica_finalParser#root}.
	 * @param ctx the parse tree
	 */
	void enterRoot(gramatica_finalParser.RootContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_finalParser#root}.
	 * @param ctx the parse tree
	 */
	void exitRoot(gramatica_finalParser.RootContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_finalParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(gramatica_finalParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_finalParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(gramatica_finalParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_finalParser#sentenciaGlobal}.
	 * @param ctx the parse tree
	 */
	void enterSentenciaGlobal(gramatica_finalParser.SentenciaGlobalContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_finalParser#sentenciaGlobal}.
	 * @param ctx the parse tree
	 */
	void exitSentenciaGlobal(gramatica_finalParser.SentenciaGlobalContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_finalParser#funcion}.
	 * @param ctx the parse tree
	 */
	void enterFuncion(gramatica_finalParser.FuncionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_finalParser#funcion}.
	 * @param ctx the parse tree
	 */
	void exitFuncion(gramatica_finalParser.FuncionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_finalParser#parametros}.
	 * @param ctx the parse tree
	 */
	void enterParametros(gramatica_finalParser.ParametrosContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_finalParser#parametros}.
	 * @param ctx the parse tree
	 */
	void exitParametros(gramatica_finalParser.ParametrosContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_finalParser#parametro}.
	 * @param ctx the parse tree
	 */
	void enterParametro(gramatica_finalParser.ParametroContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_finalParser#parametro}.
	 * @param ctx the parse tree
	 */
	void exitParametro(gramatica_finalParser.ParametroContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_finalParser#declaracion}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracion(gramatica_finalParser.DeclaracionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_finalParser#declaracion}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracion(gramatica_finalParser.DeclaracionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_finalParser#sentencia}.
	 * @param ctx the parse tree
	 */
	void enterSentencia(gramatica_finalParser.SentenciaContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_finalParser#sentencia}.
	 * @param ctx the parse tree
	 */
	void exitSentencia(gramatica_finalParser.SentenciaContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_finalParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void enterAsignacion(gramatica_finalParser.AsignacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_finalParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void exitAsignacion(gramatica_finalParser.AsignacionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_finalParser#expresionSi}.
	 * @param ctx the parse tree
	 */
	void enterExpresionSi(gramatica_finalParser.ExpresionSiContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_finalParser#expresionSi}.
	 * @param ctx the parse tree
	 */
	void exitExpresionSi(gramatica_finalParser.ExpresionSiContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_finalParser#cicloWhile}.
	 * @param ctx the parse tree
	 */
	void enterCicloWhile(gramatica_finalParser.CicloWhileContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_finalParser#cicloWhile}.
	 * @param ctx the parse tree
	 */
	void exitCicloWhile(gramatica_finalParser.CicloWhileContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_finalParser#cicloFor}.
	 * @param ctx the parse tree
	 */
	void enterCicloFor(gramatica_finalParser.CicloForContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_finalParser#cicloFor}.
	 * @param ctx the parse tree
	 */
	void exitCicloFor(gramatica_finalParser.CicloForContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_finalParser#bloque}.
	 * @param ctx the parse tree
	 */
	void enterBloque(gramatica_finalParser.BloqueContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_finalParser#bloque}.
	 * @param ctx the parse tree
	 */
	void exitBloque(gramatica_finalParser.BloqueContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_finalParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterExpresion(gramatica_finalParser.ExpresionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_finalParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitExpresion(gramatica_finalParser.ExpresionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_finalParser#comparacion}.
	 * @param ctx the parse tree
	 */
	void enterComparacion(gramatica_finalParser.ComparacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_finalParser#comparacion}.
	 * @param ctx the parse tree
	 */
	void exitComparacion(gramatica_finalParser.ComparacionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_finalParser#suma}.
	 * @param ctx the parse tree
	 */
	void enterSuma(gramatica_finalParser.SumaContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_finalParser#suma}.
	 * @param ctx the parse tree
	 */
	void exitSuma(gramatica_finalParser.SumaContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_finalParser#termino}.
	 * @param ctx the parse tree
	 */
	void enterTermino(gramatica_finalParser.TerminoContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_finalParser#termino}.
	 * @param ctx the parse tree
	 */
	void exitTermino(gramatica_finalParser.TerminoContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_finalParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(gramatica_finalParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_finalParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(gramatica_finalParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_finalParser#llamadaFuncion}.
	 * @param ctx the parse tree
	 */
	void enterLlamadaFuncion(gramatica_finalParser.LlamadaFuncionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_finalParser#llamadaFuncion}.
	 * @param ctx the parse tree
	 */
	void exitLlamadaFuncion(gramatica_finalParser.LlamadaFuncionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_finalParser#argumentos}.
	 * @param ctx the parse tree
	 */
	void enterArgumentos(gramatica_finalParser.ArgumentosContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_finalParser#argumentos}.
	 * @param ctx the parse tree
	 */
	void exitArgumentos(gramatica_finalParser.ArgumentosContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_finalParser#returnStmt}.
	 * @param ctx the parse tree
	 */
	void enterReturnStmt(gramatica_finalParser.ReturnStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_finalParser#returnStmt}.
	 * @param ctx the parse tree
	 */
	void exitReturnStmt(gramatica_finalParser.ReturnStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_finalParser#printt}.
	 * @param ctx the parse tree
	 */
	void enterPrintt(gramatica_finalParser.PrinttContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_finalParser#printt}.
	 * @param ctx the parse tree
	 */
	void exitPrintt(gramatica_finalParser.PrinttContext ctx);
}
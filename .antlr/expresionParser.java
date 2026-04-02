// Generated from /home/jimmmy/proyecto_compiladores/expresion.g by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class expresionParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PROGRAM=1, SI=2, SINO=3, WHILE=4, FOR=5, LLAVEI=6, LLAVED=7, PAI=8, PAD=9, 
		ASIG=10, SUM=11, RES=12, MUL=13, DIV=14, IGUAL=15, NOIGUAL=16, MENOR=17, 
		MAYOR=18, MENORI=19, MAYORI=20, AND=21, OR=22, NOT=23, PRINT=24, TIPO=25, 
		VERDADERO=26, FALSO=27, STRING=28, FLOAT=29, NUM=30, ID=31, FINAL=32, 
		WS=33;
	public static final int
		RULE_root = 0, RULE_sentencia = 1, RULE_asignacion = 2, RULE_expresionSi = 3, 
		RULE_cicloWhile = 4, RULE_cicloFor = 5, RULE_bloque = 6, RULE_expresion = 7, 
		RULE_orLogico = 8, RULE_andLogico = 9, RULE_igualdad = 10, RULE_comparacion = 11, 
		RULE_suma = 12, RULE_multiplicacion = 13, RULE_unico = 14, RULE_base = 15, 
		RULE_declaracion = 16, RULE_printt = 17;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "sentencia", "asignacion", "expresionSi", "cicloWhile", "cicloFor", 
			"bloque", "expresion", "orLogico", "andLogico", "igualdad", "comparacion", 
			"suma", "multiplicacion", "unico", "base", "declaracion", "printt"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'program'", "'si'", "'sino'", "'while'", "'for'", "'{'", "'}'", 
			"'('", "')'", "'='", "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", "'<'", 
			"'>'", "'<='", "'>='", "'&&'", "'||'", "'!'", "'print'", null, "'verdadero'", 
			"'falso'", null, null, null, null, "';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROGRAM", "SI", "SINO", "WHILE", "FOR", "LLAVEI", "LLAVED", "PAI", 
			"PAD", "ASIG", "SUM", "RES", "MUL", "DIV", "IGUAL", "NOIGUAL", "MENOR", 
			"MAYOR", "MENORI", "MAYORI", "AND", "OR", "NOT", "PRINT", "TIPO", "VERDADERO", 
			"FALSO", "STRING", "FLOAT", "NUM", "ID", "FINAL", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "expresion.g"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public expresionParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RootContext extends ParserRuleContext {
		public TerminalNode PROGRAM() { return getToken(expresionParser.PROGRAM, 0); }
		public TerminalNode LLAVEI() { return getToken(expresionParser.LLAVEI, 0); }
		public TerminalNode LLAVED() { return getToken(expresionParser.LLAVED, 0); }
		public TerminalNode EOF() { return getToken(expresionParser.EOF, 0); }
		public List<SentenciaContext> sentencia() {
			return getRuleContexts(SentenciaContext.class);
		}
		public SentenciaContext sentencia(int i) {
			return getRuleContext(SentenciaContext.class,i);
		}
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			match(PROGRAM);
			setState(37);
			match(LLAVEI);
			setState(41);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4286578996L) != 0)) {
				{
				{
				setState(38);
				sentencia();
				}
				}
				setState(43);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(44);
			match(LLAVED);
			setState(45);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SentenciaContext extends ParserRuleContext {
		public DeclaracionContext declaracion() {
			return getRuleContext(DeclaracionContext.class,0);
		}
		public AsignacionContext asignacion() {
			return getRuleContext(AsignacionContext.class,0);
		}
		public TerminalNode FINAL() { return getToken(expresionParser.FINAL, 0); }
		public ExpresionSiContext expresionSi() {
			return getRuleContext(ExpresionSiContext.class,0);
		}
		public PrinttContext printt() {
			return getRuleContext(PrinttContext.class,0);
		}
		public CicloWhileContext cicloWhile() {
			return getRuleContext(CicloWhileContext.class,0);
		}
		public CicloForContext cicloFor() {
			return getRuleContext(CicloForContext.class,0);
		}
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public SentenciaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentencia; }
	}

	public final SentenciaContext sentencia() throws RecognitionException {
		SentenciaContext _localctx = new SentenciaContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_sentencia);
		try {
			setState(58);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(47);
				declaracion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(48);
				asignacion();
				setState(49);
				match(FINAL);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(51);
				expresionSi();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(52);
				printt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(53);
				cicloWhile();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(54);
				cicloFor();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(55);
				expresion();
				setState(56);
				match(FINAL);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AsignacionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(expresionParser.ID, 0); }
		public TerminalNode ASIG() { return getToken(expresionParser.ASIG, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public AsignacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion; }
	}

	public final AsignacionContext asignacion() throws RecognitionException {
		AsignacionContext _localctx = new AsignacionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_asignacion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			match(ID);
			setState(61);
			match(ASIG);
			setState(62);
			expresion();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpresionSiContext extends ParserRuleContext {
		public TerminalNode SI() { return getToken(expresionParser.SI, 0); }
		public TerminalNode PAI() { return getToken(expresionParser.PAI, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode PAD() { return getToken(expresionParser.PAD, 0); }
		public List<BloqueContext> bloque() {
			return getRuleContexts(BloqueContext.class);
		}
		public BloqueContext bloque(int i) {
			return getRuleContext(BloqueContext.class,i);
		}
		public TerminalNode SINO() { return getToken(expresionParser.SINO, 0); }
		public ExpresionSiContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresionSi; }
	}

	public final ExpresionSiContext expresionSi() throws RecognitionException {
		ExpresionSiContext _localctx = new ExpresionSiContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_expresionSi);
		try {
			setState(78);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(64);
				match(SI);
				setState(65);
				match(PAI);
				setState(66);
				expresion();
				setState(67);
				match(PAD);
				setState(68);
				bloque();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(70);
				match(SI);
				setState(71);
				match(PAI);
				setState(72);
				expresion();
				setState(73);
				match(PAD);
				setState(74);
				bloque();
				setState(75);
				match(SINO);
				setState(76);
				bloque();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CicloWhileContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(expresionParser.WHILE, 0); }
		public TerminalNode PAI() { return getToken(expresionParser.PAI, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode PAD() { return getToken(expresionParser.PAD, 0); }
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public CicloWhileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cicloWhile; }
	}

	public final CicloWhileContext cicloWhile() throws RecognitionException {
		CicloWhileContext _localctx = new CicloWhileContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_cicloWhile);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			match(WHILE);
			setState(81);
			match(PAI);
			setState(82);
			expresion();
			setState(83);
			match(PAD);
			setState(84);
			bloque();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CicloForContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(expresionParser.FOR, 0); }
		public TerminalNode PAI() { return getToken(expresionParser.PAI, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode FINAL() { return getToken(expresionParser.FINAL, 0); }
		public List<AsignacionContext> asignacion() {
			return getRuleContexts(AsignacionContext.class);
		}
		public AsignacionContext asignacion(int i) {
			return getRuleContext(AsignacionContext.class,i);
		}
		public TerminalNode PAD() { return getToken(expresionParser.PAD, 0); }
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public DeclaracionContext declaracion() {
			return getRuleContext(DeclaracionContext.class,0);
		}
		public CicloForContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cicloFor; }
	}

	public final CicloForContext cicloFor() throws RecognitionException {
		CicloForContext _localctx = new CicloForContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_cicloFor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			match(FOR);
			setState(87);
			match(PAI);
			setState(90);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TIPO:
				{
				setState(88);
				declaracion();
				}
				break;
			case ID:
				{
				setState(89);
				asignacion();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(92);
			expresion();
			setState(93);
			match(FINAL);
			setState(94);
			asignacion();
			setState(95);
			match(PAD);
			setState(96);
			bloque();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BloqueContext extends ParserRuleContext {
		public TerminalNode LLAVEI() { return getToken(expresionParser.LLAVEI, 0); }
		public TerminalNode LLAVED() { return getToken(expresionParser.LLAVED, 0); }
		public List<SentenciaContext> sentencia() {
			return getRuleContexts(SentenciaContext.class);
		}
		public SentenciaContext sentencia(int i) {
			return getRuleContext(SentenciaContext.class,i);
		}
		public BloqueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloque; }
	}

	public final BloqueContext bloque() throws RecognitionException {
		BloqueContext _localctx = new BloqueContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_bloque);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(98);
			match(LLAVEI);
			setState(102);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4286578996L) != 0)) {
				{
				{
				setState(99);
				sentencia();
				}
				}
				setState(104);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(105);
			match(LLAVED);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpresionContext extends ParserRuleContext {
		public OrLogicoContext orLogico() {
			return getRuleContext(OrLogicoContext.class,0);
		}
		public ExpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion; }
	}

	public final ExpresionContext expresion() throws RecognitionException {
		ExpresionContext _localctx = new ExpresionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_expresion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			orLogico();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OrLogicoContext extends ParserRuleContext {
		public List<AndLogicoContext> andLogico() {
			return getRuleContexts(AndLogicoContext.class);
		}
		public AndLogicoContext andLogico(int i) {
			return getRuleContext(AndLogicoContext.class,i);
		}
		public List<TerminalNode> OR() { return getTokens(expresionParser.OR); }
		public TerminalNode OR(int i) {
			return getToken(expresionParser.OR, i);
		}
		public OrLogicoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_orLogico; }
	}

	public final OrLogicoContext orLogico() throws RecognitionException {
		OrLogicoContext _localctx = new OrLogicoContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_orLogico);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			andLogico();
			setState(114);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR) {
				{
				{
				setState(110);
				match(OR);
				setState(111);
				andLogico();
				}
				}
				setState(116);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AndLogicoContext extends ParserRuleContext {
		public List<IgualdadContext> igualdad() {
			return getRuleContexts(IgualdadContext.class);
		}
		public IgualdadContext igualdad(int i) {
			return getRuleContext(IgualdadContext.class,i);
		}
		public List<TerminalNode> AND() { return getTokens(expresionParser.AND); }
		public TerminalNode AND(int i) {
			return getToken(expresionParser.AND, i);
		}
		public AndLogicoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_andLogico; }
	}

	public final AndLogicoContext andLogico() throws RecognitionException {
		AndLogicoContext _localctx = new AndLogicoContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_andLogico);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(117);
			igualdad();
			setState(122);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND) {
				{
				{
				setState(118);
				match(AND);
				setState(119);
				igualdad();
				}
				}
				setState(124);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IgualdadContext extends ParserRuleContext {
		public List<ComparacionContext> comparacion() {
			return getRuleContexts(ComparacionContext.class);
		}
		public ComparacionContext comparacion(int i) {
			return getRuleContext(ComparacionContext.class,i);
		}
		public List<TerminalNode> IGUAL() { return getTokens(expresionParser.IGUAL); }
		public TerminalNode IGUAL(int i) {
			return getToken(expresionParser.IGUAL, i);
		}
		public List<TerminalNode> NOIGUAL() { return getTokens(expresionParser.NOIGUAL); }
		public TerminalNode NOIGUAL(int i) {
			return getToken(expresionParser.NOIGUAL, i);
		}
		public IgualdadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_igualdad; }
	}

	public final IgualdadContext igualdad() throws RecognitionException {
		IgualdadContext _localctx = new IgualdadContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_igualdad);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			comparacion();
			setState(130);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==IGUAL || _la==NOIGUAL) {
				{
				{
				setState(126);
				_la = _input.LA(1);
				if ( !(_la==IGUAL || _la==NOIGUAL) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(127);
				comparacion();
				}
				}
				setState(132);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ComparacionContext extends ParserRuleContext {
		public List<SumaContext> suma() {
			return getRuleContexts(SumaContext.class);
		}
		public SumaContext suma(int i) {
			return getRuleContext(SumaContext.class,i);
		}
		public List<TerminalNode> MAYOR() { return getTokens(expresionParser.MAYOR); }
		public TerminalNode MAYOR(int i) {
			return getToken(expresionParser.MAYOR, i);
		}
		public List<TerminalNode> MENOR() { return getTokens(expresionParser.MENOR); }
		public TerminalNode MENOR(int i) {
			return getToken(expresionParser.MENOR, i);
		}
		public List<TerminalNode> MAYORI() { return getTokens(expresionParser.MAYORI); }
		public TerminalNode MAYORI(int i) {
			return getToken(expresionParser.MAYORI, i);
		}
		public List<TerminalNode> MENORI() { return getTokens(expresionParser.MENORI); }
		public TerminalNode MENORI(int i) {
			return getToken(expresionParser.MENORI, i);
		}
		public ComparacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparacion; }
	}

	public final ComparacionContext comparacion() throws RecognitionException {
		ComparacionContext _localctx = new ComparacionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_comparacion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(133);
			suma();
			setState(138);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1966080L) != 0)) {
				{
				{
				setState(134);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1966080L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(135);
				suma();
				}
				}
				setState(140);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SumaContext extends ParserRuleContext {
		public List<MultiplicacionContext> multiplicacion() {
			return getRuleContexts(MultiplicacionContext.class);
		}
		public MultiplicacionContext multiplicacion(int i) {
			return getRuleContext(MultiplicacionContext.class,i);
		}
		public List<TerminalNode> SUM() { return getTokens(expresionParser.SUM); }
		public TerminalNode SUM(int i) {
			return getToken(expresionParser.SUM, i);
		}
		public List<TerminalNode> RES() { return getTokens(expresionParser.RES); }
		public TerminalNode RES(int i) {
			return getToken(expresionParser.RES, i);
		}
		public SumaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_suma; }
	}

	public final SumaContext suma() throws RecognitionException {
		SumaContext _localctx = new SumaContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_suma);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(141);
			multiplicacion();
			setState(146);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==SUM || _la==RES) {
				{
				{
				setState(142);
				_la = _input.LA(1);
				if ( !(_la==SUM || _la==RES) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(143);
				multiplicacion();
				}
				}
				setState(148);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MultiplicacionContext extends ParserRuleContext {
		public List<UnicoContext> unico() {
			return getRuleContexts(UnicoContext.class);
		}
		public UnicoContext unico(int i) {
			return getRuleContext(UnicoContext.class,i);
		}
		public List<TerminalNode> MUL() { return getTokens(expresionParser.MUL); }
		public TerminalNode MUL(int i) {
			return getToken(expresionParser.MUL, i);
		}
		public List<TerminalNode> DIV() { return getTokens(expresionParser.DIV); }
		public TerminalNode DIV(int i) {
			return getToken(expresionParser.DIV, i);
		}
		public MultiplicacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplicacion; }
	}

	public final MultiplicacionContext multiplicacion() throws RecognitionException {
		MultiplicacionContext _localctx = new MultiplicacionContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_multiplicacion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(149);
			unico();
			setState(154);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==MUL || _la==DIV) {
				{
				{
				setState(150);
				_la = _input.LA(1);
				if ( !(_la==MUL || _la==DIV) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(151);
				unico();
				}
				}
				setState(156);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnicoContext extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(expresionParser.NOT, 0); }
		public UnicoContext unico() {
			return getRuleContext(UnicoContext.class,0);
		}
		public BaseContext base() {
			return getRuleContext(BaseContext.class,0);
		}
		public UnicoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unico; }
	}

	public final UnicoContext unico() throws RecognitionException {
		UnicoContext _localctx = new UnicoContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_unico);
		try {
			setState(160);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(157);
				match(NOT);
				setState(158);
				unico();
				}
				break;
			case PAI:
			case VERDADERO:
			case FALSO:
			case STRING:
			case FLOAT:
			case NUM:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(159);
				base();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BaseContext extends ParserRuleContext {
		public TerminalNode FLOAT() { return getToken(expresionParser.FLOAT, 0); }
		public TerminalNode NUM() { return getToken(expresionParser.NUM, 0); }
		public TerminalNode STRING() { return getToken(expresionParser.STRING, 0); }
		public TerminalNode VERDADERO() { return getToken(expresionParser.VERDADERO, 0); }
		public TerminalNode FALSO() { return getToken(expresionParser.FALSO, 0); }
		public TerminalNode ID() { return getToken(expresionParser.ID, 0); }
		public TerminalNode PAI() { return getToken(expresionParser.PAI, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode PAD() { return getToken(expresionParser.PAD, 0); }
		public BaseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_base; }
	}

	public final BaseContext base() throws RecognitionException {
		BaseContext _localctx = new BaseContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_base);
		try {
			setState(172);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FLOAT:
				enterOuterAlt(_localctx, 1);
				{
				setState(162);
				match(FLOAT);
				}
				break;
			case NUM:
				enterOuterAlt(_localctx, 2);
				{
				setState(163);
				match(NUM);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 3);
				{
				setState(164);
				match(STRING);
				}
				break;
			case VERDADERO:
				enterOuterAlt(_localctx, 4);
				{
				setState(165);
				match(VERDADERO);
				}
				break;
			case FALSO:
				enterOuterAlt(_localctx, 5);
				{
				setState(166);
				match(FALSO);
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 6);
				{
				setState(167);
				match(ID);
				}
				break;
			case PAI:
				enterOuterAlt(_localctx, 7);
				{
				setState(168);
				match(PAI);
				setState(169);
				expresion();
				setState(170);
				match(PAD);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracionContext extends ParserRuleContext {
		public TerminalNode TIPO() { return getToken(expresionParser.TIPO, 0); }
		public TerminalNode ID() { return getToken(expresionParser.ID, 0); }
		public TerminalNode ASIG() { return getToken(expresionParser.ASIG, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode FINAL() { return getToken(expresionParser.FINAL, 0); }
		public DeclaracionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracion; }
	}

	public final DeclaracionContext declaracion() throws RecognitionException {
		DeclaracionContext _localctx = new DeclaracionContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_declaracion);
		try {
			setState(183);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(174);
				match(TIPO);
				setState(175);
				match(ID);
				setState(176);
				match(ASIG);
				setState(177);
				expresion();
				setState(178);
				match(FINAL);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(180);
				match(TIPO);
				setState(181);
				match(ID);
				setState(182);
				match(FINAL);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrinttContext extends ParserRuleContext {
		public TerminalNode PRINT() { return getToken(expresionParser.PRINT, 0); }
		public TerminalNode PAI() { return getToken(expresionParser.PAI, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode PAD() { return getToken(expresionParser.PAD, 0); }
		public TerminalNode FINAL() { return getToken(expresionParser.FINAL, 0); }
		public PrinttContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printt; }
	}

	public final PrinttContext printt() throws RecognitionException {
		PrinttContext _localctx = new PrinttContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_printt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(185);
			match(PRINT);
			setState(186);
			match(PAI);
			setState(187);
			expresion();
			setState(188);
			match(PAD);
			setState(189);
			match(FINAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001!\u00c0\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0005\u0000(\b\u0000\n\u0000\f\u0000+\t\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0003\u0001;\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003O\b\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005[\b\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006"+
		"\u0001\u0006\u0005\u0006e\b\u0006\n\u0006\f\u0006h\t\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0005\bq"+
		"\b\b\n\b\f\bt\t\b\u0001\t\u0001\t\u0001\t\u0005\ty\b\t\n\t\f\t|\t\t\u0001"+
		"\n\u0001\n\u0001\n\u0005\n\u0081\b\n\n\n\f\n\u0084\t\n\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0005\u000b\u0089\b\u000b\n\u000b\f\u000b\u008c\t\u000b"+
		"\u0001\f\u0001\f\u0001\f\u0005\f\u0091\b\f\n\f\f\f\u0094\t\f\u0001\r\u0001"+
		"\r\u0001\r\u0005\r\u0099\b\r\n\r\f\r\u009c\t\r\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0003\u000e\u00a1\b\u000e\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0003\u000f\u00ad\b\u000f\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0003\u0010\u00b8\b\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0000\u0000\u0012\u0000\u0002\u0004"+
		"\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \""+
		"\u0000\u0004\u0001\u0000\u000f\u0010\u0001\u0000\u0011\u0014\u0001\u0000"+
		"\u000b\f\u0001\u0000\r\u000e\u00c5\u0000$\u0001\u0000\u0000\u0000\u0002"+
		":\u0001\u0000\u0000\u0000\u0004<\u0001\u0000\u0000\u0000\u0006N\u0001"+
		"\u0000\u0000\u0000\bP\u0001\u0000\u0000\u0000\nV\u0001\u0000\u0000\u0000"+
		"\fb\u0001\u0000\u0000\u0000\u000ek\u0001\u0000\u0000\u0000\u0010m\u0001"+
		"\u0000\u0000\u0000\u0012u\u0001\u0000\u0000\u0000\u0014}\u0001\u0000\u0000"+
		"\u0000\u0016\u0085\u0001\u0000\u0000\u0000\u0018\u008d\u0001\u0000\u0000"+
		"\u0000\u001a\u0095\u0001\u0000\u0000\u0000\u001c\u00a0\u0001\u0000\u0000"+
		"\u0000\u001e\u00ac\u0001\u0000\u0000\u0000 \u00b7\u0001\u0000\u0000\u0000"+
		"\"\u00b9\u0001\u0000\u0000\u0000$%\u0005\u0001\u0000\u0000%)\u0005\u0006"+
		"\u0000\u0000&(\u0003\u0002\u0001\u0000\'&\u0001\u0000\u0000\u0000(+\u0001"+
		"\u0000\u0000\u0000)\'\u0001\u0000\u0000\u0000)*\u0001\u0000\u0000\u0000"+
		"*,\u0001\u0000\u0000\u0000+)\u0001\u0000\u0000\u0000,-\u0005\u0007\u0000"+
		"\u0000-.\u0005\u0000\u0000\u0001.\u0001\u0001\u0000\u0000\u0000/;\u0003"+
		" \u0010\u000001\u0003\u0004\u0002\u000012\u0005 \u0000\u00002;\u0001\u0000"+
		"\u0000\u00003;\u0003\u0006\u0003\u00004;\u0003\"\u0011\u00005;\u0003\b"+
		"\u0004\u00006;\u0003\n\u0005\u000078\u0003\u000e\u0007\u000089\u0005 "+
		"\u0000\u00009;\u0001\u0000\u0000\u0000:/\u0001\u0000\u0000\u0000:0\u0001"+
		"\u0000\u0000\u0000:3\u0001\u0000\u0000\u0000:4\u0001\u0000\u0000\u0000"+
		":5\u0001\u0000\u0000\u0000:6\u0001\u0000\u0000\u0000:7\u0001\u0000\u0000"+
		"\u0000;\u0003\u0001\u0000\u0000\u0000<=\u0005\u001f\u0000\u0000=>\u0005"+
		"\n\u0000\u0000>?\u0003\u000e\u0007\u0000?\u0005\u0001\u0000\u0000\u0000"+
		"@A\u0005\u0002\u0000\u0000AB\u0005\b\u0000\u0000BC\u0003\u000e\u0007\u0000"+
		"CD\u0005\t\u0000\u0000DE\u0003\f\u0006\u0000EO\u0001\u0000\u0000\u0000"+
		"FG\u0005\u0002\u0000\u0000GH\u0005\b\u0000\u0000HI\u0003\u000e\u0007\u0000"+
		"IJ\u0005\t\u0000\u0000JK\u0003\f\u0006\u0000KL\u0005\u0003\u0000\u0000"+
		"LM\u0003\f\u0006\u0000MO\u0001\u0000\u0000\u0000N@\u0001\u0000\u0000\u0000"+
		"NF\u0001\u0000\u0000\u0000O\u0007\u0001\u0000\u0000\u0000PQ\u0005\u0004"+
		"\u0000\u0000QR\u0005\b\u0000\u0000RS\u0003\u000e\u0007\u0000ST\u0005\t"+
		"\u0000\u0000TU\u0003\f\u0006\u0000U\t\u0001\u0000\u0000\u0000VW\u0005"+
		"\u0005\u0000\u0000WZ\u0005\b\u0000\u0000X[\u0003 \u0010\u0000Y[\u0003"+
		"\u0004\u0002\u0000ZX\u0001\u0000\u0000\u0000ZY\u0001\u0000\u0000\u0000"+
		"[\\\u0001\u0000\u0000\u0000\\]\u0003\u000e\u0007\u0000]^\u0005 \u0000"+
		"\u0000^_\u0003\u0004\u0002\u0000_`\u0005\t\u0000\u0000`a\u0003\f\u0006"+
		"\u0000a\u000b\u0001\u0000\u0000\u0000bf\u0005\u0006\u0000\u0000ce\u0003"+
		"\u0002\u0001\u0000dc\u0001\u0000\u0000\u0000eh\u0001\u0000\u0000\u0000"+
		"fd\u0001\u0000\u0000\u0000fg\u0001\u0000\u0000\u0000gi\u0001\u0000\u0000"+
		"\u0000hf\u0001\u0000\u0000\u0000ij\u0005\u0007\u0000\u0000j\r\u0001\u0000"+
		"\u0000\u0000kl\u0003\u0010\b\u0000l\u000f\u0001\u0000\u0000\u0000mr\u0003"+
		"\u0012\t\u0000no\u0005\u0016\u0000\u0000oq\u0003\u0012\t\u0000pn\u0001"+
		"\u0000\u0000\u0000qt\u0001\u0000\u0000\u0000rp\u0001\u0000\u0000\u0000"+
		"rs\u0001\u0000\u0000\u0000s\u0011\u0001\u0000\u0000\u0000tr\u0001\u0000"+
		"\u0000\u0000uz\u0003\u0014\n\u0000vw\u0005\u0015\u0000\u0000wy\u0003\u0014"+
		"\n\u0000xv\u0001\u0000\u0000\u0000y|\u0001\u0000\u0000\u0000zx\u0001\u0000"+
		"\u0000\u0000z{\u0001\u0000\u0000\u0000{\u0013\u0001\u0000\u0000\u0000"+
		"|z\u0001\u0000\u0000\u0000}\u0082\u0003\u0016\u000b\u0000~\u007f\u0007"+
		"\u0000\u0000\u0000\u007f\u0081\u0003\u0016\u000b\u0000\u0080~\u0001\u0000"+
		"\u0000\u0000\u0081\u0084\u0001\u0000\u0000\u0000\u0082\u0080\u0001\u0000"+
		"\u0000\u0000\u0082\u0083\u0001\u0000\u0000\u0000\u0083\u0015\u0001\u0000"+
		"\u0000\u0000\u0084\u0082\u0001\u0000\u0000\u0000\u0085\u008a\u0003\u0018"+
		"\f\u0000\u0086\u0087\u0007\u0001\u0000\u0000\u0087\u0089\u0003\u0018\f"+
		"\u0000\u0088\u0086\u0001\u0000\u0000\u0000\u0089\u008c\u0001\u0000\u0000"+
		"\u0000\u008a\u0088\u0001\u0000\u0000\u0000\u008a\u008b\u0001\u0000\u0000"+
		"\u0000\u008b\u0017\u0001\u0000\u0000\u0000\u008c\u008a\u0001\u0000\u0000"+
		"\u0000\u008d\u0092\u0003\u001a\r\u0000\u008e\u008f\u0007\u0002\u0000\u0000"+
		"\u008f\u0091\u0003\u001a\r\u0000\u0090\u008e\u0001\u0000\u0000\u0000\u0091"+
		"\u0094\u0001\u0000\u0000\u0000\u0092\u0090\u0001\u0000\u0000\u0000\u0092"+
		"\u0093\u0001\u0000\u0000\u0000\u0093\u0019\u0001\u0000\u0000\u0000\u0094"+
		"\u0092\u0001\u0000\u0000\u0000\u0095\u009a\u0003\u001c\u000e\u0000\u0096"+
		"\u0097\u0007\u0003\u0000\u0000\u0097\u0099\u0003\u001c\u000e\u0000\u0098"+
		"\u0096\u0001\u0000\u0000\u0000\u0099\u009c\u0001\u0000\u0000\u0000\u009a"+
		"\u0098\u0001\u0000\u0000\u0000\u009a\u009b\u0001\u0000\u0000\u0000\u009b"+
		"\u001b\u0001\u0000\u0000\u0000\u009c\u009a\u0001\u0000\u0000\u0000\u009d"+
		"\u009e\u0005\u0017\u0000\u0000\u009e\u00a1\u0003\u001c\u000e\u0000\u009f"+
		"\u00a1\u0003\u001e\u000f\u0000\u00a0\u009d\u0001\u0000\u0000\u0000\u00a0"+
		"\u009f\u0001\u0000\u0000\u0000\u00a1\u001d\u0001\u0000\u0000\u0000\u00a2"+
		"\u00ad\u0005\u001d\u0000\u0000\u00a3\u00ad\u0005\u001e\u0000\u0000\u00a4"+
		"\u00ad\u0005\u001c\u0000\u0000\u00a5\u00ad\u0005\u001a\u0000\u0000\u00a6"+
		"\u00ad\u0005\u001b\u0000\u0000\u00a7\u00ad\u0005\u001f\u0000\u0000\u00a8"+
		"\u00a9\u0005\b\u0000\u0000\u00a9\u00aa\u0003\u000e\u0007\u0000\u00aa\u00ab"+
		"\u0005\t\u0000\u0000\u00ab\u00ad\u0001\u0000\u0000\u0000\u00ac\u00a2\u0001"+
		"\u0000\u0000\u0000\u00ac\u00a3\u0001\u0000\u0000\u0000\u00ac\u00a4\u0001"+
		"\u0000\u0000\u0000\u00ac\u00a5\u0001\u0000\u0000\u0000\u00ac\u00a6\u0001"+
		"\u0000\u0000\u0000\u00ac\u00a7\u0001\u0000\u0000\u0000\u00ac\u00a8\u0001"+
		"\u0000\u0000\u0000\u00ad\u001f\u0001\u0000\u0000\u0000\u00ae\u00af\u0005"+
		"\u0019\u0000\u0000\u00af\u00b0\u0005\u001f\u0000\u0000\u00b0\u00b1\u0005"+
		"\n\u0000\u0000\u00b1\u00b2\u0003\u000e\u0007\u0000\u00b2\u00b3\u0005 "+
		"\u0000\u0000\u00b3\u00b8\u0001\u0000\u0000\u0000\u00b4\u00b5\u0005\u0019"+
		"\u0000\u0000\u00b5\u00b6\u0005\u001f\u0000\u0000\u00b6\u00b8\u0005 \u0000"+
		"\u0000\u00b7\u00ae\u0001\u0000\u0000\u0000\u00b7\u00b4\u0001\u0000\u0000"+
		"\u0000\u00b8!\u0001\u0000\u0000\u0000\u00b9\u00ba\u0005\u0018\u0000\u0000"+
		"\u00ba\u00bb\u0005\b\u0000\u0000\u00bb\u00bc\u0003\u000e\u0007\u0000\u00bc"+
		"\u00bd\u0005\t\u0000\u0000\u00bd\u00be\u0005 \u0000\u0000\u00be#\u0001"+
		"\u0000\u0000\u0000\u000e):NZfrz\u0082\u008a\u0092\u009a\u00a0\u00ac\u00b7";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
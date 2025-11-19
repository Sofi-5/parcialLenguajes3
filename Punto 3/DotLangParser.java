// Generated from ./DotLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class DotLangParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, ID=11, INT=12, WS=13, COMMENT=14;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_declVector = 2, RULE_assignment = 3, 
		RULE_vectorLiteral = 4, RULE_printStmt = 5;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "declVector", "assignment", "vectorLiteral", 
			"printStmt"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'vector'", "'['", "']'", "';'", "'='", "'dot'", "'('", "','", 
			"')'", "'print'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, "ID", 
			"INT", "WS", "COMMENT"
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
	public String getGrammarFileName() { return "DotLang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public DotLangParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(DotLangParser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DotLangListener ) ((DotLangListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DotLangListener ) ((DotLangListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(13); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(12);
				statement();
				}
				}
				setState(15); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 3074L) != 0) );
			setState(17);
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
	public static class StatementContext extends ParserRuleContext {
		public DeclVectorContext declVector() {
			return getRuleContext(DeclVectorContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public PrintStmtContext printStmt() {
			return getRuleContext(PrintStmtContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DotLangListener ) ((DotLangListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DotLangListener ) ((DotLangListener)listener).exitStatement(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(22);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				enterOuterAlt(_localctx, 1);
				{
				setState(19);
				declVector();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(20);
				assignment();
				}
				break;
			case T__9:
				enterOuterAlt(_localctx, 3);
				{
				setState(21);
				printStmt();
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
	public static class DeclVectorContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(DotLangParser.ID, 0); }
		public TerminalNode INT() { return getToken(DotLangParser.INT, 0); }
		public DeclVectorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declVector; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DotLangListener ) ((DotLangListener)listener).enterDeclVector(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DotLangListener ) ((DotLangListener)listener).exitDeclVector(this);
		}
	}

	public final DeclVectorContext declVector() throws RecognitionException {
		DeclVectorContext _localctx = new DeclVectorContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_declVector);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(24);
			match(T__0);
			setState(25);
			match(ID);
			setState(26);
			match(T__1);
			setState(27);
			match(INT);
			setState(28);
			match(T__2);
			setState(29);
			match(T__3);
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
	public static class AssignmentContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(DotLangParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(DotLangParser.ID, i);
		}
		public VectorLiteralContext vectorLiteral() {
			return getRuleContext(VectorLiteralContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DotLangListener ) ((DotLangListener)listener).enterAssignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DotLangListener ) ((DotLangListener)listener).exitAssignment(this);
		}
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_assignment);
		try {
			setState(45);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(31);
				match(ID);
				setState(32);
				match(T__4);
				setState(33);
				vectorLiteral();
				setState(34);
				match(T__3);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(36);
				match(ID);
				setState(37);
				match(T__4);
				setState(38);
				match(T__5);
				setState(39);
				match(T__6);
				setState(40);
				match(ID);
				setState(41);
				match(T__7);
				setState(42);
				match(ID);
				setState(43);
				match(T__8);
				setState(44);
				match(T__3);
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
	public static class VectorLiteralContext extends ParserRuleContext {
		public List<TerminalNode> INT() { return getTokens(DotLangParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(DotLangParser.INT, i);
		}
		public VectorLiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vectorLiteral; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DotLangListener ) ((DotLangListener)listener).enterVectorLiteral(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DotLangListener ) ((DotLangListener)listener).exitVectorLiteral(this);
		}
	}

	public final VectorLiteralContext vectorLiteral() throws RecognitionException {
		VectorLiteralContext _localctx = new VectorLiteralContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_vectorLiteral);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(47);
			match(T__1);
			setState(56);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INT) {
				{
				setState(48);
				match(INT);
				setState(53);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__7) {
					{
					{
					setState(49);
					match(T__7);
					setState(50);
					match(INT);
					}
					}
					setState(55);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(58);
			match(T__2);
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
	public static class PrintStmtContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(DotLangParser.ID, 0); }
		public PrintStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printStmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DotLangListener ) ((DotLangListener)listener).enterPrintStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DotLangListener ) ((DotLangListener)listener).exitPrintStmt(this);
		}
	}

	public final PrintStmtContext printStmt() throws RecognitionException {
		PrintStmtContext _localctx = new PrintStmtContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_printStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			match(T__9);
			setState(61);
			match(T__6);
			setState(62);
			match(ID);
			setState(63);
			match(T__8);
			setState(64);
			match(T__3);
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
		"\u0004\u0001\u000eC\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0001\u0000\u0004\u0000\u000e\b\u0000\u000b\u0000\f"+
		"\u0000\u000f\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0003\u0001\u0017\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003"+
		".\b\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004"+
		"4\b\u0004\n\u0004\f\u00047\t\u0004\u0003\u00049\b\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0000\u0000\u0006\u0000\u0002\u0004\u0006\b\n\u0000"+
		"\u0000B\u0000\r\u0001\u0000\u0000\u0000\u0002\u0016\u0001\u0000\u0000"+
		"\u0000\u0004\u0018\u0001\u0000\u0000\u0000\u0006-\u0001\u0000\u0000\u0000"+
		"\b/\u0001\u0000\u0000\u0000\n<\u0001\u0000\u0000\u0000\f\u000e\u0003\u0002"+
		"\u0001\u0000\r\f\u0001\u0000\u0000\u0000\u000e\u000f\u0001\u0000\u0000"+
		"\u0000\u000f\r\u0001\u0000\u0000\u0000\u000f\u0010\u0001\u0000\u0000\u0000"+
		"\u0010\u0011\u0001\u0000\u0000\u0000\u0011\u0012\u0005\u0000\u0000\u0001"+
		"\u0012\u0001\u0001\u0000\u0000\u0000\u0013\u0017\u0003\u0004\u0002\u0000"+
		"\u0014\u0017\u0003\u0006\u0003\u0000\u0015\u0017\u0003\n\u0005\u0000\u0016"+
		"\u0013\u0001\u0000\u0000\u0000\u0016\u0014\u0001\u0000\u0000\u0000\u0016"+
		"\u0015\u0001\u0000\u0000\u0000\u0017\u0003\u0001\u0000\u0000\u0000\u0018"+
		"\u0019\u0005\u0001\u0000\u0000\u0019\u001a\u0005\u000b\u0000\u0000\u001a"+
		"\u001b\u0005\u0002\u0000\u0000\u001b\u001c\u0005\f\u0000\u0000\u001c\u001d"+
		"\u0005\u0003\u0000\u0000\u001d\u001e\u0005\u0004\u0000\u0000\u001e\u0005"+
		"\u0001\u0000\u0000\u0000\u001f \u0005\u000b\u0000\u0000 !\u0005\u0005"+
		"\u0000\u0000!\"\u0003\b\u0004\u0000\"#\u0005\u0004\u0000\u0000#.\u0001"+
		"\u0000\u0000\u0000$%\u0005\u000b\u0000\u0000%&\u0005\u0005\u0000\u0000"+
		"&\'\u0005\u0006\u0000\u0000\'(\u0005\u0007\u0000\u0000()\u0005\u000b\u0000"+
		"\u0000)*\u0005\b\u0000\u0000*+\u0005\u000b\u0000\u0000+,\u0005\t\u0000"+
		"\u0000,.\u0005\u0004\u0000\u0000-\u001f\u0001\u0000\u0000\u0000-$\u0001"+
		"\u0000\u0000\u0000.\u0007\u0001\u0000\u0000\u0000/8\u0005\u0002\u0000"+
		"\u000005\u0005\f\u0000\u000012\u0005\b\u0000\u000024\u0005\f\u0000\u0000"+
		"31\u0001\u0000\u0000\u000047\u0001\u0000\u0000\u000053\u0001\u0000\u0000"+
		"\u000056\u0001\u0000\u0000\u000069\u0001\u0000\u0000\u000075\u0001\u0000"+
		"\u0000\u000080\u0001\u0000\u0000\u000089\u0001\u0000\u0000\u00009:\u0001"+
		"\u0000\u0000\u0000:;\u0005\u0003\u0000\u0000;\t\u0001\u0000\u0000\u0000"+
		"<=\u0005\n\u0000\u0000=>\u0005\u0007\u0000\u0000>?\u0005\u000b\u0000\u0000"+
		"?@\u0005\t\u0000\u0000@A\u0005\u0004\u0000\u0000A\u000b\u0001\u0000\u0000"+
		"\u0000\u0005\u000f\u0016-58";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
# Generated from DotLang.g4 by ANTLR 4.13.1
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
        4,1,14,67,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,0,1,0,1,1,1,1,1,1,3,1,23,8,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,3,3,46,8,3,1,4,1,4,1,4,1,4,5,4,52,8,4,10,4,12,4,55,9,4,3,
        4,57,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,0,0,6,0,2,4,6,8,10,
        0,0,66,0,13,1,0,0,0,2,22,1,0,0,0,4,24,1,0,0,0,6,45,1,0,0,0,8,47,
        1,0,0,0,10,60,1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,15,1,0,0,0,
        15,13,1,0,0,0,15,16,1,0,0,0,16,17,1,0,0,0,17,18,5,0,0,1,18,1,1,0,
        0,0,19,23,3,4,2,0,20,23,3,6,3,0,21,23,3,10,5,0,22,19,1,0,0,0,22,
        20,1,0,0,0,22,21,1,0,0,0,23,3,1,0,0,0,24,25,5,1,0,0,25,26,5,11,0,
        0,26,27,5,2,0,0,27,28,5,12,0,0,28,29,5,3,0,0,29,30,5,4,0,0,30,5,
        1,0,0,0,31,32,5,11,0,0,32,33,5,5,0,0,33,34,3,8,4,0,34,35,5,4,0,0,
        35,46,1,0,0,0,36,37,5,11,0,0,37,38,5,5,0,0,38,39,5,6,0,0,39,40,5,
        7,0,0,40,41,5,11,0,0,41,42,5,8,0,0,42,43,5,11,0,0,43,44,5,9,0,0,
        44,46,5,4,0,0,45,31,1,0,0,0,45,36,1,0,0,0,46,7,1,0,0,0,47,56,5,2,
        0,0,48,53,5,12,0,0,49,50,5,8,0,0,50,52,5,12,0,0,51,49,1,0,0,0,52,
        55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,
        0,56,48,1,0,0,0,56,57,1,0,0,0,57,58,1,0,0,0,58,59,5,3,0,0,59,9,1,
        0,0,0,60,61,5,10,0,0,61,62,5,7,0,0,62,63,5,11,0,0,63,64,5,9,0,0,
        64,65,5,4,0,0,65,11,1,0,0,0,5,15,22,45,53,56
    ]

class DotLangParser ( Parser ):

    grammarFileName = "DotLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'vector'", "'['", "']'", "';'", "'='", 
                     "'dot'", "'('", "','", "')'", "'print'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "INT", 
                      "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_declVector = 2
    RULE_assignment = 3
    RULE_vectorLiteral = 4
    RULE_printStmt = 5

    ruleNames =  [ "program", "statement", "declVector", "assignment", "vectorLiteral", 
                   "printStmt" ]

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
    ID=11
    INT=12
    WS=13
    COMMENT=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(DotLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DotLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(DotLangParser.StatementContext,i)


        def getRuleIndex(self):
            return DotLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = DotLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.statement()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3074) != 0)):
                    break

            self.state = 17
            self.match(DotLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declVector(self):
            return self.getTypedRuleContext(DotLangParser.DeclVectorContext,0)


        def assignment(self):
            return self.getTypedRuleContext(DotLangParser.AssignmentContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(DotLangParser.PrintStmtContext,0)


        def getRuleIndex(self):
            return DotLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = DotLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.declVector()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.assignment()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.printStmt()
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


    class DeclVectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DotLangParser.ID, 0)

        def INT(self):
            return self.getToken(DotLangParser.INT, 0)

        def getRuleIndex(self):
            return DotLangParser.RULE_declVector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclVector" ):
                listener.enterDeclVector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclVector" ):
                listener.exitDeclVector(self)




    def declVector(self):

        localctx = DotLangParser.DeclVectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declVector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(DotLangParser.T__0)
            self.state = 25
            self.match(DotLangParser.ID)
            self.state = 26
            self.match(DotLangParser.T__1)
            self.state = 27
            self.match(DotLangParser.INT)
            self.state = 28
            self.match(DotLangParser.T__2)
            self.state = 29
            self.match(DotLangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DotLangParser.ID)
            else:
                return self.getToken(DotLangParser.ID, i)

        def vectorLiteral(self):
            return self.getTypedRuleContext(DotLangParser.VectorLiteralContext,0)


        def getRuleIndex(self):
            return DotLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = DotLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.match(DotLangParser.ID)
                self.state = 32
                self.match(DotLangParser.T__4)
                self.state = 33
                self.vectorLiteral()
                self.state = 34
                self.match(DotLangParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.match(DotLangParser.ID)
                self.state = 37
                self.match(DotLangParser.T__4)
                self.state = 38
                self.match(DotLangParser.T__5)
                self.state = 39
                self.match(DotLangParser.T__6)
                self.state = 40
                self.match(DotLangParser.ID)
                self.state = 41
                self.match(DotLangParser.T__7)
                self.state = 42
                self.match(DotLangParser.ID)
                self.state = 43
                self.match(DotLangParser.T__8)
                self.state = 44
                self.match(DotLangParser.T__3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VectorLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(DotLangParser.INT)
            else:
                return self.getToken(DotLangParser.INT, i)

        def getRuleIndex(self):
            return DotLangParser.RULE_vectorLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVectorLiteral" ):
                listener.enterVectorLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVectorLiteral" ):
                listener.exitVectorLiteral(self)




    def vectorLiteral(self):

        localctx = DotLangParser.VectorLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vectorLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(DotLangParser.T__1)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 48
                self.match(DotLangParser.INT)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 49
                    self.match(DotLangParser.T__7)
                    self.state = 50
                    self.match(DotLangParser.INT)
                    self.state = 55
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 58
            self.match(DotLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DotLangParser.ID, 0)

        def getRuleIndex(self):
            return DotLangParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)




    def printStmt(self):

        localctx = DotLangParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(DotLangParser.T__9)
            self.state = 61
            self.match(DotLangParser.T__6)
            self.state = 62
            self.match(DotLangParser.ID)
            self.state = 63
            self.match(DotLangParser.T__8)
            self.state = 64
            self.match(DotLangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






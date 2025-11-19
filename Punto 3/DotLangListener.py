# Generated from DotLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DotLangParser import DotLangParser
else:
    from DotLangParser import DotLangParser

# This class defines a complete listener for a parse tree produced by DotLangParser.
class DotLangListener(ParseTreeListener):

    # Enter a parse tree produced by DotLangParser#program.
    def enterProgram(self, ctx:DotLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by DotLangParser#program.
    def exitProgram(self, ctx:DotLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by DotLangParser#statement.
    def enterStatement(self, ctx:DotLangParser.StatementContext):
        pass

    # Exit a parse tree produced by DotLangParser#statement.
    def exitStatement(self, ctx:DotLangParser.StatementContext):
        pass


    # Enter a parse tree produced by DotLangParser#declVector.
    def enterDeclVector(self, ctx:DotLangParser.DeclVectorContext):
        pass

    # Exit a parse tree produced by DotLangParser#declVector.
    def exitDeclVector(self, ctx:DotLangParser.DeclVectorContext):
        pass


    # Enter a parse tree produced by DotLangParser#assignment.
    def enterAssignment(self, ctx:DotLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by DotLangParser#assignment.
    def exitAssignment(self, ctx:DotLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by DotLangParser#vectorLiteral.
    def enterVectorLiteral(self, ctx:DotLangParser.VectorLiteralContext):
        pass

    # Exit a parse tree produced by DotLangParser#vectorLiteral.
    def exitVectorLiteral(self, ctx:DotLangParser.VectorLiteralContext):
        pass


    # Enter a parse tree produced by DotLangParser#printStmt.
    def enterPrintStmt(self, ctx:DotLangParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by DotLangParser#printStmt.
    def exitPrintStmt(self, ctx:DotLangParser.PrintStmtContext):
        pass



del DotLangParser
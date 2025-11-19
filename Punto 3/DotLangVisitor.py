# DotLangVisitor.py — generado manualmente para grammar DotLang;

from antlr4 import *
from DotLangParser import DotLangParser

class DotLangVisitor(ParseTreeVisitor):

    def visitProgram(self, ctx: DotLangParser.ProgramContext):
        return self.visitChildren(ctx)

    def visitStatement(self, ctx: DotLangParser.StatementContext):
        return self.visitChildren(ctx)

    def visitDeclVector(self, ctx: DotLangParser.DeclVectorContext):
        return self.visitChildren(ctx)

    def visitAssignment(self, ctx: DotLangParser.AssignmentContext):
        return self.visitChildren(ctx)

    def visitVectorLiteral(self, ctx: DotLangParser.VectorLiteralContext):
        return self.visitChildren(ctx)

    def visitPrintStmt(self, ctx: DotLangParser.PrintStmtContext):
        return self.visitChildren(ctx)
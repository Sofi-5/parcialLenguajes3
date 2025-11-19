# dot_evaluator.py
from DotLangVisitor import DotLangVisitor
from DotLangParser import DotLangParser

class DotLangEvaluator(DotLangVisitor):
    def __init__(self):
        self.symbols = {}  # nombre → dimensión
        self.values = {}   # nombre → datos

    # Sobrescribimos EXACTAMENTE los métodos que ANTLR espera
    def visitProgram(self, ctx):
        for child in ctx.statement():
            self.visit(child)
        return None

    def visitDeclVector(self, ctx):
        name = ctx.ID().getText()
        dim = int(ctx.INT().getText())
        self.symbols[name] = dim
        print(f"[DEBUG] Declarado: {name} con dim={dim}")
        return None

    def visitVectorLiteral(self, ctx):
        vals = [int(tok.getText()) for tok in ctx.INT()] if ctx.INT() else []
        print(f"[DEBUG] Literal: {vals}")
        return vals

    def visitAssignment(self, ctx):
        target = ctx.ID().getText()
        print(f"[DEBUG] Asignando a: {target}")
        
        if ctx.vectorLiteral():
            vals = self.visit(ctx.vectorLiteral())
            self.values[target] = vals
            print(f"[DEBUG] → {target} = {vals}")
        elif ctx.getChild(2).getText() == 'dot':
            a_name = ctx.ID(0).getText()
            b_name = ctx.ID(1).getText()
            a = self.values[a_name]
            b = self.values[b_name]
            dot_val = sum(x*y for x,y in zip(a,b))
            self.values[target] = dot_val
            print(f"[DEBUG] → {target} = dot({a_name},{b_name}) = {dot_val}")
        return None

    def visitPrintStmt(self, ctx):
        var = ctx.ID().getText()
        val = self.values.get(var, "<no encontrado>")
        print(f"[PRINT] {var} = {val}")
        return None

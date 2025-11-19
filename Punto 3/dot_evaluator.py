# dot_evaluator.py
from DotLangVisitor import DotLangVisitor

class DotLangEvaluator(DotLangVisitor):
    def __init__(self):
        self.symbols = {}
        self.values = {}

    # Este método se llama para CADA nodo del árbol
    def visit(self, ctx):
        if ctx is None:
            return None
        # Forzamos la visita recursiva manual
        result = self.visitChildren(ctx)
        # Pero también procesamos el nodo actual si es relevante
        node_type = type(ctx).__name__
        if node_type == 'DeclVectorContext':
            return self.handle_decl_vector(ctx)
        elif node_type == 'AssignmentContext':
            return self.handle_assignment(ctx)
        elif node_type == 'PrintStmtContext':
            return self.handle_print(ctx)
        return result

    def handle_decl_vector(self, ctx):
        try:
            # ID está en posición 1, INT en posición 3 (vector ID [ INT ])
            name = ctx.ID().getText()
            dim = int(ctx.INT().getText())
            self.symbols[name] = dim
            print(f"[DEBUG] Declarado: {name} con dim={dim}")
        except Exception as e:
            print(f"[ERROR decl] {e}")
        return None

    def handle_assignment(self, ctx):
        try:
            target = ctx.ID().getText()
            print(f"[DEBUG] Asignando a: {target}")
            
            # Si hay vectorLiteral
            if ctx.vectorLiteral():
                vals = self.visitVectorLiteral(ctx.vectorLiteral())
                self.values[target] = vals
                print(f"[DEBUG] → {target} = {vals}")
            # Si hay 'dot'
            elif ctx.getChildCount() >= 5 and ctx.getChild(2).getText() == 'dot':
                a_name = ctx.ID(0).getText()
                b_name = ctx.ID(1).getText()
                a = self.values[a_name]
                b = self.values[b_name]
                res = sum(x*y for x,y in zip(a,b))
                self.values[target] = res
                print(f"[DEBUG] → {target} = dot({a_name},{b_name}) = {res}")
        except Exception as e:
            print(f"[ERROR assign] {e}")
        return None

    def visitVectorLiteral(self, ctx):
        return [int(tok.getText()) for tok in ctx.INT()] if ctx.INT() else []

    def handle_print(self, ctx):
        try:
            var = ctx.ID().getText()
            val = self.values.get(var, "<no asignado>")
            print(f"[PRINT] {var} = {val}")
        except Exception as e:
            print(f"[ERROR print] {e}")
        return None

    def visitChildren(self, node):
        # Visita recursivamente todos los hijos
        result = self.defaultResult()
        n = node.getChildCount()
        for i in range(n):
            child = node.getChild(i)
            if child is not None:
                child_result = child.accept(self)
                result = self.aggregateResult(result, child_result)
        return result

    def defaultResult(self):
        return None

    def aggregateResult(self, aggregate, nextResult):
        return nextResult
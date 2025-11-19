# main.py — ✅ FUNCIONAL, SIN ERRORES
from antlr4 import *
from DotLangLexer import DotLangLexer
from DotLangParser import DotLangParser

class SimpleEvaluator:
    def __init__(self):
        self.symbols = {}
        self.values = {}

    def evaluate(self, tree):
        self._visit(tree)
        return self.values

    def _visit(self, node):
        if node is None:
            return
        # Procesar este nodo
        name = type(node).__name__
        if name == 'DeclVectorContext':
            self._handle_decl(node)
        elif name == 'AssignmentContext':
            self._handle_assign(node)
        elif name == 'PrintStmtContext':
            self._handle_print(node)
        # Visitar hijos
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            if child is not None:
                self._visit(child)

    def _handle_decl(self, ctx):
        name = ctx.ID().getText()  # solo hay 1 ID → funciona
        dim = int(ctx.INT().getText())
        self.symbols[name] = dim
        print(f"[DECL] {name} : dim={dim}")

    def _handle_assign(self, ctx):
        # Primer ID es siempre la variable destino
        target = ctx.ID(0).getText()
        print(f"[ASIG] destino: {target}")

        if ctx.vectorLiteral():
            # a = [1,2,3]
            vals = [int(t.getText()) for t in ctx.vectorLiteral().INT()] if ctx.vectorLiteral().INT() else []
            self.values[target] = vals
            print(f"      → {target} = {vals}")
        else:
            # c = dot(a, b)
            # IDs: [target, arg1, arg2]
            if ctx.ID().__len__() >= 3:
                a_name = ctx.ID(1).getText()
                b_name = ctx.ID(2).getText()
                if a_name in self.values and b_name in self.values:
                    va = self.values[a_name]
                    vb = self.values[b_name]
                    if len(va) != len(vb):
                        raise RuntimeError(f"Dimensión incompatible: {len(va)} ≠ {len(vb)}")
                    result = sum(x * y for x, y in zip(va, vb))
                    self.values[target] = result
                    print(f"      → {target} = dot({a_name}, {b_name}) = {result}")
                else:
                    missing = [n for n in [a_name, b_name] if n not in self.values]
                    print(f"      ⚠️  Vector no inicializado: {missing}")

    def _handle_print(self, ctx):
        var = ctx.ID().getText()  # solo 1 ID en print(x)
        val = self.values.get(var, "<no asignado>")
        print(f"[PRINT] {var} = {val}")

# --- Ejecución ---
code = """
vector a[3];
vector b[3];
a = [1, 2, 3];
b = [4, 5, 6];
c = dot(a, b);
print(c);
"""

lexer = DotLangLexer(InputStream(code))
parser = DotLangParser(CommonTokenStream(lexer))
tree = parser.program()

evaluator = SimpleEvaluator()
try:
    values = evaluator.evaluate(tree)
    print("\nEjecución exitosa.")
    print(" Valores finales:", values)
except Exception as e:
    print(f"\n Error: {e}")
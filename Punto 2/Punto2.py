import re

def validar_programa(codigo: str):
    lineas = [l.strip() for l in codigo.strip().split(";") if l.strip()]
    simbolos = {}  # { nombre: dim }
    errores = []

    for i, linea in enumerate(lineas, 1):
        try:
            # 1. Declaración: vector a[5]
            m = re.match(r"vector\s+(\w+)\s*\[\s*(\d+)\s*\]", linea)
            if m:
                nombre, dim = m.group(1), int(m.group(2))
                if dim <= 0:
                    errores.append(f"Línea {i}: dimensión debe ser > 0")
                elif nombre in simbolos:
                    errores.append(f"Línea {i}: '{nombre}' ya declarado")
                else:
                    simbolos[nombre] = dim
                continue

            # 2. Asignación dot: c = dot(a, b)
            m = re.match(r"(\w+)\s*=\s*dot\s*\(\s*(\w+)\s*,\s*(\w+)\s*\)", linea)
            if m:
                res, v1, v2 = m.groups()
                if v1 not in simbolos:
                    errores.append(f"Línea {i}: vector '{v1}' no declarado")
                    continue
                if v2 not in simbolos:
                    errores.append(f"Línea {i}: vector '{v2}' no declarado")
                    continue
                if simbolos[v1] != simbolos[v2]:
                    errores.append(f"Línea {i}: dimensión incompatible ({simbolos[v1]} ≠ {simbolos[v2]}) para dot({v1}, {v2})")
                # resultado es escalar (no necesita dimensión)
                continue

            # 3. Print: print(x)
            if re.match(r"print\s*\(\s*\w+\s*\)", linea):
                continue

            errores.append(f"Línea {i}: sintaxis no reconocida → '{linea}'")

        except Exception as e:
            errores.append(f"Línea {i}: error interno – {e}")

    return {
        "valido": len(errores) == 0,
        "errores": errores,
        "tabla_simbolos": simbolos
    }



codigo = """
vector a[3];
vector b[3];
c = dot(a, b);
print(c);
"""

print(validar_programa(codigo))
# → {'valido': True, 'errores': [], 'tabla_simbolos': {'a': 3, 'b': 3}}
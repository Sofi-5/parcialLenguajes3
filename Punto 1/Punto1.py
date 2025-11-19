def analizar_consulta(consulta: str):
    # Esquemas predefinidos
    ESQUEMAS = {
        "usuario": ["id", "nombre", "email", "edad"],
        "producto": ["id", "nombre", "precio", "stock"]
    }

    # Normalizar y tokenizar 
    consulta = consulta.strip().rstrip(";").upper()
    tokens = consulta.split()
    if not tokens:
        return {"valida": False, "errores": ["Consulta vacía"]}

    # Atributos iniciales 
    resultado = {
        "tipo": None,
        "tabla": None,
        "campos_usados": [],
        "valores": [],
        "valida": False,
        "errores": []
    }

    try:
        primer = tokens[0]

        if primer == "SELECT":
            # SELECT campo1, campo2 FROM tabla
            if "FROM" not in tokens:
                resultado["errores"].append("Falta palabra clave FROM")
                return resultado

            idx_from = tokens.index("FROM")
            if idx_from < 2:
                resultado["errores"].append("SELECT debe tener al menos un campo")
                return resultado

            campos_txt = " ".join(tokens[1:idx_from]).replace(",", " ").split()
            tabla = tokens[idx_from + 1] if idx_from + 1 < len(tokens) else None

            resultado["tipo"] = "SELECT"
            resultado["tabla"] = tabla
            resultado["campos_usados"] = [c for c in campos_txt if c != '*']

            # Validación
            if not tabla:
                resultado["errores"].append("Falta nombre de tabla")
            elif tabla not in ESQUEMAS:
                resultado["errores"].append(f"Tabla '{tabla}' no definida")
            else:
                campos_validos = ESQUEMAS[tabla]
                if "*" in campos_txt:
                    resultado["campos_usados"] = campos_validos[:]  # Todos
                else:
                    for c in resultado["campos_usados"]:
                        if c not in campos_validos:
                            resultado["errores"].append(f"Campo '{c}' no existe en '{tabla}'")

        elif primer == "INSERT":
            # INSERT INTO tabla VALUES (val1, val2)
            if len(tokens) < 4 or tokens[1] != "INTO" or "VALUES" not in tokens:
                resultado["errores"].append("Sintaxis inválida: debe ser INSERT INTO tabla VALUES (...)")
                return resultado

            idx_into = 1
            tabla = tokens[idx_into + 1]
            idx_values = tokens.index("VALUES")

            # Extraer valores entre paréntesis
            resto = " ".join(tokens[idx_values + 1:])
            if "(" in resto and ")" in resto:
                valores_str = resto[resto.find("(")+1 : resto.find(")")]
                valores = [v.strip() for v in valores_str.split(",") if v.strip()]
            else:
                valores = []

            resultado["tipo"] = "INSERT"
            resultado["tabla"] = tabla
            resultado["valores"] = valores

            if tabla not in ESQUEMAS:
                resultado["errores"].append(f"Tabla '{tabla}' no definida")
            else:
                esperado = len(ESQUEMAS[tabla])
                if len(valores) != esperado:
                    resultado["errores"].append(f"INSERT requiere {esperado} valores, pero se dieron {len(valores)}")

        elif primer == "UPDATE":
            # UPDATE tabla SET campo1=valor1, campo2=valor2
            if len(tokens) < 4 or tokens[2] != "SET":
                resultado["errores"].append("Sintaxis inválida: debe ser UPDATE tabla SET ...")
                return resultado

            tabla = tokens[1]
            set_part = " ".join(tokens[3:])

            # Extraer asignaciones: nombre=valor (ignoramos comas y comillas para simplificar)
            asignaciones = []
            for item in set_part.replace(",", " ").split():
                if "=" in item:
                    campo = item.split("=")[0].strip()
                    asignaciones.append(campo)

            resultado["tipo"] = "UPDATE"
            resultado["tabla"] = tabla
            resultado["campos_usados"] = asignaciones

            if tabla not in ESQUEMAS:
                resultado["errores"].append(f"Tabla '{tabla}' no definida")
            else:
                campos_validos = ESQUEMAS[tabla]
                for c in asignaciones:
                    if c not in campos_validos:
                        resultado["errores"].append(f"Campo '{c}' no existe en '{tabla}'")

        elif primer == "DELETE":
            # DELETE FROM tabla
            if len(tokens) < 3 or tokens[1] != "FROM":
                resultado["errores"].append("Sintaxis inválida: debe ser DELETE FROM tabla")
                return resultado

            tabla = tokens[2]
            resultado["tipo"] = "DELETE"
            resultado["tabla"] = tabla

            if tabla not in ESQUEMAS:
                resultado["errores"].append(f"Tabla '{tabla}' no definida")

        else:
            resultado["errores"].append(f"Operación no soportada: '{primer}'")

        # Determinar validez final
        resultado["valida"] = len(resultado["errores"]) == 0

    except Exception as e:
        resultado["errores"].append(f"Error interno: {str(e)}")

    return resultado


print(analizar_consulta("SELECT nombre, email FROM usuario"))
# → {'tipo': 'SELECT', 'tabla': 'usuario', 'campos_usados': ['nombre', 'email'], 'valida': True, ...}

print(analizar_consulta("UPDATE usuario SET apellido='Gómez'"))
# → ... 'errores': ["Campo 'apellido' no existe en 'usuario'"], 'valida': False

print(analizar_consulta("INSERT INTO producto VALUES (1, 'Laptop', 1500, 10)"))
# → valida: True (4 valores, 4 campos en 'producto')

print(analizar_consulta("DELETE FROM usuario;"))
# → valida: True
\# Gramática en forma BNF



<Programa>      → <Sentencia>+

<Sentencia>     → <DeclVector> | <Asignacion> | <Print>

<DeclVector>    → vector ID \[ NUM ] ;

<Asignacion>    → ID = <VectorLiteral> ;

&nbsp;                | ID = dot ( ID , ID ) ;

<VectorLiteral> → \[ <ListaValores> ]

<ListaValores>  → NUM | NUM , <ListaValores>

<Print>         → print ( ID ) ;





\# Gramática atribuida



DeclVector → vector ID \[ NUM ] ;

&nbsp;          { TablaSimbolos.agregar(ID.lex, tipo="vector", dim=NUM.valor) }



Asignacion → ID = dot ( ID₁ , ID₂ ) ;

&nbsp;          { 

&nbsp;            dim1 = TablaSimbolos.consultar(ID₁.lex).dim;

&nbsp;            dim2 = TablaSimbolos.consultar(ID₂.lex).dim;

&nbsp;            si dim1 ≠ dim2 → error("Dimensión incompatible para dot product");

&nbsp;            TablaSimbolos.agregar(ID.lex, tipo="escalar");

&nbsp;          }


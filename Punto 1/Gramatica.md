# Estructura básica:



<Consulta>      → <Select> | <Insert> | <Update> | <Delete>

<Select>        → SELECT <ListaCampos> FROM <Tabla>

<Insert>        → INSERT INTO <Tabla> VALUES ( <ListaValores> )

<Update>        → UPDATE <Tabla> SET <Asignaciones>

<Delete>        → DELETE FROM <Tabla>



<ListaCampos>   → ID | ID , <ListaCampos>

<ListaValores>  → VALOR | VALOR , <ListaValores>

<Asignaciones>  → ID = VALOR | ID = VALOR , <Asignaciones>

<Tabla>         → ID



# Gramática Atribuida



Consulta → Select { Consulta.tipo = Select.tipo; Consulta.tabla = Select.tabla; }

&nbsp;       | Insert { Consulta.tipo = Insert.tipo; Consulta.tabla = Insert.tabla; }

&nbsp;       | Update { Consulta.tipo = Update.tipo; Consulta.tabla = Update.tabla; }

&nbsp;       | Delete { Consulta.tipo = Delete.tipo; Consulta.tabla = Delete.tabla; }



Select → SELECT ListaCampos FROM Tabla

&nbsp;      { Select.tipo = "SELECT";

&nbsp;        Select.tabla = Tabla.nombre;

&nbsp;        ListaCampos.camposValidos = Tabla.campos;  ← heredado

&nbsp;        Select.usados = ListaCampos.usados;

&nbsp;        Select.valida = ListaCampos.valida; }



Insert → INSERT INTO Tabla VALUES ( ListaValores )

&nbsp;      { Insert.tipo = "INSERT";

&nbsp;        Insert.tabla = Tabla.nombre;

&nbsp;        ListaValores.cantEsperada = longitud(Tabla.campos);  ← heredado (ej: 2)

&nbsp;        Insert.cantValores = ListaValores.cantidad;

&nbsp;        Insert.valida = (Insert.cantValores == ListaValores.cantEsperada); }



Update → UPDATE Tabla SET Asignaciones

&nbsp;      { Update.tipo = "UPDATE";

&nbsp;        Update.tabla = Tabla.nombre;

&nbsp;        Asignaciones.camposValidos = Tabla.campos;  ← heredado

&nbsp;        Update.usados = Asignaciones.usados;

&nbsp;        Update.valida = Asignaciones.valida; }



Delete → DELETE FROM Tabla

&nbsp;      { Delete.tipo = "DELETE";

&nbsp;        Delete.tabla = Tabla.nombre;

&nbsp;        Delete.valida = true; }



Tabla → ID

&nbsp;     { Tabla.nombre = ID.lex;

&nbsp;       Tabla.campos = obtenerCampos(ID.lex); }  ← función ficticia (ej: si ID="usuario" → \["id","nombre","edad"])



ListaCampos → ID { ListaCampos.usados = \[ID.lex];

&nbsp;                  ListaCampos.valida = (ID.lex ∈ ListaCampos.camposValidos); }

&nbsp;           | ID , ListaCampos₂

&nbsp;                  { ListaCampos.usados = \[ID.lex] ++ ListaCampos₂.usados;

&nbsp;                    ListaCampos.valida = (ID.lex ∈ ListaCampos.camposValidos) ∧ ListaCampos₂.valida; }



Asignaciones → ID = VALOR

&nbsp;            { Asignaciones.usados = \[ID.lex];

&nbsp;              Asignaciones.valida = (ID.lex ∈ Asignaciones.camposValidos); }

&nbsp;          | ID = VALOR , Asignaciones₂

&nbsp;            { Asignaciones.usados = \[ID.lex] ++ Asignaciones₂.usados;

&nbsp;              Asignaciones.valida = (ID.lex ∈ Asignaciones.camposValidos) ∧ Asignaciones₂.valida; }



ListaValores → VALOR { ListaValores.cantidad = 1; }

&nbsp;            | VALOR , ListaValores₂ { ListaValores.cantidad = 1 + ListaValores₂.cantidad; }



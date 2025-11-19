grammar DotLang;

// Reglas parser
program     : statement+ EOF ;

statement   : declVector
            | assignment
            | printStmt ;

declVector  : 'vector' ID '[' INT ']' ';' ;

assignment  : ID '=' vectorLiteral ';'
            | ID '=' 'dot' '(' ID ',' ID ')' ';' ;

vectorLiteral: '[' (INT (',' INT)*)? ']' ;

printStmt   : 'print' '(' ID ')' ';' ;

// Reglas lexer
ID          : [a-zA-Z][a-zA-Z0-9_]* ;
INT         : [0-9]+ ;
WS          : [ \t\r\n]+ -> skip ;
COMMENT     : '//' ~[\r\n]* -> skip ;
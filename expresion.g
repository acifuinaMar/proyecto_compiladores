grammar expresion;
root
    : PROGRAM LLAVEI sentencia* LLAVED EOF
;

sentencia
    : asignacion
    | expresionSi
    | expresion
;

asignacion
    : ID ASIG expresion
;
expresionSi
    : SI PAI expresion PAD bloque
    | SI PAI expresion PAD bloque SINO bloque
;

bloque
    : LLAVEI sentencia* LLAVED
;

expresion
    : orLogico
;

orLogico
    : andLogico (OR andLogico)*
;

andLogico
    : igualdad (AND igualdad)*
;

igualdad
    : comparacion ((IGUAL | NOIGUAL) comparacion)*
;

comparacion
    : suma ((MAYOR | MENOR | MAYORI | MENORI) suma)*
;

suma
    : multiplicacion ((SUM | RES) multiplicacion)*
;

multiplicacion
    : unico ((MUL | DIV) unico)*
;

unico
    : NOT unico
    | base
;

base
    : NUM
    | ID
    | PAI expresion PAD
;

// Palabras clave
PROGRAM: 'program';
SI     : 'si';
SINO   : 'sino';

// Símbolos
LLAVEI: '{';
LLAVED: '}';
PAI   : '(';
PAD   : ')';
ASIG  : '=';

// Operadores aritméticos
SUM : '+';
RES : '-';
MUL : '*';
DIV : '/';

// Operadores relacionales
IGUAL   : '==';
NOIGUAL : '!=';
MENOR   : '<';
MAYOR   : '>';
MENORI  : '<=';
MAYORI  : '>=';

// Operadores lógicos
AND : '&&';
OR  : '||';
NOT : '!';

// Valores
NUM : [0-9]+;
ID  : [a-zA-Z][a-zA-Z0-9]*;

// Espacios
WS : [ \n\t\r]+ -> skip;
grammar expresion;
root
    : PROGRAM LLAVEI sentencia* LLAVED EOF
;

sentencia
    : declaracion 
    | asignacion FINAL
    | expresionSi 
    | printt
    | cicloWhile
    | cicloFor
    | funcion
    | returnStmt
    | expresion FINAL
;
funcion
    : TIPO ID PAI parametros? PAD bloque
;

parametros
    : parametro (',' parametro)*
;

parametro
    : TIPO ID
;
asignacion
    : ID ASIG expresion
;
expresionSi
    : SI PAI expresion PAD bloque
    | SI PAI expresion PAD bloque SINO bloque
;

cicloWhile
    : WHILE PAI expresion PAD bloque
;

cicloFor
    : FOR PAI (declaracion | asignacion) expresion FINAL asignacion PAD bloque
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

llamadaFuncion
    : ID PAI argumentos? PAD
;

argumentos
    : expresion (',' expresion)*
;

returnStmt
    : RETURN expresion? FINAL
;

base
    : llamadaFuncion
    | FLOAT
    | NUM
    | STRING
    | VERDADERO
    | FALSO
    | ID
    | PAI expresion PAD
;

declaracion
    : TIPO ID ASIG expresion FINAL
    | TIPO ID FINAL
;

printt
    : PRINT PAI expresion PAD FINAL
;

// Palabras clave
PROGRAM: 'program';
SI     : 'si';
SINO   : 'sino';
WHILE : 'while';
FOR : 'for';

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

// return
RETURN : 'return';

//Imprimir
PRINT : 'print';

// Tipos de datos
TIPO : 'int' | 'bool' | 'string' | 'float' | 'void';
VERDADERO : 'verdadero';
FALSO : 'falso';
STRING : '"' .*? '"';
FLOAT  : [0-9]+ '.' [0-9]+;

// Valores
NUM : [0-9]+;
ID  : [a-zA-Z][a-zA-Z0-9]*;

//Delimitador de linea
FINAL : ';';

// Espacios
WS : [ \n\t\r]+ -> skip;
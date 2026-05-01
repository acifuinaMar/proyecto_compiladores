grammar gramatica_final;

/**
 * --- REGLAS SINTÁCTICAS ---
 */

root
    : PROGRAM LLAVEI programa* LLAVED EOF
    ;

programa
    : funcion 
    | declaracion 
    | sentenciaGlobal 
    | cicloWhile
    | cicloFor 
    | expresionSi
    ;

/**
 * --- IMPORT ---
 */
importStmt
    : 'import' ID FINAL
    ;

sentenciaGlobal
    : printt 
    | asignacion FINAL
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

// ================= DECLARACIÓN (incluye arrays)
declaracion
    : TIPO ID ASIG expresion FINAL 
    | TIPO ID FINAL
    | TIPO CORI CORD ID ASIG arrayLiteral FINAL
    ;

arrayLiteral
    : CORI (expresion (',' expresion)*)? CORD
    ;

sentencia
    : declaracion
    | asignacion FINAL
    | expresionSi
    | printt
    | cicloWhile
    | cicloFor
    | returnStmt
    | breakStmt
    | continueStmt
    ;

asignacion
    : ID ASIG expresion
    ;

expresionSi
    : SI PAI expresion PAD bloque (SINO bloque)?
    ;

cicloWhile
    : WHILE PAI expresion PAD bloque
    ;

cicloFor
    : FOR PAI (declaracion | asignacion) FINAL expresion FINAL asignacion PAD bloque
    ;

// ================= NUEVO
breakStmt
    : 'break' FINAL
    ;

continueStmt
    : 'continue' FINAL
    ;

bloque
    : LLAVEI sentencia* LLAVED
    ;

/**
 * --- EXPRESIONES ---
 */

expresion
    : comparacion
    ;

comparacion
    : suma ( (MAYOR | MENOR | MAYORI | MENORI | IGUAL | NOIGUAL) suma )*
    ;

suma
    : termino ( (SUM | RES) termino )*
    ;

termino
    : factor ( (MUL | DIV | MOD) factor )*
    ;

factor
    : NUM
    | STRING
    | llamadaFuncion
    | ID '[' expresion ']'
    | ID
    | PAI expresion PAD
    | NOT factor
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

printt
    : PRINT PAI expresion PAD FINAL
    ;

/**
 * --- TOKENS ---
 */

// Palabras Reservadas
PROGRAM : 'program';
SI      : 'si';
SINO    : 'sino';
WHILE   : 'while';
FOR     : 'for';
RETURN  : 'return';
PRINT   : 'print';

// Tipos
TIPO    : 'int' | 'bool' | 'string' | 'float' | 'void';

// Símbolos
LLAVEI  : '{';
LLAVED  : '}';
PAI     : '(';
PAD     : ')';
CORI    : '[';
CORD    : ']';
ASIG    : '=';
FINAL   : ';';

// Operadores
SUM     : '+';
RES     : '-';
MUL     : '*';
DIV     : '/';
MOD     : '%'; 

IGUAL   : '==';
NOIGUAL : '!=';
MENOR   : '<';
MAYOR   : '>';
MENORI  : '<=';
MAYORI  : '>=';

AND     : '&&';
OR      : '||';
NOT     : '!';

// Literales
STRING  : '"' .*? '"';
NUM     : [0-9]+;
ID      : [a-zA-Z_][a-zA-Z0-9_]*;

// Comentarios
COMENTARIO_LINEA  : '//' ~[\r\n]* -> skip;
COMENTARIO_BLOQUE : '/*' .*? '*/' -> skip;

// Espacios
WS : [ \n\t\r]+ -> skip;
grammar gramatica_final;

/**
 * --- REGLAS SINTÁCTICAS ---
 * Representan la estructura lógica del lenguaje.
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

declaracion
    : TIPO ID ASIG expresion FINAL 
    | TIPO ID FINAL
    ;

sentencia
    : declaracion
    | asignacion FINAL
    | expresionSi
    | printt
    | cicloWhile
    | cicloFor
    | returnStmt
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

bloque
    : LLAVEI sentencia* LLAVED
    ;

/**
 * --- JERARQUÍA DE EXPRESIONES ---
 * Organizadas por precedencia (de menor a mayor).
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
    : factor ( (MUL | DIV) factor )*
    ;

factor
    : NUM
    | STRING
    | ID
    | llamadaFuncion
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
 * --- TOKENS LÉXICOS ---
 * Definición de palabras reservadas, operadores y símbolos.
 */

// Palabras Reservadas
PROGRAM : 'program';
SI      : 'si';
SINO    : 'sino';
WHILE   : 'while';
FOR     : 'for';
RETURN  : 'return';
PRINT   : 'print';

// Tipos de Datos
TIPO    : 'int' | 'bool' | 'string' | 'float' | 'void';

// Símbolos de Agrupación y Puntuación
LLAVEI  : '{';
LLAVED  : '}';
PAI     : '(';
PAD     : ')';
ASIG    : '=';
FINAL   : ';';

// Operadores Aritméticos
SUM     : '+';
RES     : '-';
MUL     : '*';
DIV     : '/';

// Operadores Relacionales
IGUAL   : '==';
NOIGUAL : '!=';
MENOR   : '<';
MAYOR   : '>';
MENORI  : '<=';
MAYORI  : '>=';

// Operadores Lógicos
AND     : '&&';
OR      : '||';
NOT     : '!';

// Literales e Identificadores
STRING  : '"' .*? '"';
NUM     : [0-9]+;
ID      : [a-zA-Z_][a-zA-Z0-9_]*;

// Ignorar espacios en blanco
WS      : [ \n\t\r]+ -> skip;
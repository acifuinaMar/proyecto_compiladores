grammar gramatica_final;

root: PROGRAM LLAVEI programa* LLAVED EOF;

programa: funcion | declaracion | sentenciaGlobal | cicloWhile;

sentenciaGlobal: printt | asignacion FINAL;

funcion: TIPO ID PAI parametros? PAD bloque;
parametros: parametro (',' parametro)*;
parametro: TIPO ID;

declaracion: TIPO ID ASIG expresion FINAL | TIPO ID FINAL;

sentencia: declaracion
         | asignacion FINAL
         | expresionSi
         | printt
         | cicloWhile
         | cicloFor
         | returnStmt
         ;

asignacion: ID ASIG expresion;

expresionSi: SI PAI expresion PAD bloque (SINO bloque)?;

cicloWhile: WHILE PAI expresion PAD bloque;

cicloFor: FOR PAI (declaracion | asignacion) FINAL expresion FINAL asignacion PAD bloque;

bloque: LLAVEI sentencia* LLAVED;

// ===== REGLAS DE EXPRESIÓN CORREGIDAS =====
expresion: comparacion;

comparacion: suma (('>' | '<' | '>=' | '<=') suma)*;

suma: termino (('+' | '-') termino)*;

termino: factor (('*' | '/') factor)*;

factor: NUM
      | STRING
      | ID
      | llamadaFuncion
      | PAI expresion PAD
      | NOT factor
      ;

llamadaFuncion: ID PAI argumentos? PAD;
argumentos: expresion (',' expresion)*;
returnStmt: RETURN expresion? FINAL;
printt: PRINT PAI expresion PAD FINAL;

// LEXER
PROGRAM: 'program';
SI: 'si';
SINO: 'sino';
WHILE: 'while';
FOR: 'for';
RETURN: 'return';
PRINT: 'print';

TIPO: 'int' | 'bool' | 'string' | 'float';

LLAVEI: '{';
LLAVED: '}';
PAI: '(';
PAD: ')';
ASIG: '=';
FINAL: ';';

SUM: '+';
RES: '-';
MUL: '*';
DIV: '/';
IGUAL: '==';
NOIGUAL: '!=';
MENOR: '<';
MAYOR: '>';
MENORI: '<=';
MAYORI: '>=';

AND: '&&';
OR: '||';
NOT: '!';

STRING: '"' .*? '"';
NUM: [0-9]+;
ID: [a-zA-Z_][a-zA-Z0-9_]*;

COMENTARIO_LINEA: '//' ~[\r\n]* -> skip;
COMENTARIO_BLOQUE: '/*' .*? '*/' -> skip;
WS: [ \n\t\r]+ -> skip;
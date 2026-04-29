grammar gramatica_final;

root: PROGRAM LLAVEI sentencia* LLAVED EOF;

sentencia: declaracion | asignacion FINAL | printt;

declaracion: TIPO ID ASIG expresion FINAL | TIPO ID FINAL;

asignacion: ID ASIG expresion;

printt: PRINT PAI expresion PAD FINAL;

expresion: suma;
suma: termino (('+' | '-') termino)*;
termino: factor (('*' | '/' | '%') factor)*;
factor: NUM | ID | PAI expresion PAD;

PROGRAM: 'program';
PRINT: 'print';
TIPO: 'int';
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
MOD: '%';
NUM: [0-9]+;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \n\t\r]+ -> skip;

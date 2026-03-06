grammar expresion;
root
    : expresion+ EOF
    ;

// Expresiones
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
expresionSi
    : SI PAI expresion PAD PAI expresion PAD
    | SI PAI expresion PAD PAI expresion PAD SINO PAI expresion PAD
    ;

// cosas que ya no puedo simplificar mas
base
    : NUM
    | ID
    | PAI expresion PAD
    | expresionSi
    ;

// Operadores aritméticos

SUM : '+' ;
RES : '-' ;
MUL : '*' ;
DIV : '/' ;

// Parentesis

PAI : '(' ;
PAD : ')' ;

// Operadores relacionales

IGUAL   : '==' ;
NOIGUAL : '!=' ;
MENOR   : '<' ;
MAYOR   : '>' ;
MENORI  : '<=' ;
MAYORI  : '>=' ;

// Operadores lógicos

AND : '&&' ;
OR  : '||' ;
NOT : '!' ;

//Condicional
SI   : 'si' ;
SINO : 'sino' ;

// Tokens
NUM : [0-9]+ ;
ID  : [a-zA-Z][a-zA-Z0-9]* ;

// Espacios en blanco
WS : [ \n\t\r]+ -> skip ;
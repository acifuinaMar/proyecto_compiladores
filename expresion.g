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
    : unario ((MUL | DIV) unario)*
    ;
unario
    : NOT unario
    | base
    ;


// cosas que ya no puedo simplificar mas
base
    : NUM
    | ID
    | PAI expresion PAD
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

// Tokens 

NUM : [0-9]+ ;
ID  : [a-zA-Z][a-zA-Z0-9]* ;

// Espacios en blanco
WS : [ \n\t\r]+ -> skip ;
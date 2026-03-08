grammar expresion;
root
//Asi garantizo que el programa vaya dentro de {}
    : PROGRAM LLAVEI sentencia* LLAVED EOF
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
//Para poder tener x=5 o 3+4 o un si
sentencia
    : asignacion
    | expresion
;

//asignacion
asignacion
    : ID ASIG expresion
;

// cosas que ya no puedo simplificar mas
base
    : NUM
    | ID
    | PAI expresion PAD
    | expresionSi
;

//Asignacion y programa
PROGRAM: 'program';
ASIG:   '=';
LLAVEI: '{';
LLAVED: '}';

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

// Variables y numeros
NUM : [0-9]+ ;
ID  : [a-zA-Z][a-zA-Z0-9]* ;

// Espacios en blanco
WS : [ \n\t\r]+ -> skip ;
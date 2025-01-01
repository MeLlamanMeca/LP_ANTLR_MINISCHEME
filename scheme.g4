grammar scheme;

root: definitions* main;

definitions: defineFunction
    | defineConstant
    ;
main: '(' 'define' '(' 'main' ')' expression* ')';

expression
    : ifExpression
    | defineConstant
    | condExpression
    | letExpression
    | literal
    | listExpression
    | readExpression
    | displayExpression
    | arithmeticExpression
    | comparisonExpression
    | logicalExpression
    | consultExpression
    | editConstantExpression
    | newLine
    | functionCall
    | beginExpression
    ;

//Cualquier expresion recibida que no sea una lista, sera tratada como una lista de un solo elemento.
listExpression
    : '\'' '(' expression* ')' #listCreation
    | '(' 'car' expression ')' #carExpression
    | '(' 'cdr' expression ')' #cdrExpression
    | '(' 'cons' expression expression ')' #consExpression
    | '(' 'null?' expression ')' #nullExpression
    | '(' 'append' expression expression ')' #appendExpression
    | '(' 'length' expression ')' #lengthExpression
    ;

displayExpression: '(' 'display' expression ')';
defineFunction: '(' 'define' '(' IDENTIFIER (IDENTIFIER)* ')' expression ')';
defineConstant: '(' 'define' IDENTIFIER expression ')';
ifExpression: '(' 'if' expression expression expression ')';
condExpression: '(' 'cond' ( '(' expression expression ')' )* ')';
letExpression: '(' 'let' '(' ( '(' IDENTIFIER expression ')' )* ')' expression ')';
functionCall: '(' IDENTIFIER expression* ')' ;
readExpression: '(' 'read' ')';

//Las expresiones aritmeticas solo aceptan numeros. En caso contrario, el resultado es inesperado. El resultado es un numero.
arithmeticExpression: '(' ('+'| '-' | '/' | '*' | 'mod' | '^' | 'max' | 'min') expression expression+ ')'; 
//Las expresiones de comparacion solo aceptan numeros(o booleanos en caso de =). En caso contrario, el resultado es inesperado. El resultado es un booleano.
comparisonExpression: '(' ('='|'<'|'>'|'<='|'>='| '<>') expression expression')';
//Las expresiones logicas solo aceptan booleanos. En caso contrario, el resultado es inesperado. El resultado es un booleano.
logicalExpression: '(' ('and'|'or' | 'nor' | 'xor' | 'nand' | 'xnor' | 'implies') expression* ')';
//Las expresiones de consulta aceptan numeros, booleanos, strings o listas. En caso de que el tipo de dato no sea el esperado, el resultado es inesperado. El resultado es un booleano.
consultExpression: '(' ('not' | 'number?' | 'boolean?' | 'string?' | 'list?') expression ')';

newLine: '(' 'newline' ')';
editConstantExpression: '(' 'set!' IDENTIFIER expression ')';
beginExpression: '(' 'begin' expression* ')';

literal
    : NUMBER #numberLiteral
    | BOOLEAN #booleanLiteral
    | STRING #stringLiteral
    | IDENTIFIER #identifierLiteral
    ;

NUMBER: [0-9]+;
BOOLEAN: '#t' | '#f' | 'else';
STRING: '"' .*? '"';
IDENTIFIER: [a-zA-Z][?_a-zA-Z-0-9]*;
WS: [ \t\r\n]+ -> skip;
COMMENT: ';' .*? '\n' -> skip;
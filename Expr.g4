grammar Expr;

WS: ' ' -> skip;

ADD: '+';
SUBSTRACT: '-';
MULTIPLY: '*';
DIVIDE:  '/';
MOD: '%';
EQ: '=';
LPAREN: '(';
RPAREN: ')';
LCURL: '{';
RCURL: '}';
LTHAN: '<';
GTHAN: '>';
EQEQ: '==';
NOTEQ: '!=';
AND: '&&';
OR: '||';
NOT: '!';

IF: 'if';
WHILE: 'while';
NEWLINE: [\r\n]+ ;
PRINT: 'print';
IDENTIFIER: ('a'..'z' | 'A'..'Z') ('0'..'9' | 'a'..'z' | 'A'..'Z')*;
INTLITERAL: ('-'? ('1'..'9')('0'..'9')*) | '0';
INPUT: 'input()';

DOT: '.';

prog: (expr NEWLINE*)*;

expr: (print_function DOT
    | if_statement DOT
    | variable_assign DOT
    | while_loop DOT
    | NEWLINE);


variable_assign:  IDENTIFIER EQ literals | IDENTIFIER EQ INPUT;

print_function: PRINT LPAREN literals RPAREN;

operators: MULTIPLY
            | DIVIDE
            | ADD
            | MOD
            | SUBSTRACT;

logic_operators: AND
                | OR;

literals: IDENTIFIER | INTLITERAL | literals operators literals;

comparisson_type: EQEQ
          | GTHAN
          | LTHAN
          | NOTEQ;

if_statement: IF NOT? LPAREN condition RPAREN LCURL NEWLINE*
                expr* NEWLINE*
                RCURL;

condition: literals comparisson_type literals
        | condition logic_operators condition;

while_loop: WHILE NOT? LPAREN  condition RPAREN LCURL NEWLINE*
        expr* NEWLINE*
        RCURL;

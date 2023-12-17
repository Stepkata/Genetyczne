grammar Expr;

WS: ' ' -> skip;

ADD: '+';
SUBSTRACT: '-';
MULTIPLY: '*';
DIVIDE:  '/';
MOD: '%';


EQ: '=';

RANGE: '..';
IN: 'in';

COLON: ':';
COMA : ',';
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

SINGLE_QUOTE: '\'';
IF: 'if';
ELSE: 'else';
FOR: 'for';

VAL: 'val';
VAR: 'var';

NEWLINE: [\r\n]+ ;
INT: 'Int';
DOUBLE: 'Double';
STRING: 'String';
BOOLEAN: 'Boolean';

IDENTIFIER: ('a'..'z' | 'A'..'Z') ('0'..'9' | 'a'..'z' | 'A'..'Z')*;
INTLITERAL: ('-'? ('1'..'9')('0'..'9')*) | '0';
DOUBLELITERAL:  ('0'..'9')+ '.' ('0'..'9')+ ;
STRINGLITERAL: UNTERMINATEDSTRINGLITERAL '"';
UNTERMINATEDSTRINGLITERAL : '"' (~["\\\r\n] | '\\' (. | EOF))*;
BOOLEANLITERAL: 'true' | 'false';
INTNUMBER: ('0'..'9');
PRINT: 'print';
READ: 'read';


prog: (expr NEWLINE*)*;

expr: (variable
    | if_statement
    | for_loop
    | NEWLINE
    | func_call);


variable: variable_assign | variable_declaration;
variable_declaration: (VAR|VAL) IDENTIFIER COLON typ (EQ literals)?;
variable_assign: (VAR|VAL)? IDENTIFIER EQ literals;

parameter:  IDENTIFIER COLON typ;

operators: MULTIPLY
            | DIVIDE
            | ADD
            | SUBSTRACT;


logic_operators: AND
                | OR;

numeric_literals: numeric_type operators numeric_type
        | numeric_type;

text_type: text_type  ADD text_type
        | STRINGLITERAL
        | IDENTIFIER;

numeric_type:   INTLITERAL
              | DOUBLELITERAL
              | IDENTIFIER;


literals:   BOOLEANLITERAL
        | text_type
        | numeric_literals
        | func_call
        | IDENTIFIER;

comparisson_type: EQEQ
          | GTHAN
          | LTHAN
          | NOTEQ;


typ:  INT
    | DOUBLE
    | STRING
    | IDENTIFIER
    | BOOLEAN;

if_statement: IF LPAREN if_body RPAREN LCURL NEWLINE*
                expr* NEWLINE*
                RCURL NEWLINE*  (ELSE if_statement |
                         ELSE LCURL NEWLINE* expr* RCURL NEWLINE* )?;

if_body: literals comparisson_type literals
        | if_body logic_operators if_body;


for_loop_condition: INTLITERAL  RANGE  INTLITERAL;

for_loop: FOR LPAREN IDENTIFIER IN for_loop_condition RPAREN LCURL NEWLINE*
            expr*
            RCURL;

func_call: ( PRINT LPAREN (IDENTIFIER| text_type+) RPAREN )| (READ LPAREN IDENTIFIER RPAREN);
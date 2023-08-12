parser grammar ExprParser;
options { tokenVocab=ExprLexer; }

program
    : expr EOF
    // | def EOF
    ;
expr: LPAREN expr RPAREN
    |<assoc=right> expr POW expr
    | expr DIV expr
    | expr MUL expr
    | expr PLUS expr
    | expr MINUS expr 
    | INT ;

// stat: ID '=' expr ';'
//     | expr ';'
//     ;

// def : ID '(' ID (',' ID)* ')' '{' stat* '}' ;

// expr: ID
//     | INT
//     | func
//     | 'not' expr
//     | expr 'and' expr
//     | expr 'or' expr
//     ;
// func : ID '(' expr (',' expr)* ')' ;
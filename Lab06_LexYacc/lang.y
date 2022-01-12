%{
#include <stdio.h>
#include <stdlib.h>

#define YYDEBUG 1 
%}

%token READ
%token START
%token WRITE
%token IF
%token ELSE
%token FOR
%token WHILE
%token BREAK
%token INTEGER
%token STRING
%token CHARACTER
%token ARRAY
%token RETURN

%token IDENTIFIER
%token CONSTANT

%token ATRIB
%token EQ
%token NE
%token LT
%token LE
%token GT
%token GE
%token NOT 
%token ASIGN

%left '+' '-' '*' '/'

%token ADD 
%token SUB
%token DIV 
%token MOD 
%token MUL 

%token OPEN_CURLY_BRACKET
%token CLOSED_CURLY_BRACKET 
%token OPEN_ROUND_BRACKET
%token CLOSED_ROUND_BRACKET
%token OPEN_RIGHT_BRACKET
%token CLOSED_RIGHT_BRACKET 

%token COMMA 
%token SEMI_COLON

%start program

%%
program : START compoundStatement
        ;
simpleType :  INTEGER | STRING | CHARACTER
        ;
type :  simpleType
        ;
compoundStatement : OPEN_CURLY_BRACKET statementList CLOSED_CURLY_BRACKET
        ;
statementList : statement |  statement SEMI_COLON statementList
        ;
statement : assignStatement | ioStatement | declaration | ifStatement | forStatement | whileStatement
        ;
assignStatement : IDENTIFIER EQ statement
        ;
ioStatement : READ IDENTIFIER | WRITE IDENTIFIER | WRITE CONSTANT
        ;     
declaration : type IDENTIFIER
	    ;
ifStatement : IF condition statement ELSE statement
        ;
forStatement :  FOR OPEN_ROUND_BRACKET assignStatement SEMI_COLON condition SEMI_COLON assignStatement CLOSED_ROUND_BRACKET statement
        ;	
whileStatement :  WHILE condition statement
        ;   
condition : expression relation expression
        ;
relation : LT | LE | EQ | NE | GT | GE
    ;
expression : IDENTIFIER | INTEGER
        ;
%%
yyerror(char *s)
{	
	printf("%s\n",s);
}

extern FILE *yyin;

int main(int argc, char **argv)
{
	if(argc>1) yyin :  fopen(argv[1],"r");
	if(argc>2 && !strcmp(argv[2],"-d")) yydebug: 1;
	if(!yyparse()) fprintf(stderr, "\tO.K.\n");
}

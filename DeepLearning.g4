grammar DeepLearning;

options {
    language = Python3;
}

program
    : statement* EOF
    ;

statement
    : assignment
    | matrixDecl
    | modelDecl
    | ifStmt
    | forStmt
    | printStmt 
    | whileStmt
    | doWhileStmt
    | funcDecl
    | returnStmt
    | block
    ;

assignment
    : ID ASSIGN expr SEMI
    ;

assignNoSemi
    : ID ASSIGN expr
    ;

matrixDecl
    : MATRIX ID ASSIGN matrixLiteral SEMI
    ;

matrixLiteral
    : LBRACK row (COMMA row)* RBRACK
    ;

row
    : LBRACK expr (COMMA expr)* RBRACK
    ;



modelDecl
    : MODEL ID ASSIGN mlpDecl SEMI
    | MODEL ID SEMI
    ;

mlpDecl
    : MLP LPAREN expr COMMA expr COMMA expr RPAREN
    ;


funcCallExpr
    : (
        ID
        | TRAIN | PREDICT | PLOT
        | SQRT | POW_FUNC | ABS | EXP | LOG
        | SIN | COS | TAN | ARCSIN | ARCCOS | ARCTAN
        | MEAN | STD | SUM | MAX | MIN
        | TRANSPOSE | INVERSE | DOT_KW | ZEROS | ONES
        | IDENTITY | DETERMINANT | RESHAPE
        | READ_FILE | WRITE_FILE | READ_CSV | WRITE_CSV
        | SAVE_MODEL | LOAD_MODEL
        | SIGMOID | RELU | TANH_FUNC | SOFTMAX | LEAKY_RELU
        | MSE | CROSS_ENTROPY | MAE
        | PRINT | LEN | RANGE | TYPE | SHAPE | NORMALIZE | SPLIT_DATA
        | KMEANS | KNN_CLASSIFIER | DECISION_TREE
        | NEURAL_NETWORK | ADD_LAYER | COMPILE | FIT | EVALUATE | CREATE_MLP
        | LINEAR_REGRESSION | PREDICT_LINEAR | R2_SCORE
        | SCATTER | HISTOGRAM | PLOT_LOSS | SHOW
    ) LPAREN args? RPAREN
    | ID DOT ID LPAREN args? RPAREN
    ;

printStmt
    : PRINT LPAREN args? RPAREN SEMI
    ;

args
    : expr (COMMA expr)*
    ;


ifStmt
    : IF LPAREN? expr RPAREN? block (ELSE block)?
    ;


/*
   FIX COMPLETO:
   - soporta estilo C sin errores: for (i=0; i<5; i=i+1)
   - soporta estilo Python: for i in lista : { ... }
*/
forStmt
    : FOR LPAREN assignNoSemi SEMI expr SEMI assignNoSemi RPAREN block
    | FOR ID IN expr COLON block
    ;


/* FIX: while con y sin paréntesis */
whileStmt
    : WHILE LPAREN expr RPAREN block
    | WHILE expr block
    ;

doWhileStmt
    : DO block WHILE LPAREN expr RPAREN SEMI
    ;


funcDecl
    : DEF ID LPAREN params? RPAREN COLON block
    ;

params
    : ID (COMMA ID)*
    ;

returnStmt
    : RETURN expr SEMI
    ;


block
    : LBRACE statement* RBRACE
    ;


expr
    : equalityExpr
    ;

equalityExpr
    : relationalExpr ( (EQ | NEQ) relationalExpr )*
    ;

relationalExpr
    : addExpr ( (LT | LE | GT | GE) addExpr )*
    ;

addExpr
    : mulExpr ( (PLUS | MINUS) mulExpr )*
    ;

mulExpr
    : powExpr ( (MULT | DIV | MOD) powExpr )*
    ;

powExpr
    : unaryExpr ( POW unaryExpr )*
    ;

unaryExpr
    : MINUS unaryExpr
    | primary
    ;

primary
    : NUMBER
    | STRING
    | ID
    | matrixLiteral
    | arrayLiteral
    | funcCallExpr
    | LPAREN expr RPAREN
    ;

arrayLiteral
    : LBRACK expr (COMMA expr)* RBRACK
    ;


IF      : 'if';
ELSE    : 'else';
FOR     : 'for';
WHILE   : 'while';
DO      : 'do';
IN      : 'in';
DEF     : 'def';
RETURN  : 'return';

// Keywords - Tipos y estructuras
MATRIX  : 'matrix';
MODEL   : 'model';
MLP     : 'MLP';

// Keywords - Funciones principales
TRAIN   : 'train';
PREDICT : 'predict';
PLOT    : 'plot';
READ    : 'read';

// Keywords - Matemáticas
SQRT    : 'sqrt';
POW_FUNC: 'pow';
ABS     : 'abs';
EXP     : 'exp';
LOG     : 'log';
SIN     : 'sin';
COS     : 'cos';
TAN     : 'tan';
ARCSIN  : 'arcsin';
ARCCOS  : 'arccos';
ARCTAN  : 'arctan';
MEAN    : 'mean';
STD     : 'std';
SUM     : 'sum';
MAX     : 'max';
MIN     : 'min';

// Keywords - Matrices
TRANSPOSE   : 'transpose';
INVERSE     : 'inverse';
DOT_KW      : 'dot';
ZEROS       : 'zeros';
ONES        : 'ones';
IDENTITY    : 'identity';
DETERMINANT : 'determinant';
RESHAPE     : 'reshape';

// Keywords - Archivos
READ_FILE   : 'read_file';
WRITE_FILE  : 'write_file';
READ_CSV    : 'read_csv';
WRITE_CSV   : 'write_csv';
SAVE_MODEL  : 'save_model';
LOAD_MODEL  : 'load_model';

// Keywords - Funciones de activación
SIGMOID     : 'sigmoid';
RELU        : 'relu';
TANH_FUNC   : 'tanh';
SOFTMAX     : 'softmax';
LEAKY_RELU  : 'leaky_relu';

// Keywords - Funciones de pérdida
MSE             : 'mse';
CROSS_ENTROPY   : 'cross_entropy';
MAE             : 'mae';

// Keywords - Utilidades
PRINT       : 'print';
LEN         : 'len';
RANGE       : 'range';
TYPE        : 'type';
SHAPE       : 'shape';
NORMALIZE   : 'normalize';
SPLIT_DATA  : 'split_data';

// Keywords - Clustering y clasificación
KMEANS          : 'kmeans';
KNN_CLASSIFIER  : 'knn_classifier';
DECISION_TREE   : 'decision_tree';

// Keywords - Redes neuronales
NEURAL_NETWORK  : 'neural_network';
ADD_LAYER       : 'add_layer';
COMPILE         : 'compile';
FIT             : 'fit';
EVALUATE        : 'evaluate';
CREATE_MLP      : 'create_mlp';

// Keywords - Regresión lineal
LINEAR_REGRESSION : 'linear_regression';
PREDICT_LINEAR    : 'predict_linear';
R2_SCORE          : 'r2_score';

// Keywords - Visualización
SCATTER     : 'scatter';
HISTOGRAM   : 'histogram';
PLOT_LOSS   : 'plot_loss';
SHOW        : 'show';

// Operadores aritméticos
PLUS    : '+';
MINUS   : '-';
MULT    : '*';
DIV     : '/';
POW     : '^';
MOD     : '%';
ASSIGN  : '=';

// Delimitadores
LPAREN  : '(';
RPAREN  : ')';
LBRACE  : '{';
RBRACE  : '}';
LBRACK  : '[';
RBRACK  : ']';
COMMA   : ',';
SEMI    : ';';
DOT     : '.';
COLON   : ':';

// Operadores relacionales 
LE      : '<=';
GE      : '>=';
EQ      : '==';
NEQ     : '!=';
LT      : '<';
GT      : '>';

// Identificadores 
ID
    : [a-zA-Z_] [a-zA-Z_0-9]*
    ;

// Números
NUMBER
    : DIGIT+ ('.' DIGIT*)?
    | '.' DIGIT+
    ;

fragment DIGIT : [0-9] ;

// Strings
STRING
    : '"' (~["\\] | '\\' . )* '"'
    ;

// Comentarios
LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

BLOCK_COMMENT
    : '/*' .*? '*/' -> skip
    ;

// Whitespace
WS
    : [ \t\r\n]+ -> skip
    ;

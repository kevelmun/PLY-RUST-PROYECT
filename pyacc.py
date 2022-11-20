import ply.yacc as yacc
from main import tokens


#KEVIN MUÑOZ

# GENERAL RULE
def p_main_rule(p):
    '''main_rule : father_rule
    | father_rule main_rule'''
    

# RULE WITH ALL THE OPTIONS TO MAKE
def p_father_rule(p):
    '''father_rule : print
    | dvariable
    | array
    | function
    | variables
    | control_str
    | expression
    | void
    | linkedlist
    | push
    | remove
    | if
    | else
    | else_if'''

#KEVIN MUÑOZ

# Rule for the different number expression
def p_expression(p):
    '''expression : expression PLUS expression
    | expression MINUS expression
    | expression TIMES expression
    | expression DIVIDE expression
    | LPAREN expression RPAREN
    | number'''


# Types of numbers
def p_number(p):
    '''number : INTEGER
    | FLOAT
    | VARIABLE'''

# LOBERLLY SALAZAR
def p_dataType(p):
    '''dataType : UNSIG_INT_8
                | UNSIG_INT_16
                | UNSIG_INT_32
                | UNSIG_INT_64
                | UNSIG_INT_128
                | SIG_INT_8
                | SIG_INT_16
                | SIG_INT_32
                | SIG_INT_64
                | SIG_INT_128
                | FLOAT_32
                | FLOAT_64
                | KW_BOOLEAN'''

#DANIEL GUERRERO
def p_data(p):
    '''data : CADENA
    | INTEGER
    | CHAR
    | FLOAT
    | KW_FALSE
    | KW_TRUE'''

def p_comparator(p):
    '''comparator :
    | EQ
    | NE
    | GE
    | LE
    | GT
    | LT'''

def p_and(p):
    'and : VARIABLE LAND VARIABLE'

def p_conditional(p):
    '''conditional : VARIABLE comparator data
    | and comparator data'''

def p_or(p):
    'or : VARIABLE LOR VARIABLE'

def p_mdata(p):
    '''mdata : data
    | data COMMA mdata'''

def p_print(p):
    'print : KW_PRINT LPAREN CADENA RPAREN SEMI'

def p_declare_variable(p):
    'dvariable : KW_LET VARIABLE SEMI'

def p_array(p):
    'array : KW_LET VARIABLE EQUALS LBRACKET mdata RBRACKET'

def p_variables(p):
    '''variables : VARIABLE 
    | VARIABLE COMMA variables'''

def p_while(p):
    'while : KW_WHILE LPAREN VARIABLE '
    
# KEVIN MUÑOZ

# Arguments for functions
def p_arguments(p):
    '''arguments : void
    | variables'''

# Function without arguments   
def p_function(p):
    'function : KW_FN VARIABLE LPAREN arguments RPAREN LBRACE father_rule RBRACE'


def p_control_str(p):
    '''control_str : for_str
    | for_str_tagged'''

def p_for_str(p):
    '''for_str : KW_FOR VARIABLE KW_IN range LBRACE father_rule RBRACE
    | KW_FOR VARIABLE KW_IN VARIABLE LBRACE father_rule RBRACE'''

def p_for_str_tagged(p):
    '''for_str_tagged : label COLON for_str'''

def p_range(p):
    '''range : INTEGER DOT DOT INTEGER
    | VARIABLE DOT DOT VARIABLE'''

def p_label(p):
    'label : QUOTE VARIABLE'

# Void rule productions
def p_void(p):
    '''void : '''
    pass

# LOBERLLY SALAZAR if, funcion con retorno, arraylist

## Arraylist

def p_linkedlist_empty(p):
    '''linkedlist : KW_LET VARIABLE COLON KW_LINKEDLIST LT dataType GT EQUALS KW_LINKEDLIST COLON COLON KW_NEW LPAREN RPAREN SEMI
                  | KW_LET KW_MUT VARIABLE COLON KW_LINKEDLIST LT dataType GT EQUALS KW_LINKEDLIST COLON COLON KW_NEW LPAREN RPAREN SEMI'''

def p_linkedlist_array(p):
    '''linkedlist : KW_LET VARIABLE EQUALS KW_LINKEDLIST COLON COLON KW_FROM LPAREN array RPAREN SEMI
                  | KW_LET KW_MUT VARIABLE EQUALS KW_LINKEDLIST COLON COLON KW_FROM LPAREN array RPAREN SEMI'''

def p_push(p):
    'push : VARIABLE DOT PUSH LPAREN data RPAREN SEMI'

def p_remove(p):
    'remove : VARIABLE DOT REMOVE LPAREN INTEGER RPAREN SEMI'

## if 

def p_if(p):
    'if : KW_IF conditional LBRACE father_rule RBRACE'

def p_else(p):
    'else : KW_ELSE LBRACE father_rule RBRACE'

def p_else_if(p):
    'else_if : KW_ELSE KW_IF conditional LBRACE father_rule RBRACE'

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


 # Build the parser
parser = yacc.yacc()
 
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
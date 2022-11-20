import ply.yacc as yacc
from main import tokens


#KEVIN MUÑOZ

# GENERAL RULE
def p_main_rule(p):
    '''main_rule : expression
    | expression main_rule'''
    

# RULE WITH ALL THE OPTIONS TO MAKE
def p_expression(p):
    '''expression : print
    | dvariable
    | array
    | function_argument
    | function
    | variables
    | void'''

#DANIEL GUERRERO
def p_print(p):
    'print : KW_PRINT LPAREN CADENA RPAREN SEMI'

def p_declare_variable(p):
    'dvariable : KW_LET VARIABLE SEMI'

def p_array(p):
    'array : LBRACKET RBRACKET'

def p_variables(p):
    '''variables : VARIABLE 
    | VARIABLE COMMA variables'''

# KEVIN MUÑOZ

# Function without arguments   
def p_function(p):
    'function : KW_FN VARIABLE LPAREN RPAREN LBRACKET expression RBRACKET'

def p_function_argument(p):
    'function_argument : KW_FN VARIABLE LPAREN variables RPAREN LBRACKET expression RBRACKET'





# Void rule productions
def p_void(p):
    '''void : '''
    pass

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
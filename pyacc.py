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
    | void'''

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
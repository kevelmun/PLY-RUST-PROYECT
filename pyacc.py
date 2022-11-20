import ply.yacc as yacc
from main import tokens


 # Error rule for syntax errors
def p_error(p):
     print("Syntax error in input!")
#DANIEL GUERRERO
def p_print(p):
    'IMPRIMIR : KW_PRINT LPAREN CADENA RPAREN SEMI'

def p_declare_variable(p):
    'DVARIABLE : KW_LET VARIABLE SEMI'

def p_array(p):
    'ARRAY : LBRACKET RBRACKET'

def p_variables(p):
    '''VARIABLES : VARIABLE 
    | VARIABLE VARIABLES'''

def p_function(p):
    'FUNCION : KW_FN VARIABLE LPAREN VARIABLES RPAREN LBRACKET IMPRIMIR RBRACKET'

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
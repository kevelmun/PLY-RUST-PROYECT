import ply.yacc as yacc
import datetime

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
    | function
    | variables
    | control_str
    | expression
    | void
    | data_str
    | array
    | linkedlist_methods
    | hashmap_methods
    | initialization'''

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
def p_data_type(p):
    '''data_type : UNSIG_INT_8
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
                | KW_BOOLEAN
                | KW_STRING'''

#DANIEL GUERRERO
def p_data(p):
    '''data : CADENA
    | INTEGER
    | CHAR
    | FLOAT
    | KW_FALSE
    | KW_TRUE
    | tuple'''

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
    '''array : KW_LET VARIABLE EQUALS LBRACKET mdata RBRACKET
    | LBRACKET mdata RBRACKET'''

def p_variables(p):
    '''variables : VARIABLE 
    | VARIABLE COMMA variables'''

def p_while(p):
    'while : KW_WHILE LPAREN VARIABLE '
    
# KEVIN MUÑOZ



def p_tuple(p):
    'tuple : LPAREN mdata RPAREN'

# Initialization full options
def p_initialization(p):
    '''initialization : let_initialization SEMI 
    | const_initialization SEMI 
    | data_str SEMI'''

# Let initializations possible options
def p_let_initialization(p):
    '''let_initialization : KW_LET VARIABLE EQUALS data
    | KW_LET VARIABLE COLON data_type EQUALS data
    | KW_LET KW_MUT VARIABLE EQUALS data
    | KW_LET KW_MUT VARIABLE COLON data_type EQUALS data
    | KW_LET VARIABLE EQUALS expression_var
    | KW_LET VARIABLE COLON data_type EQUALS expression_var
    | KW_LET KW_MUT VARIABLE EQUALS expression_var
    | KW_LET KW_MUT VARIABLE COLON data_type EQUALS expression_var'''

# Const initialization possible options
def p_const_initialization(p):
    'const_initialization : KW_CONST VARIABLE COLON data_type EQUALS data'

# Arguments for functions
def p_arguments(p):
    '''arguments : void
    | variables'''

# Function without arguments   
def p_function(p):
    'function : KW_FN VARIABLE LPAREN arguments RPAREN LBRACE main_rule RBRACE'

# Control structures
def p_control_str(p):
    '''control_str : for_str
    | for_str_tagged
    | if
    | else
    | else_if
    | while'''

# For structure
def p_for_str(p):
    '''for_str : KW_FOR VARIABLE KW_IN range LBRACE main_rule RBRACE
    | KW_FOR VARIABLE KW_IN VARIABLE LBRACE main_rule RBRACE'''

# For structure with label
def p_for_str_tagged(p):
    '''for_str_tagged : label COLON for_str'''

# Posible values to use a range 
def p_range(p):
    '''range : INTEGER DOT DOT INTEGER
    | VARIABLE DOT DOT VARIABLE'''

# Title tag to recognize a specific loop
def p_label(p):
    'label : QUOTE VARIABLE'

# Data structures
def p_data_str(p):
    '''data_str : array
    | hashmap
    | linkedlist'''

# HashMap structure
def p_hashmap(p):
    '''hashmap : KW_LET VARIABLE EQUALS KW_HASHMAP COLON COLON KW_NEW LPAREN RPAREN
    | KW_LET KW_MUT VARIABLE EQUALS KW_HASHMAP COLON COLON KW_NEW LPAREN RPAREN
    | KW_LET VARIABLE EQUALS KW_HASHMAP COLON COLON KW_FROM LPAREN array RPAREN
    | KW_LET KW_MUT VARIABLE EQUALS KW_HASHMAP COLON COLON KW_FROM LPAREN array RPAREN'''

# HashMap methods
def p_hashmap_methods(p):
    '''hashmap_methods : VARIABLE hashmap_insert
    | VARIABLE hashmap_remove'''

# HashMap insert
def p_hashmap_insert(p):
    'hashmap_insert : DOT KW_INSERT LPAREN mdata RPAREN SEMI'

# HashMap remove
def p_hashmap_remove(p):
    'hashmap_remove : DOT KW_REMOVE LPAREN AND data RPAREN SEMI'

# Void rule productions
def p_void(p):
    '''void : '''
    pass

# LOBERLLY SALAZAR if, funcion con retorno, arraylist

## Arraylist

def p_linkedlist_empty(p):
    '''linkedlist : KW_LET VARIABLE COLON KW_LINKEDLIST LT data_type GT EQUALS KW_LINKEDLIST COLON COLON KW_NEW LPAREN RPAREN
                  | KW_LET KW_MUT VARIABLE COLON KW_LINKEDLIST LT data_type GT EQUALS KW_LINKEDLIST COLON COLON KW_NEW LPAREN RPAREN'''

def p_linkedlist_array(p):
    '''linkedlist : KW_LET VARIABLE EQUALS KW_LINKEDLIST COLON COLON KW_FROM LPAREN array RPAREN
                  | KW_LET KW_MUT VARIABLE EQUALS KW_LINKEDLIST COLON COLON KW_FROM LPAREN array RPAREN'''

def p_linkedlist_methods(p):
    '''linkedlist_methods : VARIABLE linkedlist_push
    | VARIABLE linkedlist_remove'''

def p_linkedlist_push(p):
    'linkedlist_push : DOT KW_PUSH_BACK LPAREN data RPAREN SEMI'

def p_linkedlist_remove(p):
    'linkedlist_remove : DOT KW_REMOVE LPAREN INTEGER RPAREN SEMI'

## if data structure

def p_if(p):
    'if : KW_IF conditional LBRACE main_rule RBRACE'

def p_else(p):
    'else : KW_ELSE LBRACE main_rule RBRACE'

def p_else_if(p):
    'else_if : KW_ELSE KW_IF conditional LBRACE main_rule RBRACE'

## Function with a return value

def p_function_return(p):
    '''function : KW_FN VARIABLE LPAREN arguments RPAREN MINUS GT data_type LBRACE return RBRACE'''

def p_expression_var(p):
    '''expression_var : expression
                    | VARIABLE'''

def p_return_statement(p):
    '''return : main_rule
              | main_rule KW_RETURN expression_var SEMI'''

## Input of data

def p_input(p):
    ''

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


 # Build the parser
parser = yacc.yacc()
 
# while True:
#     try:
#         s = input('calc > ')
#     except EOFError:
#         break
#     if not s: continue
#     result = parser.parse(s)
#     print(result)

filew = open("log.txt","a")


timenow = datetime.datetime.now()

files = ["source4.txt"]
for file in files:
  with open(file) as archivo:
    linea = archivo.read()
    result = parser.parse(linea)
    print(str(result), " ", str(timenow))

    filew.write("DateTime: " + str(timenow) + " | File: " + file +" >> " + "Result:"+str(result) + " "  + "\n")
        
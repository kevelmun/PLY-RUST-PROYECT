import ply.yacc as yacc
import datetime

from main import tokens

filew = open("log.txt","a", encoding="utf-8")

error_number = 0

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
    | control_str
    | void
    | array
    | linkedlist_methods
    | hashmap_methods
    | initialization
    | input
    | assignation
    | declare_data_type'''

#KEVIN MUÑOZ

# Rule for the different number expression
def p_expression(p):
    '''expression : expression PLUS expression
    | expression MINUS expression
    | expression TIMES expression
    | LPAREN expression RPAREN
    | number
    | division
    | variable'''


# Types of numbers
def p_number(p):
    '''number : INTEGER
    | FLOAT'''

def p_variable(p):
    'variable : VARIABLE'

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
                | KW_STRING
                | KW_CHARACTER'''

# Asignation
def p_assign_operators(p):
    '''assign_operators : EQUALS
                        | TIMESEQUAL 
                        | DIVEQUAL
                        | MODULUSEQUAL
                        | PLUSEQUAL 
                        | MINUSEQUAL'''

#DANIEL GUERRERO
def p_semantic_cast_sigint(p):
    '''sigint : SIG_INT_8
    | SIG_INT_16
    | SIG_INT_32
    | SIG_INT_64
    | SIG_INT_128'''

def p_semantic_cast_unsigint(p):
    '''unsigint : UNSIG_INT_8
    | UNSIG_INT_16
    | UNSIG_INT_32
    | UNSIG_INT_64
    | UNSIG_INT_128''' 

def p_semantic_cast_float(p):
    '''flotante : FLOAT_32
    | FLOAT_64'''

def p_semantic_casting(p):
    '''casting : VARIABLE KW_AS sigint
    | VARIABLE KW_AS unsigint
    | VARIABLE KW_AS flotante'''

def p_semantic_division(p):
    '''division : INTEGER DIVIDE INTEGER
    | FLOAT DIVIDE FLOAT'''

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

def p_logic(p):
    '''logic : LOR
    | LAND'''

def p_logic_variable(p):
    '''lvariable : conditional 
    | VARIABLE
    | KW_TRUE
    | KW_FALSE
    | VARIABLE logic lvariable
    | conditional logic lvariable'''

def p_conditional(p):
    '''conditional : VARIABLE comparator data
    | data comparator VARIABLE
    | VARIABLE comparator VARIABLE
    | data comparator data'''

def p_mdata(p):
    '''mdata : data
    | data COMMA mdata'''

def p_print(p):
    '''print : KW_PRINT LNOT LPAREN CADENA RPAREN SEMI
    | KW_PRINT LNOT LPAREN CADENA COMMA VARIABLE RPAREN SEMI'''

def p_declare_variable(p):
    'dvariable : KW_LET VARIABLE COLON data_type SEMI'

def p_array(p):
    '''array : KW_LET VARIABLE EQUALS LBRACKET mdata RBRACKET SEMI
    | LBRACKET mdata RBRACKET
    | LBRACKET data SEMI data RBRACKET
    | KW_LET VARIABLE COLON LBRACKET data_type SEMI data RBRACKET EQUALS LBRACKET mdata RBRACKET SEMI
    | KW_LET VARIABLE COLON LBRACKET data_type SEMI data RBRACKET EQUALS LBRACKET data SEMI data RBRACKET SEMI
    | KW_LET KW_MUT VARIABLE COLON LBRACKET data_type SEMI data RBRACKET EQUALS LBRACKET mdata RBRACKET SEMI
    | KW_LET KW_MUT VARIABLE COLON LBRACKET data_type SEMI data RBRACKET EQUALS LBRACKET data SEMI data RBRACKET SEMI'''

def p_variables(p):
    '''variables : VARIABLE 
    | VARIABLE COMMA variables'''

def p_while(p):
    'while : KW_WHILE lvariable LBRACE main_rule RBRACE'
    
# KEVIN MUÑOZ


def p_tuple(p):
    'tuple : LPAREN mdata RPAREN'

# Initialization full options
def p_initialization(p):
    '''initialization : let_initialization SEMI 
    | const_initialization SEMI 
    | data_str SEMI
    | input_init SEMI'''

# Let initializations possible options
def p_let_initialization(p):
    '''let_initialization : KW_LET VARIABLE EQUALS data
    | KW_LET VARIABLE COLON data_type EQUALS data
    | KW_LET KW_MUT VARIABLE EQUALS data
    | KW_LET KW_MUT VARIABLE COLON data_type EQUALS data
    | KW_LET VARIABLE EQUALS expression_var
    | KW_LET VARIABLE COLON data_type EQUALS expression_var
    | KW_LET KW_MUT VARIABLE EQUALS expression_var
    | KW_LET KW_MUT VARIABLE COLON data_type EQUALS expression_var
    | KW_LET VARIABLE EQUALS casting
    | KW_LET KW_MUT VARIABLE EQUALS casting'''

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
    | VARIABLE DOT DOT VARIABLE
    | LBRACKET mdata RBRACKET'''

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
    | KW_LET KW_MUT VARIABLE EQUALS KW_HASHMAP COLON COLON KW_NEW LPAREN RPAREN'''

# HashMap methods
def p_hashmap_methods(p):
    '''hashmap_methods : VARIABLE hashmap_insert
    | VARIABLE hashmap_remove'''

# HashMap insert
def p_hashmap_insert(p):
    'hashmap_insert : DOT KW_INSERT LPAREN data COMMA data RPAREN SEMI'

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
    'if : KW_IF lvariable LBRACE main_rule RBRACE'

def p_else(p):
    'else : KW_ELSE LBRACE main_rule RBRACE'

def p_else_if(p):
    'else_if : KW_ELSE KW_IF lvariable LBRACE main_rule RBRACE'

## Function with a return value

def p_function_return(p):
    '''function : KW_FN VARIABLE LPAREN arguments RPAREN MINUS GT data_type LBRACE return RBRACE'''

def p_expression_var(p):
    '''expression_var : expression
                      | data'''

def p_return_statement(p):
    '''return : main_rule
              | KW_RETURN expression_var SEMI
              | main_rule KW_RETURN expression_var SEMI'''

## Input of data

def p_input_init(p):
    'input_init : KW_LET VARIABLE EQUALS KW_IO COLON COLON KW_STDIN LPAREN RPAREN'

def p_input(p):
    'input : VARIABLE DOT KW_READ_LINE LPAREN AND KW_MUT VARIABLE RPAREN DOT KW_EXPECT LPAREN CADENA RPAREN SEMI'

## Assignation with operators

def p_assignation(p):
    '''assignation : VARIABLE assign_operators number SEMI
    | VARIABLE assign_operators expression SEMI
    | VARIABLE assign_operators number
    | VARIABLE assign_operators expression'''

## Declaration of variables 

def p_declare_datat_type(p):
    'declare_data_type : KW_LET VARIABLE COLON data_type SEMI'

# Error rule for syntax errors



def p_error(p):
    timenow = datetime.datetime.now()
    if p is not None:
        global yacc_errors
        print ("Syntax error %s token in line %s [DateTime: %s]" % (p.type, p.lineno, str(timenow)))
        yacc_errors.append("Syntax error %s token in line %s [DateTime: %s]" % (p.type, p.lineno, str(timenow)))
        
        filew.write("Syntax error %s token in line %s [DateTime: %s]" % (p.type, p.lineno, str(timenow)))
        
    else:
        print('Unexpected end of input')
        yacc_errors.append('Unexpected end of input')
        filew.write('Unexpected end of input\n')


# Build the parser
parser = yacc.yacc(debug=True)
yacc_errors = []
""" while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result) """




# timenow = datetime.datetime.now()

# files = ["source.txt","source2.txt","source3.txt","source4.txt"]
# for file in files:
#   with open(file) as archivo:
#     linea = archivo.read()
#     result = parser.parse(linea)
#     if error_number != 0:
#       result = error_number
#       error_number = 0
      
#     print("File: %s >> Result: %s errors found. %s" %(file, str(result), str(timenow)))
#     filew.write("DateTime: %s | File: %s >> Result: %s errors found.\n" % (str(timenow), file, str(result)))


def get_yacc():
    return yacc.yacc(errorlog=yacc.NullLogger())


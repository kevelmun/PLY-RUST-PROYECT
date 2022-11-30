import ply.lex as lex
import datetime
## KEVIN ELIHAN MUNOZ
reserved = {
    "const": 'KW_CONST',
    "else": 'KW_ELSE',
    "false": 'KW_FALSE',
    "fn": 'KW_FN',
    "for": 'KW_FOR',
    "if": 'KW_IF',
    "in": 'KW_IN',
    "let": 'KW_LET',
    "mut": 'KW_MUT',
    "return": 'KW_RETURN',
    "true": 'KW_TRUE',
    "while": 'KW_WHILE',
## KEVIN ELIHAN MUNOZ

## LOBERLLY SALAZAR ASPIAZU
    "i8": 'SIG_INT_8',
    "i16": 'SIG_INT_16',
    "i32": 'SIG_INT_32',
    "i64": 'SIG_INT_64',
    "i128": 'SIG_INT_128',

    "u8": 'UNSIG_INT_8',
    "u16": 'UNSIG_INT_16',
    "u32": 'UNSIG_INT_32',
    "u64": 'UNSIG_INT_64',
    "u128": 'UNSIG_INT_128',

    "f32": 'FLOAT_32',
    "f64": 'FLOAT_64',

    "bool": 'KW_BOOLEAN',
    "char": 'KW_CHARACTER',

    "LinkedList": 'KW_LINKEDLIST',
    "new": 'KW_NEW',
    "from": 'KW_FROM',
    "push_back": 'KW_PUSH_BACK',
    "remove": 'KW_REMOVE',
    "String": 'KW_STRING',
    "stdin": 'KW_STDIN',
    "read_line": 'KW_READ_LINE',
    "expect": 'KW_EXPECT',
    "io": 'KW_IO',


    #Daniel Guerrero
    "println": 'KW_PRINT',
    "as": 'KW_AS',

    #KEVIN ELIHAN MUNOZ
    "HashMap": 'KW_HASHMAP',
    "insert": 'KW_INSERT',
}



tokens = ( 
    ## LOBERLLY SALAZAR ASPIAZU
    # Tipos de dato
    'FLOAT',
    'CHAR',
    
    # Símbolos
    'AND',

    # Comentarios
    'COMMENT',

    ## KEVIN ELIHAN MUNOZ
    'VARIABLE',
    # Operadores
    'PLUS', 
    'MINUS', 
    'TIMES', 
    'DIVIDE', 
    'LOR', 
    'LAND', 
    'LNOT',
    'LT', 
    'LE', 
    'GT', 
    'GE', 
    'EQ', 
    'NE',

    # Asignación
    'EQUALS',
    'TIMESEQUAL', 
    'DIVEQUAL', 
    'MODULUSEQUAL', 
    'PLUSEQUAL', 
    'MINUSEQUAL',

    # Delimitadores
    'LPAREN', 
    'RPAREN',        
    'LBRACKET', 
    'RBRACKET',    
    'LBRACE', 
    'RBRACE',         
    'COMMA',                   
    'SEMI', 
    'COLON',            
    ## KEVIN ELIHAN MUNOZ

    ## DANIEL GUERRERO RODRIGUEZ
    # Caracteres
    'QUOTE',
    'DOT',

    # Datos
    'INTEGER',
    'CADENA',
    
)+tuple(reserved.values())




## KEVIN ELIHAN MUNOZ

#EMPRESIONES REGULARES
 # Operadores
t_PLUS              = r'\+'
t_MINUS             = r'-'
t_TIMES             = r'\*'
t_DIVIDE            = r'/'
t_LOR               = r'\|\|'
t_LAND              = r'&&'
t_LNOT              = r'!'
t_LT                = r'<'
t_GT                = r'>'
t_LE                = r'<='
t_GE                = r'>='
t_EQ                = r'=='
t_NE                = r'!='

# Asignacion
t_EQUALS            = r'='
t_TIMESEQUAL        = r'\*='
t_DIVEQUAL          = r'/='
t_MODULUSEQUAL      = r'%='
t_PLUSEQUAL         = r'\+='
t_MINUSEQUAL        = r'-='

# Delimitadores
t_LPAREN            = r'\('
t_RPAREN            = r'\)'
t_LBRACE            = r'\{'
t_RBRACE            = r'\}'
t_LBRACKET          = r'\['
t_RBRACKET          = r'\]'

t_COMMA             = r','
t_SEMI              = r';'
t_COLON             = r':'
## KEVIN ELIHAN MUNOZ

## DANIEL GUERRERO RODRIGUEZ
# Caracteres
t_QUOTE             = r'\''
t_DOT               = r'\.'

## LOBERLLY SALAZAR ASPIAZU
t_AND               = r'\&'


## LOBERLLY SALAZAR ASPIAZU
# FLOTANTE
def t_FLOAT(t):
  r'\-?[\d]+\.[\d]+'
  t.value = float(t.value) 
  return t 

#CHARACTER
def t_CHAR(t):
  r'\'[\w\W]{1}\''
  return t

# COMMENTS
def t_COMMENT(t):
  r'\/\/.+'
  pass

## KEVIN ELIHAN MUNOZ
#VARIABLE
## MEJORABLE
def t_VARIABLE(t):
  r'[a-zA-Z_]+[\w]*'
  t.type = reserved.get(t.value, 'VARIABLE')
  return t

## DANIEL GUERRERO RODRIGUEZ
#ENTERO
def t_INTEGER(t):
  r'(-?[1-9]\d*)|0'
  t.value = int(t.value) 
  return t

def t_CADENA(t):
  r'\"([^\\\n]|(\\.))*?\"'
  return t

#Conteo de lineas
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

#Token de ignorar
t_ignore  = ' \t'



'''def getTokens(lexer):
  for tok in lexer:
    print(tok)


#Lea el archivo source.txt y retorne los tokens
files = ["source.txt", "source2.txt", "source3.txt", ]
for file in files:
  with open(file) as archivo:
    linea = archivo.read()
    lexer.input(linea)
    getTokens(lexer)
  print("#DONE " + file + "\n\n")

print("COMPLETED")'''


def t_error(t):
    global lex_errors

    print(f"Caracter no reconocido {t.value[0]} en la línea {t.lineno}")
    lex_errors.append(f"Caracter no reconocido {t.value[0]} en la línea {t.lineno}")
    #filew = open("log.txt","a", encoding="utf-8")
    #timenow = datetime.datetime.now()
    #filew.write("---------------------------------ANALISIS LEXICO----------------------------------------------\n")
    #filew.write(f"Caracter no reconocido {t.value[0]} en la línea {t.lineno} [DateTime: %s]"% str(timenow))
    t.lexer.skip(1)
  
lex.lex()

# List de errores
lex_errors = []

def getTokens(lexer):
    l = []
    while True:
        tok = lexer.token()
        if not tok:
            break 
        l.append(tok)
    return l

def get_lexer():
    return lex.lex()
## KEVIN ELIHAN MUNOZ
import ply.lex as lex

## KEVIN ELIHAN MUNOZ
reserved = {
    "as": 'KW_AS',
    "break": 'KW_BREAK',
    "const": 'KW_CONST',
    "continue": 'KW_CONTINUE',
    "crate": 'KW_CRATE',
    "else": 'KW_ELSE',
    "enum": 'KW_ENUM',
    "extern": 'KW_EXTERN',
    "false": 'KW_FALSE',
    "fn": 'KW_FN',
    "for": 'KW_FOR',
    "if": 'KW_IF',
    "impl": 'KW_IMPL',
    "in": 'KW_IN',
    "let": 'KW_LET',
    "loop": 'KW_LOOP',
    "match" : 'KW_MATCH',
    "mod" : 'KW_MOD',
    "move" : 'KW_MOVE',
    "mut": 'KW_MUT',
    "pub": 'KW_PUB',
    "ref": 'KW_REF',
    "return": 'KW_RETURN',
    "self": 'KW_SELFVALUE',
    "Self" : 'KW_SELFTYPE',
    "static" : 'KW_STATIC',
    "struct": 'KW_STRUCT',
    "super": 'KW_SUPER',
    "trait" : 'KW_TRAIT',
    "true": 'KW_TRUE',
    "type": 'KW_TYPE',
    "unsafe": 'KW_UNSAFE',
    "use": 'KW_USE',
    "where": 'KW_WHERE',
    "while": 'KW_WHILE',

    "async": 'KW_ASYNC',
    "await": 'KW_AWAIT',
    "dyn": 'KW_DYN',
    "abstract": 'KW_ABSTRACT',
    "become": 'KW_BECOME',
    "box": 'KW_BOX',
    "do": 'KW_DO',
    "final": 'KW_FINAL',
    "macro": 'KW_MACRO',
    "override": 'KW_OVERRIDE',
    "priv": 'KW_PRIV',
    "typeof": 'KW_TYPEOF',
    "unsized": 'KW_UNSIZED',
    "virtual": 'KW_VIRTUAL',
    "yield ": 'KW_YIELD',
    "try": 'KW_TRY',
    "union": 'KW_UNION',
    "'static": 'KW_STATICLIFETIME',
## KEVIN ELIHAN MUNOZ
}



tokens = ( 
    ## KEVIN ELIHAN MUNOZ
    'VARIABLE',
    # Operadores
    'PLUS', 
    'MINUS', 
    'TIMES', 
    'DIVIDE', 
    'MODULUS',
    'LOR', 
    'LAND', 
    'LNOT',
    'LT', 
    'LE', 
    'GT', 
    'GE', 
    'EQ', 
    'NE',

    # Asignacion
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
    
)+tuple(reserved.values())




## KEVIN ELIHAN MUNOZ

#EMPRESIONES REGULARES
 # Operadores
t_PLUS              = r'\+'
t_MINUS             = r'-'
t_TIMES             = r'\*'
t_DIVIDE            = r'/'
t_MODULUS           = r'%'
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








## KEVIN ELIHAN MUNOZ
#VARIABLE
## MEJORABLE
def t_VARIABLE(t):
  r'[a-zA-Z_]+[a-zA-Z\d]*'
  t.type = reserved.get(t.value, 'VARIABLE')
  return t

#Conteo de lineas
def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)
    

#Token de ignorar
t_ignore  = ' \t'


#Token de error
def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
    

#Construccion del lexer
lexer = lex.lex()

def getTokens(lexer):
    for tok in lexer:
        print(tok)


#Lea el archivo source.txt y retorne los tokens
with open("source.txt") as archivo:
    linea = archivo.read()
    lexer.input(linea)
    getTokens(lexer)

print("#DONE")


## KEVIN ELIHAN MUNOZ
import ply

import ply.lex as lex
from datetime import datetime

# List of token names.   This is always required
reserved = {
   'if' : 'IF',
   'then' : 'THEN',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'int': 'INT',
   'double':'DOUBLE',
   'char:': 'CHAR',
   
}
tokens = (
   'LBRACE', 
   'RBRACE',
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'VARIABLE',
   'SEMICOLON',
   'DOT',
   'ARROBA',
   'COMPARE',
   'ID',
   'MOD',          # %
   'EQUAL',        # =
   'NOTEQUAL',     # !=
   'TERNARIO_Q',   # ?
   'TERNARIO_C',   # :
   'STRING'       # "texto"
)+tuple(reserved.values())

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_VARIABLE=r'_[a-z]\w+'
t_COMPARE=r'={2}'
t_SEMICOLON  = r';'
t_DOT        = r'\.'
t_LBRACE     = r'\{'
t_RBRACE     = r'\}'

# Operador módulo %
t_MOD = r'%'

# Operador de asignación =
t_EQUAL = r'='

# Operador diferente !=
t_NOTEQUAL = r'!='

# Operadores del operador ternario ? :
t_TERNARIO_Q = r'\?'
t_TERNARIO_C = r':'

nombre=input("Ingresa el nombre de github. ")
fecha_actual = datetime.now().strftime("%d-%m-%Y")
algoritmo=input("Escribe el nombre del algoritmo")
def leer(nombre_algo):
    with open("./Algoritmos/"+nombre_algo+".cs", "r", encoding="utf-8") as f:
        contenido = f.read()
    return contenido
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t
# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    msg = f"Caracter no registrado: {t.value[0]!r} en linea {t.lexer.lineno}"
    print(msg)
    # Escribe (añade) al archivo de log de errores
    with open("./Logs/"+"lexico-"+nombre+"-"+fecha_actual+".txt", "a+", encoding="utf-8") as f:
        f.write(msg + "\n")
    t.lexer.skip(1)

# Token para strings en C# usando comillas dobles
def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

# Token para comentarios de línea //
def t_COMMENT(t):
    r'//.*'
    pass  # Se ignoran los comentarios


# Build the lexer
lexer = lex.lex()
# Test it out
data=leer(algoritmo)
# Give the lexer some input
lexer.input(data)
# Tokenize(cambios para)
with open("./Logs/"+"lexico-"+nombre+"-"+fecha_actual+".txt", "w+", encoding="utf-8")as out:
    while True:
        tok = lexer.token()
        if not tok:
            break      
        line = f"{tok.type}({tok.value}) en linea {tok.lineno} posicion {tok.lexpos}"
        print(line)
        out.write(line + "\n")

import ply.lex as lex
from datetime import datetime

# ============================
# PALABRAS RESERVADAS
# ============================
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'int': 'INT',
    'double': 'DOUBLE',
    'char': 'CHAR',
    'string': 'STRINGTYPE',
    'Console': 'CONSOLE',
    'using': 'USING',
    'System': 'SYSTEM',
    'class': 'CLASS',
    'Program': 'PROGRAM',
    'static': 'STATIC',
    'void': 'VOID'
}

# ============================
# TOKENS
# ============================
tokens = (
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
    'DOT',
    'EQUAL',
    'NOTEQUAL',
    'COMPARE',
    'MOD',
    'COMMA',
    'ID',
    'STRING_LITERAL',
    'AND',
    'OR'
) + tuple(reserved.values())

# ============================
# REGEX SIMPLES
# ============================
t_PLUS       = r'\+'
t_MINUS      = r'-'
t_TIMES      = r'\*'
t_DIVIDE     = r'/'
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_LBRACE     = r'\{'
t_RBRACE     = r'\}'
t_LBRACKET   = r'\['
t_RBRACKET   = r'\]'
t_SEMICOLON  = r';'
t_DOT        = r'\.'
t_COMMA      = r','
t_MOD        = r'%'
t_COMPARE    = r'=='
t_NOTEQUAL   = r'!='
t_EQUAL      = r'='
t_AND        = r'&&'
t_OR         = r'\|\|'

# ============================
# IDENTIFICADORES
# ============================
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# ============================
# NÚMEROS
# ============================
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# ============================
# STRINGS — normales e interpolados
# ============================
def t_STRING_LITERAL(t):
    r'\$\"([^\"\\]|\\.)*\"|\"([^\"\\]|\\.)*\"'
    return t


# ============================
# COMENTARIOS
# ============================
def t_COMMENT(t):
    r'//.*'
    pass

# ============================
# CONTADOR DE LÍNEAS
# ============================
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# ============================
# IGNORADOS
# ============================
t_ignore = ' \t'

# ============================
# ERRORES
# ============================
def t_error(t):
    msg = f"Caracter no registrado: {t.value[0]!r} en linea {t.lexer.lineno}"
    print(msg)
    with open(f"./Logs/lexico-{t.lexer.nombre_archivo}-{t.lexer.fecha_actual}.txt",
              "a+", encoding="utf-8") as f:
        f.write(msg + "\n")
    t.lexer.skip(1)

# ============================
# CONSTRUIR LEXER
# ============================
lexer = lex.lex()

# ============================
# FUNCIÓN PRINCIPAL
# ============================
def analizador_lexico(data, nombre):
    lexer.input(data)
    lexer.nombre_archivo = nombre
    lexer.fecha_actual = datetime.now().strftime("%d-%m-%Y")

    ruta = f"./Logs/lexico-{nombre}-{lexer.fecha_actual}.txt"
    with open(ruta, "w+", encoding="utf-8") as out:
        while True:
            tok = lexer.token()
            if not tok:
                break
            line = f"{tok.type}({tok.value}) en linea {tok.lineno} posicion {tok.lexpos}"
            print(line)
            out.write(line + "\n")

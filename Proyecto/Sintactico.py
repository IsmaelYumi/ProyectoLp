import ply.yacc as yacc
from Lexico import tokens

# --- Precedencia de Operadores (Fundamental para expresiones) ---
# Se asume que estos tokens existen en Lexico.py (Ej: AND, OR, +, -, *, /, etc.)
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQ', 'NE'),
    ('left', 'LT', 'LE', 'GT', 'GE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('right', 'UMINUS', 'NOT') 
)

# --- Estructura Base del Programa ---

def p_programa(p):
    '''programa : sentencias'''
    p[0] = ('PROGRAMA', p[1])

def p_sentencias(p):
    '''sentencias : sentencia sentencias
                  | sentencia
                  | empty'''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    elif len(p) == 2 and p[1] is not None:
        p[0] = [p[1]]
    else:
        p[0] = []

def p_sentencia(p):
    '''sentencia : estructura_control
                 | asignacion          
                 | declaracion_var  
                 | expresion PUNTO_COMA'''
    p[0] = p[1]

def p_bloque(p):
    '''bloque : LBRACE sentencias RBRACE
              | sentencia''' 
    if len(p) == 4:
        p[0] = ('BLOQUE', p[2])
    else:
        p[0] = ('BLOQUE', [p[1]])

def p_empty(p):
    'empty :'
    pass



def p_expresion(p):
    '''expresion : expresion PLUS expresion
                 | expresion MINUS expresion
                 | LPAREN expresion RPAREN
                 | LITERAL_INT
                 | LITERAL_FLOAT
                 | ID'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    elif len(p) == 2:
        p[0] = p[1]

def p_condicion(p):
    '''condicion : expresion relacional expresion
                 | T_TRUE
                 | T_FALSE'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_relacional(p):
    '''relacional : EQ
                  | NE
                  | LT
                  | LE
                  | GT
                  | GE'''
    p[0] = p[1]

def p_tipo(p):
    '''tipo : T_INT 
            | T_FLOAT  
            | T_STRING 
            | T_BOOL 
            | ID''' 
    p[0] = p[1]

def p_declaracion_var(p):
    '''declaracion_var : tipo ID PUNTO_COMA'''
    p[0] = ('DECLARACION', p[1], p[2])

def p_asignacion(p):
    '''asignacion : ID ASSIGN expresion PUNTO_COMA'''
    p[0] = ('ASIGNACION', p[1], p[3])

def p_estructura_control(p):
    '''estructura_control : while_statement
                          | if_statement
                          | for_statement'''
    p[0] = p[1]

def p_while_statement(p):
    '''while_statement : T_WHILE LPAREN condicion RPAREN bloque'''
    
    p[0] = ('WHILE', p[3], p[5])


def p_if_statement(p):
    '''if_statement : T_IF LPAREN condicion RPAREN bloque
                    | T_IF LPAREN condicion RPAREN bloque T_ELSE bloque'''
    if len(p) == 6:
        p[0] = ('IF', p[3], p[5])
    else:
        p[0] = ('IF_ELSE', p[3], p[5], p[7])

def p_for_statement(p):
    '''for_statement : T_FOR LPAREN for_inicializacion PUNTO_COMA condicion PUNTO_COMA for_incremento RPAREN bloque'''
    p[0] = ('FOR', p[3], p[5], p[7], p[9])

def p_for_inicializacion(p):
    '''for_inicializacion : declaracion_var
                          | asignacion_simple
                          | empty'''
    p[0] = p[1]

def p_for_incremento(p):
    '''for_incremento : asignacion_simple
                      | ID PLUS PLUS     
                      | ID MINUS MINUS   
                      | empty'''
    p[0] = p[1]

def p_asignacion_simple(p):
    '''asignacion_simple : ID ASSIGN expresion''' 
    p[0] = ('ASIGNACION', p[1], p[3])



def p_estructura_datos(p):
    '''estructura_datos : array_declaration''' 
    p[0] = p[1]


def p_array_declaration(p):
    '''array_declaration : T_NEW tipo LBRACKET LITERAL_INT RBRACKET        
                         | T_NEW tipo LBRACKET RBRACKET LBRACE expresion_lista RBRACE'''
    if len(p) == 6:
        p[0] = ('ARRAY_INIT_SIZE', p[2], p[4])
    else:
        p[0] = ('ARRAY_INIT_LIST', p[2], p[6])

def p_expresion_lista(p):
    '''expresion_lista : expresion
                       | expresion_lista COMMA expresion'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_error(p):
    print("Syntax error in input!")
    

parser = yacc.yacc()
while True:
   try:
      s = input('csharp > ')
   except EOFError:
      break
   if not s: continue
   result = parser.parse(s)
   print(result)
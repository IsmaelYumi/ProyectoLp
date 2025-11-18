import ply.yacc as yacc
from Lexico import tokens, lexer

tabla = {}
builtins = {"Console", "Convert", "Program", "System"}

start = "program"

def log_error(msg):
    with open(f"./Logs/Semantico-{lexer.nombre_archivo}-{lexer.fecha_actual}.txt",
              "a+", encoding="utf-8") as f:
        f.write(msg + "\n")

# =====================
# MISMAS REGLAS QUE EL SINTÁCTICO
# =====================
def p_program(p):
    """program : using_list class_section"""
    pass

def p_using_list(p):
    """using_list : using_list using_section
                  | using_section
                  | empty"""
    pass

def p_using_section(p):
    """using_section : USING SYSTEM SEMICOLON"""
    pass

def p_class_section(p):
    """class_section : CLASS ID LBRACE class_body RBRACE"""
    pass

def p_class_body(p):
    """class_body : class_body class_member
                  | class_member
                  | empty"""
    pass

def p_class_member(p):
    """class_member : property
                    | method"""
    pass

def p_property(p):
    """property : type ID SEMICOLON"""
    nombre = p[2]
    tipo = p[1]

    if nombre in tabla:
        log_error(f"Variable redeclarada: {nombre}")
    else:
        tabla[nombre] = tipo

def p_type(p):
    """type : INT
            | DOUBLE
            | CHAR
            | STRINGTYPE
            | VOID"""
    p[0] = p[1]

def p_method(p):
    """method : STATIC VOID ID LPAREN RPAREN LBRACE statements RBRACE
              | STATIC VOID ID LPAREN parameter_list RPAREN LBRACE statements RBRACE"""
    pass

def p_parameter_list(p):
    """parameter_list : param
                      | parameter_list COMMA param"""
    pass

def p_param(p):
    """param : type ID
             | STRINGTYPE LBRACKET RBRACKET ID"""
    pass


def p_statements(p):
    """statements : statements statement
                  | statement
                  | empty"""
    pass

def p_statement(p):
    """statement : declaration SEMICOLON
                 | assignment SEMICOLON
                 | method_call SEMICOLON
                 | expression SEMICOLON
                 | if_statement
                 | while_statement"""
    pass

def p_declaration(p):
    """declaration : type ID EQUAL expression"""
    nombre = p[2]
    tipo = p[1]

    if nombre in tabla:
        log_error(f"Variable redeclarada: {nombre}")
    else:
        tabla[nombre] = tipo

def p_assignment(p):
    """assignment : ID EQUAL expression"""
    nombre = p[1]

    if nombre not in tabla and nombre not in builtins:
        log_error(f"Variable usada sin declarar: {nombre}")

def p_if_statement(p):
    """if_statement : IF LPAREN expression RPAREN LBRACE statements RBRACE
                    | IF LPAREN expression RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE"""
    pass

def p_while_statement(p):
    """while_statement : WHILE LPAREN expression RPAREN LBRACE statements RBRACE"""
    pass

def p_method_call(p):
    """method_call : ID LPAREN args RPAREN
                   | ID DOT ID LPAREN args RPAREN
                   | CONSOLE DOT ID LPAREN args RPAREN"""
    pass

def p_args(p):
    """args : expression
            | args COMMA expression
            | empty"""
    pass

def p_expression_value(p):
    """expression : ID
                  | NUMBER
                  | STRING_LITERAL"""
    if p.slice[1].type == "ID":
        nombre = p[1]
        if nombre not in tabla and nombre not in builtins:
            log_error(f"Variable usada sin declarar: {nombre}")

def p_expression_method_call(p):
    """expression : method_call"""
    pass


def p_expression_group(p):
    """expression : LPAREN expression RPAREN"""
    pass

def p_expression_binop(p):
    """expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression MOD expression"""
    pass

def p_expression_compare(p):
    """expression : expression COMPARE expression
                  | expression NOTEQUAL expression"""
    pass

def p_expression_logic(p):
    """expression : expression AND expression
                  | expression OR expression"""
    pass

def p_expression_dot(p):
    """expression : expression DOT ID"""
    pass

def p_empty(p):
    """empty :"""
    pass

def p_error(p):
    log_error(f"Error semántico cerca de: {p.value if p else 'EOF'}")

parser = yacc.yacc(write_tables=False)

def analizador_semantico(data):
    return parser.parse(data, lexer=lexer)

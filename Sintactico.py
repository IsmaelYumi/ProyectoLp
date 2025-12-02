import ply.yacc as yacc
from Lexico import tokens, lexer
import os

start = "program"
log_sematico=[]
#Funcion para logs
def log(level, message):
    os.makedirs("./Logs", exist_ok=True)
    ruta = f"./Logs/Sintactico-{lexer.nombre_archivo}-{lexer.fecha_actual}.txt"
    linea= f" [{level}] {message}"
    with open(ruta, "a+", encoding="utf-8") as f:
        f.write(linea + "\n")
    log_sematico.append(linea)

# ===========================
# PROGRAMA
# ===========================
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

# ===========================
# CLASE
# ===========================
def p_class_section(p):
    """class_section : CLASS ID LBRACE class_body RBRACE 
                     | CLASS PROGRAM LBRACE class_body RBRACE """

    log("OK","Expresion verificada , nombre de clase correcto:"f"{p[1]},")
    pass

def p_class_body(p):
    """class_body : class_body class_member
                  | class_member
                  | empty"""
    pass

def p_class_member(p):
    """class_member : method
                    | property"""
    pass

# ===========================
# PROPIEDADES
# ===========================
def p_property(p):
    """property : type ID SEMICOLON"""
    log("OK","Expresion verificada , propiedad declarada correctamente:"f"{p[1]}")
    pass

# ===========================
# TIPOS
# ===========================
def p_type(p):
    """type : INT
            | DOUBLE
            | CHAR
            | STRINGTYPE
            | VOID
            | INT LBRACKET RBRACKET
            | STRINGTYPE LBRACKET RBRACKET
            | CHAR LBRACKET RBRACKET
            | DOUBLE LBRACKET RBRACKET
            | LIST LT INT GT
            | LIST LT DOUBLE GT
            | LIST LT CHAR GT
            | LIST LT STRINGTYPE GT"""
    
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = f"{p[1]}[]"
    else:
        p[0] = f"List<{p[3]}>"




# ===========================
# MÉTODOS
# ===========================
def p_method(p):
    """
    method : STATIC VOID ID LPAREN RPAREN LBRACE statements RBRACE
           | STATIC VOID ID LPAREN parameter_list RPAREN LBRACE statements RBRACE
    """
    log("OK","Expresion verificada , metodo delcarado correctamente:"f"{p[3]}")
    pass

# ===========================
# PARÁMETROS
# ===========================
def p_parameter_list(p):
    """parameter_list : param
                      | parameter_list COMMA param"""
    pass

def p_param(p):
    """param : type ID"""
    log("OK","Expresion verificada , parametro declarado correctamente:"f"{p[3]}")
    pass

# ===========================
# STATEMENTS
# ===========================
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
    log("OK","Expresion verificada , declaracion  correcta"f"{p[1]}")
    pass

 
# ===========================
# DECLARACIÓN / ASIGNACIÓN
# ===========================
def p_declaration(p):
    """declaration : type ID EQUAL expression"""
    log("OK","Expresion verificada , declaracion  correcta"f"{p[3]}")
    pass

def p_assignment(p):
    """assignment : ID EQUAL expression"""
    pass

# ===========================
# IF / WHILE
# ===========================
def p_if_statement(p):
    """if_statement : IF LPAREN expression RPAREN LBRACE statements RBRACE
                    | IF LPAREN expression RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE"""
    log("OK","Expresion verificada , declaracion  correcta"f"{p[0]}{p[1]}{p[2]}")
    pass

def p_while_statement(p):
    """while_statement : WHILE LPAREN expression RPAREN LBRACE statements RBRACE"""
    pass

# ===========================
# CALLS
# ===========================
def p_method_call(p):
    """method_call : ID LPAREN args RPAREN
                   | ID DOT ID LPAREN args RPAREN
                   | CONSOLE DOT ID LPAREN args RPAREN"""
    pass

def p_expression_method_call(p):
    "expression : method_call"
    pass


def p_args(p):
    """args : expression
            | args COMMA expression
            | empty"""
    pass

# ===========================
# EXPRESIONES
# ===========================
def p_expression_group(p):
    """expression : LPAREN expression RPAREN"""
    p[0] = p[2]

def p_expression_value(p):
    """expression : ID
                  | NUMBER
                  | STRING_LITERAL"""
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

# ===========================
# EMPTY
# ===========================
def p_empty(p):
    """empty :"""
    pass
# ===========================
# SWITCH-CASE
# ===========================
def p_switch_statement(p):
    """switch_statement : SWITCH LPAREN expression RPAREN LBRACE case_list RBRACE
                        | SWITCH LPAREN expression RPAREN LBRACE case_list default_case RBRACE"""
    log("OK", f"Switch statement verificado correctamente")
    pass

def p_case_list(p):
    """case_list : case_list case_clause
                 | case_clause"""
    pass

def p_case_clause(p):
    """case_clause : CASE expression COLON statements BREAK SEMICOLON
                   | CASE expression COLON statements"""
    log("OK", f"Case clause verificado: {p[2]}")
    pass

def p_default_case(p):
    """default_case : DEFAULT COLON statements
                    | DEFAULT COLON statements BREAK SEMICOLON"""
    log("OK", "Default case verificado correctamente")
    pass


# ===========================
# ERROR
# ===========================
def p_error(p):
    mensaje = f"[ERROR] Syntax error cerca de: {p.value if p else 'EOF'}"

    # Guardar en archivo
    with open(f"./Logs/Sintactico-{lexer.nombre_archivo}-{lexer.fecha_actual}.txt",
              "a+", encoding="utf-8") as f:
        f.write(mensaje + "\n")

    # 🔥 MOSTRAR TAMBIÉN EN LA GUI
    log_sematico.append(mensaje)

parser = yacc.yacc(write_tables=False)
def analizador_sintactico(data):
    global log_sematico
    log_sematico.clear()   # 🔥 LIMPIAR LOGS PREVIOS

    parser.parse(data, lexer=lexer)
    return log_sematico

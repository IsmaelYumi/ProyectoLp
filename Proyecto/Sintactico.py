import ply.yacc as yacc
from Lexico import tokens
from Lexico import lexer

def p_program(p):
    "program : Inicio statements"

def p_statements(p):
    '''statements : statement
                  | statements statement'''

def p_statement_assign(p):
    "statement : ID EQUAL valor"

def p_statement_if(p):
    '''statement : IF LPAREN expression RPAREN statement
                 | IF LPAREN expression RPAREN statement ELSE statement'''
def p_expression(p):
    '''expression : VARIABLE COMPARE VARIABLE
                    | VARIABLE COMPARE  valor '''
def p_valor(p):
    '''valor : NUMBER
             | STRING'''
    p.value = p[1]

def p_Inicio(p):
    "Inicio : USING SYSTEM COMA"

def p_error(p):
    if p:
        msg = f"Syntax error: {p.value}"
    else:
        msg = "Unexpected EOF"
    with open("./Logs/"+"Semantico-"+lexer.nombre_archivo+"-"+lexer.fecha_actual+".txt", "a+", encoding="utf-8") as f:
        f.write(msg + "\n")

parser = yacc.yacc(write_tables=False, debug=True)

def analisador_sintactico(data):
   return parser.parse(data, lexer=lexer)

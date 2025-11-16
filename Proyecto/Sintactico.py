import ply.yacc as yacc
from Lexico import tokens
from Lexico import lexer
#Seccion para crear las reglas que se necesite
def p_program(p):
    '''program : Inicio statement
               | Inicio program statement'''
    pass
def p_asginacion(p):
   '''statement : VARIABLE EQUAL STRING'''
   pass
def p_IncioPrograma(p):
    '''Inicio : USING SYSTEM COMA'''
    pass
def p_error(p):
    print("Syntax error in input!: "+str(p.value))
    msg=f"caracte fuera de orden semantico: {p.value}"
    with open("./Logs/"+"lexico-"+lexer.nombre_archivo+"-"+lexer.fecha_actual+".txt", "a+", encoding="utf-8") as f:
        f.write(msg + "\n")

parser = yacc.yacc(write_tables=False)

def analisador_sintactico(data):
   result = parser.parse(data, lexer=lexer)
   return str(result)
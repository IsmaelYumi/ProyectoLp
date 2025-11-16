import ply.yacc as yacc
from Lexico import tokens
#Seccion para crear las reglas que se necesite
def p_error(p):
    print("Syntax error in input!")

# Csontruccion del yacc
parser = yacc.yacc()
#Codigo de prueba (Borrar luego)
while True:
   try:
       s = input('csharp > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)

   # ============================================================
#   --- REGLAS APORTADAS POR ANDRÉS ---
# ============================================================

# 1. ESTRUCTURA DE CONTROL → WHILE
def p_while(p):
    '''while : WHILE LPAREN expression RPAREN LBRACE statements RBRACE'''
    p[0] = ("while", p[3], p[6])

# 2. ESTRUCTURA DE DATOS → LISTA SIMPLE C#
def p_list_def(p):
    '''expression : ID LBRACE expression RBRACE'''
    # Ej: lista { 1 }
    p[0] = ("list", p[1], p[3])

# 3. FUNCIÓN CON PARÁMETROS
def p_function(p):
    '''function : ID ID LPAREN ID RPAREN LBRACE statements RBRACE'''
    # Ej: bool EsPalindromo(cadena) { ... }
    p[0] = ("function", p[2], p[4], p[7])
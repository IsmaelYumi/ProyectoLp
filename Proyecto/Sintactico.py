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
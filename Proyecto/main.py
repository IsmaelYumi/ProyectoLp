from Lexico import analizador_lexico, lexer
from Sintactico import analizador_sintactico
from Semantico import analizador_semantico
from datetime import datetime
import os

def leer_archivo(nombre_algo):
    with open("./Algoritmos/" + nombre_algo + ".cs", "r", encoding="utf-8") as f:
        return f.read()

def limpiar_log_especifico(nombre, fecha, tipo):
    ruta = f"./Logs/{tipo}-{nombre}-{fecha}.txt"
    open(ruta, "w+", encoding="utf-8").close()

def main():
    print("=== Analizador Léxico / Sintáctico / Semántico ===")
    
    nombreGithub = input("Ingrese su nombre de GitHub: ")
    archivo = input("Ingrese el nombre del archivo en /Algoritmos (sin .cs): ")

    codigo = leer_archivo(archivo)

    fecha_actual = datetime.now().strftime("%d-%m-%Y")
    lexer.nombre_archivo = nombreGithub
    lexer.fecha_actual = fecha_actual

    print("""
Seleccione el análisis que desea ejecutar:
1) Análisis Léxico
2) Análisis Sintáctico
3) Análisis Semántico
""")

    opcion = input("Ingrese opción (1/2/3): ")

    # ======================
    # ANÁLISIS LÉXICO
    # ======================
    if opcion == "1":
        limpiar_log_especifico(nombreGithub, fecha_actual, "lexico")
        analizador_lexico(codigo, nombreGithub)
        print("Log léxico generado.")

    # ======================
    # ANÁLISIS SINTÁCTICO
    # ======================
    elif opcion == "2":
        limpiar_log_especifico(nombreGithub, fecha_actual, "Sintactico")
        analizador_sintactico(codigo)
        print("Log sintáctico generado.")

    # ======================
    # ANÁLISIS SEMÁNTICO
    # ======================
    elif opcion == "3":
        limpiar_log_especifico(nombreGithub, fecha_actual, "Semantico")
        analizador_semantico(codigo)
        print("Log semántico generado.")

    else:
        print("Opción inválida.")

if __name__ == "__main__":
    main()

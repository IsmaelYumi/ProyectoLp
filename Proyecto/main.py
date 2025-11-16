from Sintactico import analisador_sintactico
from Lexico import analizador_lexico
def leer(nombre_algo):
    with open("./Algoritmos/"+nombre_algo+".cs", "r", encoding="utf-8") as f:
        contenido = f.read()
    return contenido
def main():
    nombreGithub=input("Ingrese su nombre: ")
    NombreAlgoritmo=input("Ingrese el nombre del algoritmo en la carpeta de algoritmo: ")
    Algoritmo=leer(NombreAlgoritmo)
    analizador_lexico(Algoritmo,nombreGithub)
    print("Creacion de log lexico")
    resultado= analisador_sintactico(Algoritmo)
    print(resultado)
    print("Creacion de log ")
if __name__ == "__main__":
    main()
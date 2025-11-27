from Lexico import analizador_lexico
from Sintactico import analizador_sintactico
from Semantico import analizador_semantico

class AnalizadorController:

    def __init__(self):
        self.codigo = ""

    def cargar_codigo(self, contenido):
        self.codigo = contenido

    def ejecutar_lexico(self, usuario):
        return analizador_lexico(self.codigo, usuario)

    def ejecutar_sintactico(self, usuario):
        return analizador_sintactico(self.codigo)

    def ejecutar_semantico(self, usuario):
        return analizador_semantico(self.codigo)

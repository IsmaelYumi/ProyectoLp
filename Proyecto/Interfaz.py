import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from datetime import datetime
import os

from Lexico import analizador_lexico, lexer
from Sintactico import analizador_sintactico
from Semantico import analizador_semantico

# ======================================================
#     INTERFAZ GRÁFICA COMPLETA PARA LOS 3 ANALIZADORES
# ======================================================
class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Analizador Léxico - Sintáctico - Semántico")
        self.geometry("1000x650")

        self.archivo_actual = None

        self.crear_widgets()
    def mostrar_log(self, ruta):
        if os.path.exists(ruta):
            with open(ruta, "r", encoding="utf-8") as f:
                contenido = f.read()

            self.log("\n===== CONTENIDO DEL LOG =====")
            self.log(contenido)
            self.log("===== FIN DEL LOG =====\n")
        else:
            self.log(f"No existe el log: {ruta}")


    # --------------------------------------------------
    def crear_widgets(self):

        # ---------- BOTONES SUPERIORES ----------
        frame = tk.Frame(self)
        frame.pack(fill="x", pady=5)

        tk.Button(frame, text="Abrir archivo .cs", command=self.cargar_archivo).pack(side="left", padx=5)
        
        tk.Button(frame, text="Ejecutar Léxico", command=self.run_lexico).pack(side="left", padx=5)
        tk.Button(frame, text="Ejecutar Sintáctico", command=self.run_sintactico).pack(side="left", padx=5)
        tk.Button(frame, text="Ejecutar Semántico", command=self.run_semantico).pack(side="left", padx=5)

        # Nombre de GitHub requerido por tus logs
        tk.Label(frame, text="GitHub:").pack(side="left", padx=5)
        self.entrada_github = tk.Entry(frame, width=20)
        self.entrada_github.pack(side="left")

        # ---------- ÁREA DE CÓDIGO ----------
        tk.Label(self, text="Código fuente:").pack(anchor="w", padx=10)
        self.txt_codigo = scrolledtext.ScrolledText(self, height=20)
        self.txt_codigo.pack(fill="both", expand=True, padx=10, pady=5)

        # ---------- OUTPUT DE RESULTADOS ----------
        tk.Label(self, text="Salida / Errores:").pack(anchor="w", padx=10)
        self.txt_salida = scrolledtext.ScrolledText(self, height=12, state="normal", bg="#111", fg="#0f0")
        self.txt_salida.pack(fill="both", expand=True, padx=10, pady=5)

    # --------------------------------------------------
    def cargar_archivo(self):
        ruta = filedialog.askopenfilename(filetypes=[("Archivos C#", "*.cs"), ("Todos", "*.*")])
        if not ruta:
            return
        
        self.archivo_actual = os.path.basename(ruta).replace(".cs", "")

        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()

        self.txt_codigo.delete("1.0", tk.END)
        self.txt_codigo.insert("1.0", contenido)

        self.log(f"Archivo cargado: {ruta}")

    # --------------------------------------------------
    def log(self, mensaje):
        self.txt_salida.config(state="normal")
        self.txt_salida.insert(tk.END, mensaje + "\n")
        self.txt_salida.see(tk.END)
        self.txt_salida.config(state="disabled")

    # --------------------------------------------------
    def preparar_logs(self):
        nombre = self.entrada_github.get().strip()
        if not nombre:
            messagebox.showerror("Error", "Debe ingresar su usuario de GitHub antes de ejecutar el análisis.")
            return None

        fecha = datetime.now().strftime("%d-%m-%Y")
        lexer.nombre_archivo = nombre
        lexer.fecha_actual = fecha

        return nombre, fecha

    # --------------------------------------------------
    def run_lexico(self):
        datos = self.txt_codigo.get("1.0", tk.END)
        if not datos.strip():
            messagebox.showerror("Error", "No hay código para analizar.")
            return
        
        datos_logs = self.preparar_logs()
        if not datos_logs:
            return
        nombre, fecha = datos_logs

        ruta_log = f"./Logs/lexico-{nombre}-{fecha}.txt"
        open(ruta_log, "w", encoding="utf-8").close()

        self.log("=== EJECUTANDO ANÁLISIS LÉXICO ===")

        analizador_lexico(datos, nombre)

        self.log(f"Log generado: {ruta_log}")
        # ⬇️ MOSTRAR LOG EN CONSOLA
        self.mostrar_log(ruta_log)

    # --------------------------------------------------
    def run_sintactico(self):
        datos = self.txt_codigo.get("1.0", tk.END)
        if not datos.strip():
            messagebox.showerror("Error", "No hay código para analizar.")
            return
        
        datos_logs = self.preparar_logs()
        if not datos_logs:
            return
        nombre, fecha = datos_logs

        ruta_log = f"./Logs/Sintactico-{nombre}-{fecha}.txt"
        open(ruta_log, "w", encoding="utf-8").close()

        self.log("=== EJECUTANDO ANÁLISIS SINTÁCTICO ===")

        try:
            analizador_sintactico(datos)
            self.log("Sintaxis correcta.")
        except Exception as e:
            self.log(str(e))

        self.log(f"Log generado: {ruta_log}")
        # ⬇️ MOSTRAR LOG EN CONSOLA
        self.mostrar_log(ruta_log)

    # --------------------------------------------------
    def run_semantico(self):
        datos = self.txt_codigo.get("1.0", tk.END)
        if not datos.strip():
            messagebox.showerror("Error", "No hay código para analizar.")
            return
        
        datos_logs = self.preparar_logs()
        if not datos_logs:
            return
        nombre, fecha = datos_logs

        ruta_log = f"./Logs/Semantico-{nombre}-{fecha}.txt"
        open(ruta_log, "w", encoding="utf-8").close()

        self.log("=== EJECUTANDO ANÁLISIS SEMÁNTICO ===")

        try:
            analizador_semantico(datos)
            self.log("Semántica correcta.")
        except Exception as e:
            self.log(str(e))

        self.log(f"Log generado: {ruta_log}")
        # ⬇️ MOSTRAR LOG EN CONSOLA
        self.mostrar_log(ruta_log)

# ======================================================
if __name__ == "__main__":
    App().mainloop()

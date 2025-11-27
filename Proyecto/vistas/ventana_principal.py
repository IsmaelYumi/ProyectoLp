import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from controladores.controller import AnalizadorController
import os

class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Analizador C# – Léxico, Sintáctico y Semántico")
        self.geometry("1200x750")
        self.minsize(1100, 700)

        self.controller = AnalizadorController()

        # Estilos visuales
        self._configurar_estilos()

        # Layout
        self._crear_componentes()

    # ===============================================
    # ============= ESTILOS MODERNOS =================
    # ===============================================
    def _configurar_estilos(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TFrame", background="#1E1E1E")
        style.configure("TLabel", background="#1E1E1E", foreground="white")
        style.configure("TButton", padding=6, font=("Segoe UI", 10))
        style.configure("Success.TButton", background="#00A36C", foreground="white")
        style.configure("Warning.TButton", background="#D93636", foreground="white")

        style.configure("TNotebook", background="#252526", borderwidth=0)
        style.configure("TNotebook.Tab", background="#333333", foreground="white", padding=[10, 5])
        style.map("TNotebook.Tab", background=[("selected", "#007ACC")])

    # ===============================================
    # ============= CREACIÓN DE WIDGETS =============
    # ===============================================
    def _crear_componentes(self):
        contenedor = ttk.Frame(self)
        contenedor.pack(fill="both", expand=True, padx=10, pady=10)

        # Panel principal dividido en 2
        panel = ttk.Frame(contenedor)
        panel.pack(fill="both", expand=True)

        self._crear_editor(panel)
        self._crear_panel_resultados(panel)
        self._crear_botones(contenedor)
        self._crear_barra_estado()

    # ===============================================
    # =================== EDITOR =====================
    # ===============================================
    def _crear_editor(self, parent):

        frame_editor = ttk.Frame(parent)
        frame_editor.pack(side="left", fill="both", expand=True, padx=(0, 10))

        lbl = ttk.Label(frame_editor, text="Editor de Código C#")
        lbl.pack(anchor="w", pady=5)

        self.editor = tk.Text(
            frame_editor,
            font=("Consolas", 12),
            bg="#1E1E1E",
            fg="white",
            insertbackground="white",
            undo=True
        )
        self.editor.pack(fill="both", expand=True)

        self.editor.bind("<KeyRelease>", self._actualizar_contadores)

    # ===============================================
    # ============= PANEL RESULTADOS =================
    # ===============================================
    def _crear_panel_resultados(self, parent):
        frame_result = ttk.Frame(parent)
        frame_result.pack(side="right", fill="both", expand=True)

        lbl = ttk.Label(frame_result, text="Resultados del Análisis")
        lbl.pack(anchor="w", pady=5)

        self.notebook = ttk.Notebook(frame_result)
        self.notebook.pack(fill="both", expand=True)

        self.tab_lexico = tk.Text(frame_result, bg="#252526", fg="white", font=("Consolas", 11))
        self.tab_sintactico = tk.Text(frame_result, bg="#252526", fg="white", font=("Consolas", 11))
        self.tab_semantico = tk.Text(frame_result, bg="#252526", fg="white", font=("Consolas", 11))

        self.notebook.add(self.tab_lexico, text="Léxico")
        self.notebook.add(self.tab_sintactico, text="Sintáctico")
        self.notebook.add(self.tab_semantico, text="Semántico")

    # ===============================================
    # ================= BOTONES ======================
    # ===============================================
    def _crear_botones(self, parent):
        frame_botones = ttk.Frame(parent)
        frame_botones.pack(fill="x", pady=(10, 0))

        # Botones grandes del análisis
        btn_lex = ttk.Button(frame_botones, text="Análisis Léxico", style="Success.TButton",
                             command=self.ejecutar_lexico)
        btn_sin = ttk.Button(frame_botones, text="Análisis Sintáctico", command=self.ejecutar_sintactico)
        btn_sem = ttk.Button(frame_botones, text="Análisis Semántico", command=self.ejecutar_semantico)

        btn_lex.pack(side="left", padx=5)
        btn_sin.pack(side="left", padx=5)
        btn_sem.pack(side="left", padx=5)

        # Cargar algoritmo prueba
        btn_algoritmo = ttk.Button(frame_botones, text="Cargar Algoritmo de Prueba",
                                   command=self.cargar_algoritmo_prueba)
        btn_algoritmo.pack(side="right", padx=5)

    # ===============================================
    # ============= BARRA DE ESTADO =================
    # ===============================================
    def _crear_barra_estado(self):
        self.estado = ttk.Label(self, text="Listo.", anchor="w")
        self.estado.pack(fill="x", side="bottom")

    # ===============================================
    # =================== FUNCIONES ==================
    # ===============================================
    def ejecutar_lexico(self):
        codigo = self.editor.get("1.0", "end")
        self.controller.cargar_codigo(codigo)

        resultado = self.controller.ejecutar_lexico("codigo")

        self.tab_lexico.delete("1.0", "end")

        if resultado:
            self.tab_lexico.insert("end", "TOKEN\tVALOR\tLINEA\n")
            self.tab_lexico.insert("end", "-"*50 + "\n")

            for ttype, val, line in resultado:
                self.tab_lexico.insert("end", f"{ttype}\t{val}\t{line}\n")
        else:
            self.tab_lexico.insert("end", "No se encontraron tokens.")

        self.estado.config(text="Análisis léxico completado.")


    def ejecutar_sintactico(self):
        codigo = self.editor.get("1.0", "end")
        self.controller.cargar_codigo(codigo)

        resultado = self.controller.ejecutar_sintactico("codigo")

        self.tab_sintactico.delete("1.0", "end")

        for linea in resultado:
            self.tab_sintactico.insert("end", linea + "\n")

        self.estado.config(text="Análisis sintáctico completado.")


    def ejecutar_semantico(self):
        codigo = self.editor.get("1.0", "end")
        self.controller.cargar_codigo(codigo)

        resultado = self.controller.ejecutar_semantico("codigo")

        self.tab_semantico.delete("1.0", "end")

        for linea in resultado:
            self.tab_semantico.insert("end", linea + "\n")

        self.estado.config(text="Análisis semántico completado.")


    # ===============================================
    # =========== CARGAR ALGORITMO PRUEBA ============
    # ===============================================
    def cargar_algoritmo_prueba(self):
        ruta = filedialog.askopenfilename(
            initialdir="../Algoritmos/",
            filetypes=[("C# Files", "*.cs")]
        )

        if not ruta:
            return

        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()

        self.editor.delete("1.0", "end")
        self.editor.insert("1.0", contenido)

        self.estado.config(text=f"Algoritmo cargado: {os.path.basename(ruta)}")

    # ===============================================
    # ============ CONTADORES =========================
    # ===============================================
    def _actualizar_contadores(self, event=None):
        texto = self.editor.get("1.0", "end")
        lineas = int(self.editor.index("end").split(".")[0]) - 1
        chars = len(texto)

        self.estado.config(text=f"{lineas} líneas | {chars} caracteres")

# =====================================================
# =============== EJECUTAR PROGRAMA ===================
# =====================================================

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()

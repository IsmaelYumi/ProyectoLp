# 🧩 Analizador Léxico, Sintáctico y Semántico para C#

## 📋 Descripción

Este proyecto es un analizador completo para un subconjunto del lenguaje C#. Implementa tres fases de análisis:

- **Análisis Léxico**: Reconoce tokens del código fuente
- **Análisis Sintáctico**: Valida la estructura gramatical
- **Análisis Semántico**: Verifica reglas semánticas (tipos, declaraciones, etc.)

El proyecto incluye una interfaz gráfica moderna desarrollada con Tkinter que permite escribir código C# y ejecutar los tres tipos de análisis de forma independiente.

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**
- **PLY (Python Lex-Yacc)**: Para análisis léxico y sintáctico
- **Tkinter**: Para la interfaz gráfica
- **Patrón MVC**: Arquitectura del proyecto

## 📁 Estructura del Proyecto

```
ProyectoLp/
├── Lexico.py                    # Analizador léxico
├── Sintactico.py                # Analizador sintáctico
├── Semantico.py                 # Analizador semántico
├── vistas/
│   └── ventana_principal.py     # Interfaz gráfica principal
├── controladores/
│   ├── __init__.py
│   └── controller.py            # Controlador MVC
├── Algoritmos/                  # Archivos .cs de prueba
│   └── ejemplo.cs
├── Logs/                        # Archivos de log generados
│   ├── lexico-*.txt
│   ├── Sintactico-*.txt
│   └── Semantico-*.txt
└── README.md
```

## 🚀 Instalación

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/ProyectoLp.git
cd ProyectoLp
```

2. **Crear entorno virtual (opcional pero recomendado)**
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install ply
```

## ▶️ Ejecución

### Opción 1: Ejecutar la Interfaz Gráfica

Desde la raíz del proyecto:

```bash
python vistas/ventana_principal.py
```

### Opción 2: Ejecutar Analizadores Individualmente

**Análisis Léxico:**
```python
from Lexico import analizador_lexico

codigo = '''
class Program {
    static void Main() {
        int x = 5;
    }
}
'''

tokens = analizador_lexico(codigo, "test")
```

**Análisis Sintáctico:**
```python
from Sintactico import analizador_sintactico

resultado = analizador_sintactico(codigo, "test")
```

**Análisis Semántico:**
```python
from Semantico import analizador_semantico

resultado = analizador_semantico(codigo)
```

## 📖 Uso de la Interfaz Gráfica

1. **Escribir código**: Escribe o pega tu código C# en el editor de la izquierda
2. **Cargar algoritmo**: Usa el botón "Cargar Algoritmo de Prueba" para abrir un archivo `.cs`
3. **Ejecutar análisis**:
   - Clic en "Análisis Léxico" para ver los tokens
   - Clic en "Análisis Sintáctico" para validar la gramática
   - Clic en "Análisis Semántico" para verificar reglas semánticas
4. **Ver resultados**: Los resultados aparecen en las pestañas de la derecha
5. **Revisar logs**: Los archivos de log se generan en la carpeta `Logs/`

## 🎯 Características Soportadas

### Tokens Reconocidos
- **Palabras reservadas**: `if`, `else`, `while`, `int`, `double`, `char`, `string`, `class`, `static`, `void`, etc.
- **Operadores**: `+`, `-`, `*`, `/`, `%`, `==`, `!=`, `=`, `&&`, `||`
- **Delimitadores**: `{`, `}`, `(`, `)`, `[`, `]`, `;`, `,`, `.`
- **Literales**: Números enteros, strings (normales e interpolados)
- **Identificadores**: Variables, nombres de clase, métodos

### Gramática Soportada
- Declaración de clases
- Métodos estáticos
- Declaración de variables (`int`, `double`, `char`, `string`)
- Estructuras de control (`if-else`, `while`)
- Expresiones aritméticas y lógicas
- Console.WriteLine

### Validaciones Semánticas
- Variables declaradas antes de uso
- Tipos compatibles en asignaciones
- Ámbito de variables (scope)
- Detección de variables duplicadas

## 📝 Archivos de Log

El sistema genera automáticamente archivos de log con formato:

```
Logs/lexico-{nombre}-{fecha}.txt
Logs/Sintactico-{nombre}-{fecha}.txt
Logs/Semantico-{nombre}-{fecha}.txt
```

Ejemplo de contenido del log léxico:
```
=== Análisis Léxico - codigo ===
Fecha: 27-11-2025
Hora: 14:30:45
==================================================

CLASS(class) en linea 1 posicion 0
ID(Program) en linea 1 posicion 6
LBRACE({) en linea 1 posicion 14
...
```

## 🐛 Solución de Problemas

### Error: ModuleNotFoundError: No module named 'controladores'

Asegúrate de ejecutar desde el directorio correcto:
```bash
cd ProyectoLp
python vistas/ventana_principal.py
```

### Error: No such file or directory: './Logs/...'

El programa crea automáticamente la carpeta `Logs`. Si persiste el error, créala manualmente:
```bash
mkdir Logs
```

## 👥 Autores

- [andrsvb] - Andres Bohorques
- [danny-veliz] - Danny Veliz
- [IsmaelYumi] - Ismael Yumipanta

## 📄 Licencia

Este proyecto es de uso académico.

## 🙏 Agradecimientos

- PLY (Python Lex-Yacc) por facilitar la implementación de compiladores
- Documentación oficial de Python y Tkinter